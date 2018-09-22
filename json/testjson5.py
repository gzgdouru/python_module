import json
text = '''
    {
       "status" : 0
    }
'''
text = open("text.json").read()
out_josn = json.loads(text)
print(out_josn)

hostList = out_josn["hosts"]
for host in hostList:
    print(host)