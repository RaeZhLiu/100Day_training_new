import requests
import json


def main():

    param = {
        "key": "9f626e4aec5d7ce7076d538b7d1a7e4f",
        "city": "上海"

    }
    r = requests.get("http://api.tianapi.com/txapi/worldtime/index", params=param)
    data_module = json.loads(r.text)
    print(type(data_module))
    print(data_module)
    for new in data_module['newslist']:
        print(new['strtime'])


if __name__ == '__main__':
    main()
