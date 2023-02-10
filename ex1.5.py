import timeit
import matplotlib.pyplot as plt

def funcMem(n, cache={}):
    if n == 0 or n == 1:
        return n
    else:
        if n in cache:
            return cache[n]
        else:
            cache[n] = funcMem(n-1) + funcMem(n-2)
            return cache[n]


def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)

func_time_list = []
funcMem_time_list = []
for x in range(36):
    func_time = timeit.timeit(lambda : func(x), number=10)
    funcMem_time = timeit.timeit(lambda : funcMem(x), number=10)
    func_time_list.append(func_time)
    funcMem_time_list.append(funcMem_time)

print(func_time_list)
print(funcMem_time_list)

plt.title("Original Function")
plt.xlabel("n")
plt.ylabel("Time")
plt.plot(func_time_list,)
plt.show()
plt.title("Memoization")
plt.xlabel("n")
plt.ylabel("Time")
plt.plot(funcMem_time_list)
plt.show()

plt.title("Both Functions")
plt.xlabel("n")
plt.ylabel("Time")
plt.plot(funcMem_time_list, "-b", label="Memozation")
plt.plot(func_time_list, "-r", label="Original")
plt.legend(loc="upper left")
plt.show()
