import timeit

def enqueueNItems(queue, n):
   for i in range(n):
      queue.enqueue(i)

def testEnqueue():
   print("==Analysis of enqueue complexity==")
   enqueueTimer = timeit.Timer("enqueueNItems(myqueue, n)",
      "from __main__ import enqueueNItems, n; "
      "from queue import Queue; myqueue = Queue()"
   )
   enqueueAltTimer = timeit.Timer("enqueueNItems(myqueue, n)",
      "from __main__ import enqueueNItems, n; "
      "from queue import QueueAlt; myqueue = QueueAlt()"
   )
   print("n     Queue      QueueAlt")
   print("=========================")
   global n
   for n in range(10,101,10):
      enqueueTime = enqueueTimer.timeit(number=1000)
      enqueueAltTime = enqueueAltTimer.timeit(number=1000)
      print("%d,%10.3f,%10.3f" % (n, enqueueTime, enqueueAltTime))

if __name__ == "__main__":
   testEnqueue()
