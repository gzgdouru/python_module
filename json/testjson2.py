#coding:utf-8
import json

data = {
    "status" : 0,
    "data" : [
        {
            "type": "light",
            "deviceId": "123123",
            "name" : "灯灯灯灯",
            "actions": {
                "switch": ["on", "off"]
            },
                "state": {
                 "switch": "off"
            }
        }
    ]
}

in_json = json.dumps(data, skipkeys=True, indent=4)
print in_json

print "-" * 80

out_json = json.loads(in_json)
print out_json["status"]
print out_json["data"][0]["state"]
print out_json["data"][0]["actions"]["switch"]