settings = {
    "title":"糖尿病智慧化管理平台API",
    "description":"測試版本供手機APP與網頁版使用",
    "version":"1.0.0",
    "hide_top_bar":True
}

template = {
    "swagger":"2.0",
    "hide_top_bar":True,
    "info":{
        "title": "糖尿病智慧化管理平台API",
        "description": "測試版本供手機APP與網頁版使用, 版權所屬:喬不攏",
        "contact":{
            "responsibleOrganization":"喬不攏",
            "responsibleDeveloper":"Leon Lin",
            "email":"i88828702@gmail.com"
        },
    "servers":{
        "url":"127.0.0.1:8016"
    },
    "version":"1.0.0"
    },
    "host":"127.0.0.1:8016",
    "basePath":"",
    "tags":[
        {
            "name":"Test",
            "description":"連線測試"
        },
        {
            "name":"Self Health Data",
            "description":"自主監測數據"
        },
        {
            "name": "Users",
            "description": "使用者資訊"
        },
        {
            "name": "Basic Information",
            "description": "系統基礎設定"
        },
    ],
    "schemes":[
        "http",
        "https"
    ]
}