import numpy as np
import time 
filename = 'test_np.dat'
# fp = np.memmap(filename, dtype='float32', mode='w+', shape=(3,4))
fp = np.memmap(filename, dtype='<U100', mode='w+', shape=(3,4)) # 传输字符串,U:字符串，100 字符串的最大长度
print(fp)

for i in range(100):
    # data = np.ones(12)*i # float
    data= np.array([f'{i}-{i}']*12) # 字符串
    data.resize((3,4))
    fp[:] = data[:]
    print('server:',fp)
    time.sleep(1)
