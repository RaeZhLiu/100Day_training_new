from typing import Mapping
import requests
import threading
import time
from icecream import ic


def download_thread(url):
    # 获取爬取到的文件名
    file_name = url[url.rfind('/') + 1:]
    pic_resp = requests.get(url)
    try:
        with open(r'./Thirteen_day/pic_folder/' + file_name, 'wb') as f:
            f.write(pic_resp.content)
    except Exception as e:
        ic(e)


def main():
    # requests获取url内容
    t_url = "http://api.tianapi.com/txapi/htmlpic/index?" \
        "key=9f626e4aec5d7ce7076d538b7d1a7e4f&" \
        "url=https://www.huceo.com/post/481.html"
    resp = requests.get(t_url)
    # 将返回的json转换为字典
    data_module = resp.json()

    # 定义一个多线程列表t[]
    t = list()
    index = 0
    for mm_dict in data_module["newslist"]:
        g_url = mm_dict["picUrl"]
        t.append(threading.Thread(target=download_thread, args=(g_url,), name="download"))
        t[index].start()
        index += 1

    for i in range(len(t)):
        t[i].join()
    print("Download task has Done!")


if __name__ == "__main__":
    main()
