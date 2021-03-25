import numpy as np
import time 
filename = 'test_np.dat'
fp = np.memmap(filename, dtype='float32', mode='w+', shape=(3,4))
print(fp)

for i in range(100):
    data = np.ones(12)*i
    data.resize((3,4))
    fp[:] = data[:]
    print('server:',fp)
    time.sleep(1)
