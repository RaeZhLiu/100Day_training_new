import threading

num = 0
lock = threading.Lock()


class MyThread(threading.Thread):

    def run(self) -> None:
        global num
        print("Thread %s is Running...." % threading.current_thread().name)
        for _ in range(1000000):
            lock.acquire()
            num += 1
            lock.release()
        print("Thread %s is Ended...." % threading.current_thread().name)


def main():
    print("Thread %s is Running..." % threading.current_thread().name)
    t1 = MyThread()
    t1.start()
    t2 = MyThread()
    t2.start()
    t1.join()
    t2.join()
    print("Thread %s is Ended..." % threading.current_thread().name)
    print("global num = %d" % num)


if __name__ == '__main__':
    main()
