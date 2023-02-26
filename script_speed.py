import timeit

def slow_function():
    t = []
    for i in range(10000):
        t.append(i)
    return t

def faster_function():
    t = []
    l = t.append    
    for i in range(10000):
        l(i)
    return t

def fastest_function():
    return [i for i in range(10000)]

# slow_function timeout
t1 = timeit.timeit(slow_function, number=100)
print("Time taken by slow_function: ", t1)

# faster_function timeout
t2 = timeit.timeit(faster_function, number=100)
print("Time taken by faster_function: ", t2)

# fastest_function timeout
t3 = timeit.timeit(fastest_function, number=100)
print("Time taken by fastest_function: ", t3)