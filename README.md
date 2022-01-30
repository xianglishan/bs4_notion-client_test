# bs4 and notion-client sample
---

this isbs4 and notion-client sample
```
./
├── README.md
├── bf4_test.py             scraping example
├── config.py               loads environment
├── main.py                 main
└── test.py                 call notion api
```

request
```json
{
    "header":{
        "x-api-key" : "************"
    }, 
    "body":{
        "tabelog_url" : "https://************", 
        "type" : [
            {"name" : "***"}, 
            {"name" : "----"}
        ]
    }
}
```