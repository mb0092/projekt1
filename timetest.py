from time import time

start = int (time())

for x in range(1,100000000):
    result = 23*2.3
    x += 1

end = int(time())
print(end - start)