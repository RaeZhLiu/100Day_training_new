from time import sleep
from icecream import ic
from selenium import webdriver


def main():
    drive = webdriver.Chrome()

    # url = "http://www.baidu.com"
    url = r"file:///Users/liuzhihui/Desktop/Learning/%E9%98%B6%E6%AE%B57-%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95%E5%BC%80%E5%8F%91/%E9%98%B6%E6%AE%B57-%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95%E5%BC%80%E5%8F%91/%E4%BB%A3%E7%A0%81%E4%BB%A5%E5%8F%8A%E5%85%B6%E4%BB%96/day05-web%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95/02-%E8%B5%84%E6%96%99/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html"
    drive.get(url)
    try:
        # id定位
        input01 = drive.find_element_by_id("userA")
        input01.send_keys("admin")
        sleep(1)
        # name定位
        input02 = drive.find_element_by_name("passwordA")
        input02.send_keys("123456")
        sleep(1)
        # class name定位
        input03 = drive.find_element_by_class_name("telAHHH")
        input03.send_keys("18830222351")
        sleep(1)
        # tag name定位
        input03 = drive.find_elements_by_tag_name("input")
        input03[3].send_keys("heima@itcaset.cn")
        sleep(1)
        # link text定位-全部匹配
        input04 = drive.find_element_by_partial_link_text("AA 百度 网站")
        input04.click()
        sleep(1)
        # link text定位-部分匹配
        input05 = drive.find_element_by_partial_link_text("官方")
        input05.click()
        sleep(1)
    except Exception as e:
        ic(e)
    finally:
        sleep(3)
        drive.quit()


if __name__ == '__main__':
    main()
