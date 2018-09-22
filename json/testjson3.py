import requests
import json

payload = {
    "name" : "ouru",
    "age" : 25
}

res = requests.get(url='http://httpbin.org/post', data=json.dumps(payload))
print res.text
# out_json = json.loads(res.text)
#
# print out_json