import sys
import json
import timeit
import matplotlib.pyplot as plt

sys.setrecursionlimit(20000)

def func1(arr, low, high):

    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)

def func2(array, start, end):

    p = array[start]
    low = start + 1
    high = end

    while True:

        while low <= high and array[high] >= p:
            high = high - 1

        while low <= high and array[low] <= p:
            low = low + 1

        if low <= high:
            array[low], array[high] = array[high], array[low]

        else:
            break

    array[start], array[high] = array[high], array[start]

    return high



with open("ex2.json", "r") as jsonFile:
    data = json.load(jsonFile)


time_list = []
index = []
x = 0

for i in data:
    index.append(x)
    n = len(i)
    elapsed_time = timeit.timeit(lambda: func1(i, 0, n-1), number=1)
    x += 1
    time_list.append(elapsed_time)


plt.scatter(index, time_list)
plt.xticks(index)
plt.xlabel("Runs")
plt.ylabel("Seconds")
plt.title("Time For How Long Func1 Takes To Execute")
plt.show()


