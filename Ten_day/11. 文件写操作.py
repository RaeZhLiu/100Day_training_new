def is_prime(num):
    """判断是否是素数"""
    s = 1
    if num == 1:
        return s - 1
    for i in range(2, num):
        if num % i == 0:
            return s - 1
    return s


def write_func(start, end, file):
    """
    将start及end间的素数写入的file中
    :param start: 开始数
    :param end: 终止数
    :param file: 文件名
    :return: None
    """
    try:
        for num in range(start, end):
            if is_prime(num):
                with open(file, "a", encoding='utf-8') as f:
                    f.write(str(num) + '\n')
    except Exception as result:
        print("未知错误", result)

    print("%d到%d的素数写入完成" % (start, end))


def main():
    write_func(1, 99, "a.txt")
    write_func(100, 999, "b.txt")
    write_func(1000, 9999, "c.txt")


if __name__ == '__main__':
    main()
