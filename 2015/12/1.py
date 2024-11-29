from json import loads

def crawl_json(json):
    json_type = type(json)

    if json_type is int:
        return json
    elif json_type is str:
        return 0
    elif json_type is list:
        return sum(map(crawl_json, json))
    elif json_type is dict:
        return sum(map(crawl_json, json.values()))

input_json = loads(input())
print(crawl_json(input_json))
