import timeit

def enqueueNItems(queue, n):
   for i in range(n):
      queue.enqueue(i)

def dequeueNItems(queue, n):
   for _ in range(n):
      queue.dequeue()

def testEnqueue():
   queueEnqTimer = timeit.Timer("enqueueNItems(myqueue, n)",
      "from __main__ import enqueueNItems, n; "
      "from queue import Queue; myqueue = Queue()"
   )
   altqueueEnqTimer = timeit.Timer("enqueueNItems(myqueue, n)",
      "from __main__ import enqueueNItems, n; "
      "from queue import QueueAlt; myqueue = QueueAlt()"
   )
   fasterqueueEnqTimer = timeit.Timer("enqueueNItems(myqueue, n)",
      "from __main__ import enqueueNItems, n; "
      "from queue import FasterQueue; myqueue = FasterQueue()"
   )
   queueDeqTimer = timeit.Timer("dequeueNItems(myqueue, n)",
      "from __main__ import enqueueNItems, dequeueNItems, n; "
      "from queue import Queue; myqueue = Queue(); "
      "enqueueNItems(myqueue, 55000)"
   )
   altqueueDeqTimer = timeit.Timer("dequeueNItems(myqueue, n)",
      "from __main__ import enqueueNItems, dequeueNItems, n; "
      "from queue import QueueAlt; myqueue = QueueAlt(); "
      "enqueueNItems(myqueue, 55000)"
   )
   fasterqueueDeqTimer = timeit.Timer("dequeueNItems(myqueue, n)",
      "from __main__ import enqueueNItems, dequeueNItems, n; "
      "from queue import FasterQueue; myqueue = FasterQueue(); "
      "enqueueNItems(myqueue, 55000)"
   )
   print("n       q-enq      q-deq    alt-enq    alt-deq    fast-enq    fast-deq")
   print("======================================================================")
   global n
   for n in range(10,101,10):
      queueEnqTime = queueEnqTimer.timeit(number=1000)
      altqueueEnqTime = altqueueEnqTimer.timeit(number=1000)
      fasterqueueEnqTime = fasterqueueEnqTimer.timeit(number=1000)
      queueDeqTime = queueDeqTimer.timeit(number=100)
      altqueueDeqTime = altqueueDeqTimer.timeit(number=100)
      fasterqueueDeqTime = fasterqueueDeqTimer.timeit(number=100)
      print("%d,%10.3f,%10.3f,%10.3f,%10.3f,%10.3f,%10.3f" % 
            (n, queueEnqTime, queueDeqTime, altqueueEnqTime, altqueueDeqTime,
            fasterqueueEnqTime, fasterqueueDeqTime))

if __name__ == "__main__":
   testEnqueue()
