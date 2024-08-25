from json import loads

raw_json = input()
parsed_json = loads(raw_json)

def crawl_json(json):
    the_type = type(json)
    global total
    if the_type is int:
        total += json
    elif the_type is list:
        for item in json:
            crawl_json(item)
    elif the_type is dict:
        if 'red' in json.values():
            return
        for item in json.values():
            crawl_json(item)

total = 0
crawl_json(parsed_json)

print(total)
