import json
import matplotlib.pyplot as plt
import timeit

def func1(arr):
    list = []
    list.append((0, len(arr) - 1))

    while list:
        low, high = list.pop()
        if low < high:
            pi = func2(arr, low, high)
            list.append((low, pi - 1))
            list.append((pi + 1, high))
    
def func2(arr, start, end):
    high = end
    p = arr[high]
    i = start - 1
    low = start

    for j in range(low, high):
        if arr[j] <= p:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


time_list = []
f = open("ex2.json")
data = json.load(f)

for i in range(len(data)):
    func_time = timeit.timeit(lambda : func1(data[i]), number=100)
    time_list.append(func_time)

plt.title("Quicksort Non-recursive Time Plot")
plt.xlabel("Array Index")
plt.ylabel("Time")
plt.plot(time_list, "-r", marker=".")
plt.show()