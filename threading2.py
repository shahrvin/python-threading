import threading
import logging 
import time


def thread_func(name):
    logging.info("thread %s: starting",name)
    time.sleep(2)
    logging.info("thread %s: finishing", name)

if __name__ == "__main__":
    logging.basicConfig(format= "%(asctime)s: %(message)s", level=logging.INFO, datefmt="%H: %M: %S")
    logging.info("main: before creating threads")

    threads = list()
    for index in range(3):
        logging.info("main:  create and start thread %d.", index)

        x  = threading.Thread(target=thread_func, args= (index,))
        threads.append(x)
        x.start()

    for index , thread in enumerate(threads):

        logging.info("main: before joining thread %d", index)
        thread.join()
    
        logging.info("main: thread %d is done.", index)
    



