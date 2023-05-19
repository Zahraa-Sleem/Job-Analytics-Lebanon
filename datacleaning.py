import json
with open('objects.json') as f:
    data = json.load(f)
with open('bagofwords.json') as b:
    bag=json.load(b)
for element in data:
    element['jobtitle']=element['jobtitle'].replace("/n",'').strip()
    if ',' in element['location']:
        element['location']=element['location'].split(",")[1]
        print(element['location'])
    element["tags"]=[]
    words=element['jobtitle'].split()
    for item in bag:
        common_elements = set(map(str.lower, words)).intersection(map(str.lower, item['Keywords']))
        if(len(common_elements)):
          element["tags"].append(item["tag"])  
     
with open("objects.json", "w") as f:
    json.dump(data, f, indent=2)  
 