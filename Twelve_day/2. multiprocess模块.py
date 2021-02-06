import os
from multiprocessing import Process


def child_poc(name):
    print("Run child process %s (%s)..." % (name, os.getpid()))


def parent():
    print("Parent process %s." % os.getpid())
    p = Process(target=child_poc, args=("test",))
    print("Process will start!")
    p.start()
    p.join()
    print("Process end")


if __name__ == '__main__':
    parent()
