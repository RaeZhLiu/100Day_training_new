"""
输入M和N计算C(M,N)
(M-1)! / (N-1)! / (M-N)!

Version: 0.1
Author: zhihui Liu
"""


def fac(value):
    """求阶乘"""
    result = 1

    for i in range(1, value):
        result *= i
    print(result)

    return result


if __name__ == '__main__':
    m = int(input("M= "))
    n = int(input("N= "))

    print(fac(m) // fac(n) // fac(m - n))
