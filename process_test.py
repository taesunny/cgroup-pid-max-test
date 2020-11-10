import multiprocessing import Process
import os

def execute(index):
    print(index, "th created process, id", os.getpid())
    time.sleep(1000000000)

print("Start!")

procs = []

for i in range(150):
    proc = Process(target=execute, arges=(i))
    procs.append(proc)
    proc.start()

print("Main process")
time.sleep(2000000000)