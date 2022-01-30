import config
from notion_client import Client
import bf4_test

notion = Client(auth=config.NOTION_KEY)

## 以下を受け取る
# T_url = 'tabelog_url'
# type = [
#     {'name':'+++'}, 
#     {'name':'***'}, 
#     {'name':'---'}
# ]

def notion_api(T_url, type):
    ## 以下を上記食べログurlからスクレイピングする
    params =  bf4_test.catch_param(T_url)

    address = params['address']
    fig_url = params['fig_url']
    rest_name = params['rest_name']
    station = params['station']
    good = params['good']
    dinner_cost = params['dinner_cost']
    lunch_cost = params['lunch_cost']
    business_hours = params['business_hours']


    ## データベースに上記urlの店のレコードを追加
    notion.pages.create(
        **{
            'object': 'page',
            'parent': { 'database_id': config.NOTION_DATABASE_ID },
            'properties': {
                'TabeLog url': {
                    'url': T_url
                },
                'address': {
                    'rich_text': [
                        {
                            'text': {
                                'content': address
                            }
                        }
                    ]
                },
                'fig': {
                    'files': [
                        {'external': {'url': fig_url},
                                    'name': 'fig_name01',
                                    'type': 'external'}]
                },
                'name': {
                    'title': [{
                        'text': {
                            'content': rest_name
                        }
                    }],
                },
                'nearest station': {
                    'multi_select': station
                },
                'type': {
                    'multi_select': type
                },
                'whats good?': {
                    'multi_select': good
                }, 
                'dinner cost': {
                    'rich_text': [
                        {
                            'text': {
                                'content': dinner_cost
                            }
                        }
                    ]
                }, 
                'lunch cost': {
                    'rich_text': [
                        {
                            'text': {
                                'content': lunch_cost
                            }
                        }
                    ]
                }, 
                'business_hours': {
                    'rich_text': [
                        {
                            'text': {
                                'content': business_hours
                            }
                        }
                    ]
                }
            }
        }
    )


    ## たった今追加したレコードのpage_idを持ってくる
    db = notion.databases.query(
        **{
            'database_id' : config.NOTION_DATABASE_ID, # データベースID
            "filter": {
                "property": "name",
                'title': {
                    "contains": rest_name
                }
            }
        }
    )
    page_id = db['results'][0]['id']


    ## 上記新規追加したページの中身に画像urlを追加
    notion.blocks.children.append(
        **{
            'block_id' : page_id, 
            'children':[
                {
                    'image': {'caption': [],
                            'external': {'url': fig_url},
                            'type': 'external'},
                    'object': 'block',
                    'type': 'image'
                }
            ]
        }
    )