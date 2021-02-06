from threading import Thread, current_thread, Lock
from icecream import ic
from datetime import date, datetime, time
import time

num = 0
lock = Lock()


def thread_test():
    global num
    ic("Thread %s is Running..." % current_thread().name)
    for _ in range(1000000):
        lock.acquire()  # 添加锁
        num += 1
        lock.release()  # 释放锁
    ic("Thread %s is Ended..." % current_thread().name)


def main():
    start_time = datetime.now()
    start_time1 = time.clock()
    ic("Thread %s is Running..." % current_thread().name)
    t = list()
    for i in range(5):
        t.append(Thread(target=thread_test, name="thread" + str(i+1)))
        t[i].start()
    for i in range(5):
        t[i].join()

    ic("global num: ", num)
    ic("Thread %s is Ended..." % current_thread().name)
    end_time = datetime.now()
    end_time1 = time.clock()
    ic(end_time - start_time, end_time1 - start_time1)


if __name__ == '__main__':
    main()
