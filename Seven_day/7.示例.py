import sys


def fib(num):
    fn, fn_1 = 0, 1
    for _ in range(num):
        fn, fn_1 = fn_1, fn + fn_1
        yield fn


def main():
    for value in fib(20):
        print(value)


if __name__ == '__main__':

    s1 = r'\'hello, world!\''
    s2 = r'\n\\hello, world!\\\n'
    print(s1, s2, end='\n')

    a, b = 5, 10
    print(f"{a} * {b} = {a * b}")

    list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
    list2 = sorted(list1)
    # sorted函数返回列表排序后的拷贝不会修改传入的列表
    # 函数的设计就应该像sorted函数一样尽可能不产生副作用
    list3 = sorted(list1, reverse=True)
    # 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
    list4 = sorted(list1, key=len)
    print(list1)
    print(list2)
    print(list3)
    print(list4)
    # 给列表对象发出排序消息直接在列表对象上进行排序
    list1.sort(reverse=True)
    print(list1)

    # 列表生成
    lis = [x for x in range(1, 10)]
    print(lis)

    lis1 = [x + y for x in 'abcde' for y in '123456']
    print(lis1)

    f = [x ** 2 for x in range(1, 1000)]
    print('--------------')
    print(f)
    print('-' * 50)
    print(sys.getsizeof(f))

    f1 = (x ** 2 for x in range(1, 1000))
    print(f1)
    for val in f1:
        print(val, end=' ')
    print("f1所占用内存：", sys.getsizeof(f1))
    print("f所占用内存：", sys.getsizeof(f))

    main()

    # 创建字典的字面量语法
    scores = {'骆昊': 95, '白元芳': 78, '狄仁杰': 82}
    print(scores)
    # 创建字典的构造器语法
    items1 = dict(one=1, two=2, three=3, four=4)
    # 通过zip函数将两个序列压成字典
    items2 = dict(zip(['a', 'b', 'c'], '123'))
    # 创建字典的推导式语法
    items3 = {num: num ** 2 for num in range(1, 10)}
    print(items1, items2, items3)
    # 通过键可以获取字典中对应的值
    print(scores['骆昊'])
    print(scores['狄仁杰'])
    # 对字典中所有键值对进行遍历
    for key in scores:
        print(f'{key}: {scores[key]}')
    # 更新字典中的元素
    scores['白元芳'] = 65
    scores['诸葛王朗'] = 71
    scores.update(冷面=67, 方启鹤=85)
    print(scores)
    if '武则天' in scores:
        print(scores['武则天'])
    print(scores.get('武则天'))
    # get方法也是通过键获取对应的值但是可以设置默认值
    print(scores.get('武则天', 60))
    # 删除字典中的元素
    print(scores.popitem())
    print(scores.popitem())
    print(scores.pop('骆昊'))
    # 清空字典
    scores.clear()
    print(scores)
