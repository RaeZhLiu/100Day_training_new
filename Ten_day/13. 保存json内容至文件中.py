import json


def save(obj):
    if type(obj) != dict:
        print("请输入json文本")
        return
    try:
        with open("json.txt", 'w', encoding='utf-8') as f:
            json_obj = json.dumps(obj, ensure_ascii=False)
            f.write(json_obj)
    except IOError as e:
        print(e)
    print("Save Done!")
    print(type(json_obj))

    return


def read(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as fr:
            content = fr.read()
            obj_json = json.loads(content)
            print(obj_json)
    except IOError as e:
        print(e)
    print("Read Done!")
    print(type(obj_json))
    return


def main():
    dic = {
        "name": "骆昊",
        "age": 38,
        "qq": 957658,
        "friends": ["王大锤", "白元芳"],
        "cars": [
            {"brand": "BYD", "max_speed": 180},
            {"brand": "Audi", "max_speed": 280},
            {"brand": "Benz", "max_speed": 320}
        ]
    }
    save(dic)
    read("json.txt")


if __name__ == '__main__':
    main()
