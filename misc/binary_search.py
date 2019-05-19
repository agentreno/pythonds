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

# Input array for 3 powers of 10 (1000, 10000, 100000) to illustrate running
# time progression

# Simple search, get average running time over 1000 runs for each input
print("Simple search:")
for i in [10**x for x in range(3,6)]:
    global myarray
    myarray = list(range(i))
    print("n = {}".format(i))
    print(simple_timer.timeit(number=1000))
    
# Binary search
print("Binary search:")
for i in [10**x for x in range(3,6)]:
    global myarray
    myarray = list(range(i))
    print("n = {}".format(i))
    print(binary_timer.timeit(number=1000))
    
