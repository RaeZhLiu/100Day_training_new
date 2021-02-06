from multiprocessing import Process, Queue
import time


# 向队列中写数据
def write(q):
    try:
        n = 1
        while n < 5:
            print("write, %d" % n)
            q.put(n)
            time.sleep(1)
            n += 1
    except BaseException:
        print("write_task error!")
    finally:
        print("write_task end!!!")


# 从队列中读数据
def read(q):
    try:
        n = 1
        while n < 5:
            print("read, %d" % q.get())
            time.sleep(1)
            n += 1
    except BaseException:
        print("read_task error!")
    finally:
        print("read_task end!!!")


def main():
    q = Queue()     # 父进程创建Queue，并传给各个子进程
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))

    pw.start()
    pr.start()
    pw.join()
    pr.join()
    print("Done!!!!!!")


if __name__ == '__main__':
    main()

