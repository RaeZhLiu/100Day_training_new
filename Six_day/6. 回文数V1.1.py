def is_palindrome(num):
    tmp = num
    total = 0

    # 将num逆序为total
    while tmp:
        total = total * 10 + tmp % 10
        tmp //= 10
    print(total)

    return num == total


if __name__ == '__main__':
    value = int(input("请输入要判断的数字："))

    if is_palindrome(value):
        print("%d 是回文数" % value)
    else:
        print("%d 不是回文数" % value)