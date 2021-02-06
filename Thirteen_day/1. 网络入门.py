import time
from threading import Thread
import requests
# import re


class DownloadHandler(Thread):

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        # pattern = re.compile('')
        file_name = self.url[self.url.rfind('/') + 1:]
        resp = requests.get(self.url)
        with open('test/' + file_name, 'wb') as f:
            f.write(resp.content)


def main():
    # 通过requests模块的get函数获取网络资源
    w_url = "http://api.tianapi.com/txapi/htmlpic/index?" \
          "key=9f626e4aec5d7ce7076d538b7d1a7e4f&" \
          "url=https://www.huceo.com/post/481.html"
    resp = requests.get(w_url)
    # 将服务器返回的JSON格式数据保存为字典
    data_module = resp.json()
    for mm_dict in data_module["newslist"]:
        url = mm_dict["picUrl"]
        # 通过多线程的方式下载图片
        download = DownloadHandler(url)
        download.start()


if __name__ == '__main__':
    main()
