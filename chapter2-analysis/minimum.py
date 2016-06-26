import time
import random

def quadratic_minimum(list_of_ints):
    minimum = list_of_ints[0]
    
    for i in list_of_ints:
        isSmallest = True
        for j in list_of_ints:
            if i > j:
                isSmallest = False

        if isSmallest:
            minimum = i

    return minimum

def linear_minimum(list_of_ints):
    minimum = list_of_ints[0]

    for i in list_of_ints:
        if i < minimum:
            minimum = i

    return minimum

if __name__ == "__main__":
    print("== Iterative approach, running time O(n^2) ==")

    for listSize in [100, 1000, 10000]:
        list_of_ints = [random.randrange(100000) for x in range(listSize)]
        start = time.time()
        print(quadratic_minimum(list_of_ints))
        end = time.time()
        print("Size: %d Time: %f" % (listSize, end - start))

    print("== Linear approach, running time O(n) ==")

    for listSize in [100, 1000, 10000]:
        list_of_ints = [random.randrange(100000) for x in range(listSize)]
        start = time.time()
        print(linear_minimum(list_of_ints))
        end = time.time()
        print("Size: %d Time: %f" % (listSize, end - start))
