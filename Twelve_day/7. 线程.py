import threading
from icecream import ic
import time


def test(name):
    print('thread %s is running...' % threading.current_thread().name)
    print('hello', name)
    print('thread %s ended.' % threading.current_thread().name)


def main():
    ic("thread %s is running..." % threading.current_thread().name)
    ic("hello world")
    t = threading.Thread(target=test, args=('test',), name="Thread_test")
    t.start()
    t.join()
    ic('thread %s ended.' % threading.current_thread().name)


if __name__ == '__main__':
    main()
