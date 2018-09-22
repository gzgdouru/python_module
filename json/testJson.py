import json

data = {
    "spam" : "foo",
    "parrot" : 42
}

data2 = {
    "type" : "text1",
    "name" : "zhan"
}

data3 = [data, data2]

in_json = json.dumps(data, skipkeys=True, indent=4)
print in_json

out_json = json.loads(in_json)
print out_json["spam"]

# in_json = json.dumps(data3, skipkeys=True, indent=4)
# print in_json