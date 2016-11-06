import timeit
import random

def binary_search(arr, item):
    begin = 0
    end = len(arr) - 1

    while begin <= end:
        mid = (end + begin) // 2
        if arr[mid] == item:
            return mid
        elif arr[mid] < item:
            begin = mid + 1
        else:
            end = mid - 1
    return None

def simple_search(arr, item):
    for i in range(len(arr)):
        if arr[i] == item:
            return i
        
simple_timer = timeit.Timer("simple_search(myarray, random.randint(0, len(myarray)))", "from __main__ import myarray, simple_search, random")
binary_timer = timeit.Timer("binary_search(myarray, random.randint(0, len(myarray)))", "from __main__ import myarray, binary_search, random")
for i in range(10000, 100001, 10000):
    global myarray
    myarray = list(range(i))
    print(simple_timer.timeit(number=1000))
    
for i in range(10000, 100001, 10000):
    global myarray
    myarray = list(range(i))
    print(binary_timer.timeit(number=1000))
    
