import time

def iterativeSum(n):
    start = time.time()

    theSum = 0
    for i in range(1, n+1):
        theSum += i

    end = time.time()

    return (theSum, end - start)

def fixedSum(n):
    start = time.time()

    theSum = (n * (n+1)) / 2

    end = time.time()

    return (theSum, end - start)

if __name__ == "__main__":
    print("== Iterative approach, running time O(n) ==")
    print("N = 10000")
    for i in range(5):
        print("Sum is %d required %10.7f seconds" % iterativeSum(10000))
    print("N = 100000")
    for i in range(5):
        print("Sum is %d required %10.7f seconds" % iterativeSum(100000))
    print("N = 1000000")
    for i in range(5):
        print("Sum is %d required %10.7f seconds" % iterativeSum(1000000))

    print("== Fixed approach, running time O(1) ==")
    print("N = 10000")
    for i in range(5):
        print("Sum is %d required %10.7f seconds" % fixedSum(10000))
    print("N = 100000")
    for i in range(5):
        print("Sum is %d required %10.7f seconds" % fixedSum(100000))
    print("N = 1000000")
    for i in range(5):
        print("Sum is %d required %10.7f seconds" % fixedSum(1000000))
