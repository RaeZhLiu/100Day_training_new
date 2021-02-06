def main():
    try:
        with open("/Users/liuzhihui/Downloads/图片2.png", 'rb') as f1:
            data = f1.read()
            print(type(data))
        with open("复制图片2.png", 'wb') as f2:
            f2.write(data)
    except FileNotFoundError as e:
        print('指定的文件无法打开.')
    except IOError as e:
        print('读写文件时出现错误.')
    print("程序执行结束")


if __name__ == '__main__':
    main()
