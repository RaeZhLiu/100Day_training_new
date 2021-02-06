def gys(x, y):
    """计算最大公约数"""
    if x < y:
        y, x = x, y

    for tmp in range(y, 0, -1):
        if x % tmp == 0 and y % tmp == 0:
           return tmp


def gbs(x, y):
    """计算最小公倍数"""
    result = x * y // gys(x, y)
    return result


if __name__ == '__main__':
    m = int(input("M= "))
    n = int(input("N= "))

    print("%d 和 %d 的最大公约数为 %d" % (m, n, gys(m, n)))
    print("%d 和 %d 的最小公倍数为 %d" % (m, n, gbs(m, n)))
