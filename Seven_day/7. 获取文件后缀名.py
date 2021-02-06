def get_suffix(filename, has_dot=False):
    """
    获取给定文件的后缀名
    :param filename: 文件名
    :param has_dot: 返回的后缀名是否需要带点
    :return: 文件的后缀名
    """
    pos = 0
    for index in range(len(filename) - 1, 0, -1):
        # 遍历字符串，查找最后'.'的索引值
        if filename[index] == '.':
            pos = index if has_dot else index + 1
            break
    else:
        return '所输入文件名不带后缀，请重新输入'

    return filename[pos:]


if __name__ == '__main__':
    file = input("请输入文件名：")
    print("文件后缀为：", get_suffix(file))
