def max2(lis):
    x0, x1 = 0, 0
    for i in range(0, len(lis)):
        if lis[i] > x0:
            x0, x1 = lis[i], x0
        elif lis[i] > x1:
            x1 = lis[i]

    return x0, x1


if __name__ == '__main__':
    print(max2([5, 1, 2, 4, 10]))
