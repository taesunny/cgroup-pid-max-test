import threading
import os

def execute(index):
    print(index, "th created thread, process id", os.getpid(), "thread id: ", threading.get_ident())
    time.sleep(1000000000)

print("Start!")

for i in range(150):
    t = threading.Thread(target=execute, args=(i))
    t.daemon = True
    t.start()

print("Main Thread")
time.sleep(2000000000)