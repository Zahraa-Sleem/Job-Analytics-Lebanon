import json
with open('objects.json') as f:
    data = json.load(f)
for element in data:
    element['jobtitle']=element['jobtitle'].replace("/n",'').strip()
with open("objects.json", "w") as f:
    json.dump(data, f, indent=2)   