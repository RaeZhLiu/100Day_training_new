def main():
    try:
        with open("致橡树.txt", "r") as f:
            content = f.read()

        print(content)
    except FileNotFoundError:
        print("文件不存在，打开失败")


if __name__ == '__main__':
    main()
