def gys(x, y):
    """计算最大公约数"""
    if x < y:
        x, y = y, x

    while x % y:
        tmp = x % y

        if y != 1:
            if tmp < y:
                x, y = y, tmp
            else:
                x = tmp
        else:
            return y
    return y


def gbs(x, y):
    """计算最小公倍数"""
    result = x * y / gys(x, y)
    return result


if __name__ == '__main__':
    m = int(input("M= "))
    n = int(input("N= "))

    print("%d 和 %d 的最大公约数为 %d" % (m, n, gys(m, n)))
    print("%d 和 %d 的最小公倍数为 %d" % (m, n, gbs(m, n)))
