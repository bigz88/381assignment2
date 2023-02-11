import matplotlib.pyplot as plt
import json
import sys
import timeit
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

time_list = []
f = open("ex2.json")
data = json.load(f)
for i in range(len(data)):
    func_time = timeit.timeit(lambda : func1(data[i], 0, len(data[i])-1), number=100)
    time_list.append(func_time)

plt.title("Quicksort Time Plot")
plt.xlabel("Array Index")
plt.ylabel("Time")
plt.plot(time_list, "-b", marker=".")
plt.show()