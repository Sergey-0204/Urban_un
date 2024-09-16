# import threading
# import time
#
#
# def some_func():
#     time.sleep(4)
#     raise Exception
#
#
#
# def thread_func():
#     try:
#         some_func()
#     except Exception as e:
#         pass
#
# t1 = threading.Thread(target=thread_func)
# t2 = threading.Thread(target=thread_func)
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()

import threading

import threading
import time


def some_func():
    time.sleep(4)
    raise Exception


def excepthook(args):
    print(args.thread.name)


threading.excepthook = excepthook

tr1 = threading.Thread(target=some_func)
tr2 = threading.Thread(target=some_func)

tr1.start()
tr2.start()

tr1.join()
tr2.join()