import timeit

mydict = { k:None for k in range(10000) }

def testGetSetDict():
   for i in range(10000, 100001, 10000):
      setTimer = timeit.Timer('setDict(%d, 0, mydict)' % i,
            'from __main__ import setDict, mydict')
      setTime = setTimer.timeit(number=1000)
      print('n = %d, time = %10.3f' % (i, setTime))

# Run a set value operation on provided dict n times for key k
def setDict(n, k, adict):
   for i in range(n):
      adict[k] = 1

if __name__ == "__main__":
   print("==Dictionary set operation analysis==")
   testGetSetDict()
