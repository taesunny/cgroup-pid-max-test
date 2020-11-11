from multiprocessing import Process
import threading
import argparse
import os
import time

def execute_for_process(index):
    print(index, "th created process, id", os.getpid())
    time.sleep(1000000)

def execute_for_thread(index):
    print(index, "th created thread, process id", os.getpid(), "thread id: ", threading.get_ident())
    time.sleep(1000000)

def create_processes(howmany):
    for i in range(1, howmany+1):
        proc = Process(target=execute_for_process, args=(i,))
        proc.start()

def create_threads(howmany):
    for i in range(1, howmany+1):
        t = threading.Thread(target=execute_for_thread, args=(i,))
        t.daemon = True
        t.start()

def create_processes_n_threads(howmany):
    count = 0

    while count < howmany:
        proc = Process(target=execute_for_process, args=(count+1,))
        proc.start()
        count += 1

        if count > howmany:
            break

        t = threading.Thread(target=execute_for_thread, args=(count+1,))
        t.daemon = True
        t.start()
        count += 1

if __name__ == '__main__':
    print("Start!")

    # parser = argparse.ArgumentParser()
    # parser.add_argument('--mode', type=str, help="test mode (process/thread, default: process)")
    # parser.add_argument('--howmany', type=int, help="enter how many process or thread do you want to create")

    # args = parser.parse_args()

    # mode = args.mode
    # howmany = args.howmany

    mode = os.getenv('MODE', 'process')
    howmany = int(os.getenv('HOWMANY', '1'))

    print("Test Mode : ", mode)
    print("Target Number to create process/thread/each of process and thread : ", howmany)

    if mode == "thread":
        create_threads(howmany)
    elif mode == "process":
        create_processes(howmany)
    elif mode == "both":
        create_processes_n_threads(howmany)
    else:
        print("input error, please restart again")

    print("Main process")

    time.sleep(2000000)