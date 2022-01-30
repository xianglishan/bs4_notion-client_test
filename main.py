import json
import test

def lambda_handler(event, context):
    T_url = event['tabelog_url']
    type = event['type']
    
    test.notion_api(T_url, type)
    
    res = {
        "message":"ok!! posted!!!"
    }
    
    return json.dumps(res)