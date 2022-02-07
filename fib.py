import decimal
import time
start_time = time.time()



def iterativeFib(n):
    a, b = 0, 1

    for i in range(n):
        a, b = b, a + b

    return a

n = int(input())
print(iterativeFib(n))
print("--- %s seconds ---" % (time.time() - start_time))
