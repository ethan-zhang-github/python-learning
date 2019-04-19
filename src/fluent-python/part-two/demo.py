import array
import random

floats = array.array('d', (random.random() for i in range(10**7)))
# print(floats[-1])

fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()
floats2 = array.array('d')
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10**7)
fp.close()
print(floats2[-1])
print(floats == floats2)
