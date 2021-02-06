import re


def func(m):
    print(m)
    return 'hi' + ' ' + m.group(2)


if __name__ == '__main__':
    p = re.compile(r'(\w+) (\w+)')
    s = 'hello 123, hello 456'
    print(p.sub(r'hello world', s))     # 使用 'hello world' 替换 'hello 123' 和 'hello 456'
    print(p.sub(r'\2 \1', s))       # 引用分组
    print(p.sub(func, s))
    print(p.sub(func, s, 1))    # 最多替换一次
