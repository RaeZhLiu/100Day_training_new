import os
import time
import multiprocessing


def func(num):
    print("Run task %s (pid:%s)..." % (num, os.getpid()))
    time.sleep(2)
    print("Task %s^2 result is %s" % (num, num * num))


def main():
    print("Parent process is %s" % os.getpid())
    p = multiprocessing.Pool(4)     # 设置进程数
    for i in range(5):
        p.apply_async(func, args=(i,))  # 设置每个进程要执行的函数和参数
    print("Waiting for all subProcesses done...")
    p.close()
    p.join()
    print("All subProcesses done.")


if __name__ == '__main__':
    main()
