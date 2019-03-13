ref: https://www.youtube.com/watch?v=9N6a-VLBa2I

+ json.load() vs json.loads()
- json.load(file)  # load json direct from file
- json.loads(json_string) # load json from a string in your code

+ json.dump() vs json.dumps(): similar to load() and loads()

+ dump to json file with unicode format

with open('new_ichat_db.json','w', encoding = 'utf-8') as f:
    json.dump(data, f,indent = 2, ensure_ascii = False)



