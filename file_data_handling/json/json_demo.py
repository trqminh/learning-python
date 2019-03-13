import json


with open('ichat_db.json') as f:
    data = json.load(f)

for group in data['Groups'].values():
    for group_id in group.keys():
        print(group[group_id])
        del group[group_id]['name']


with open('new_ichat_db.json','w', encoding = 'utf-8') as f:
    json.dump(data, f,indent = 2, ensure_ascii = False)




        
