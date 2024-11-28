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
        values = json.values()

        if 'red' in values:
            return 0
        else:
            return sum(map(crawl_json, values))

print(crawl_json(loads(input())))
