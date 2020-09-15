import time
import threading

start = time.perf_counter()

def do_something(i):
    if i % 2 == 0:
        print('even')
    else:
        print('odd')
    print('Sleeping 1 sec')
    time.sleep(1)
    print('Done sleeping')

threads = []

for _ in range(10):
    t = threading.Thread(target=do_something,args=[_])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()


print(round(time.perf_counter()-start),' secs')
