def is_palindrome(num):
    str_num = str(num)

    print("%s 类型是 %s" % (str_num, type(str_num)))
    # 字符串逆序
    reverse_num = str_num[::-1]
    print("%s 类型是 %s" % (reverse_num, type(reverse_num)))

    return str_num == reverse_num


if __name__ == '__main__':
    value = int(input("请输入要判断的数字："))

    if is_palindrome(value):
        print("%d 是回文数" % value)
    else:
        print("%d 不是回文数" % value)
