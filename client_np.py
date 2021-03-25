import numpy as np
import time
import threading 
filename = 'test_np.dat'


def client(cid):
    for i in range(100):
        newfp = np.memmap(filename, dtype='float32', mode='r', shape=(3,4))
        print(f'client:{cid}',newfp[0][0])
        time.sleep(1)

cids = [1,2]
for cid in range(1000):
    t = threading.Thread(target=client,args=[cid])
    t.start()