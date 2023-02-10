import timeit
import matplotlib.pyplot as plt


def funcI(n, cache={0:0, 1:1}):
    if n not in cache:
        cache[n] = funcI(n-1, cache) + funcI(n-2, cache)
    return cache[n]


def funcO(n):
    if n == 0 or n == 1:
        return n
    else:
        return funcO(n-1) + funcO(n-2)


timeI = []
timeO = []
value = []

for i in range(0, 36):
    time = timeit.timeit(lambda : funcI(i), number = 1)
    timeI.append(time)
    value.append(i)

for i in range(0, 36):
    time0 = timeit.timeit(lambda : funcO(i), number = 1)
    timeO.append(time0)

plt.scatter(value, timeI, c = "r")
plt.scatter(value, timeO, c = "b")
plt.ylabel("time (sec)")
plt.xlabel("value")
plt.title("Value vs. Run-time for both algorithms")
plt.legend(["Imporved func", "Original func"])
plt.show()

#print(timeI)