from functools import wraps


def new_decorator(func):
    @wraps(func)
    def fun2():
        print("I am doing some boring work before executing func()")
        func()
        print("I am doing some boring work after executing func()")

    return fun2


# @new_decorator 等价于 func1 = new_decorator(func1)
@new_decorator
def func1():
    print("I'm Func1")


if __name__ == '__main__':

    func1()
    print(func1.__name__)
    # func1 = new_decorator(func1)
    # func1()

