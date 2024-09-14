import threading
import logging 
import time


def thred_func(name):
    logging.info("thread %s: starting",name)
    time.sleep(2)
    logging.info("thread %s: finishing", name)

if __name__ == "__main__":
    logging.basicConfig(format= "%(asctime)s: %(message)s", level=logging.INFO, datefmt="%H: %M: %S")
    logging.info("main: before creating thread")
    x  = threading.Thread(target=thred_func, args= (1,))
    logging.info("main: before running thread")
    x.start()
    logging.info("main: wait for thread to finish")
    # x.join()
    logging.info("main: all done")



