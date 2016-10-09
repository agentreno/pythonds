import timeit

def enqueueNItems(queue, n):
   for i in range(n):
      queue.enqueue(i)

def dequeueNItems(queue, n):
   for _ in range(n):
      queue.dequeue()

def testEnqueue():
   print("==Analysis of enqueue complexity==")
   queueEnqTimer = timeit.Timer("enqueueNItems(myqueue, n)",
      "from __main__ import enqueueNItems, n; "
      "from queue import Queue; myqueue = Queue()"
   )
   altqueueEnqTimer = timeit.Timer("enqueueNItems(myqueue, n)",
      "from __main__ import enqueueNItems, n; "
      "from queue import QueueAlt; myqueue = QueueAlt()"
   )
   queueDeqTimer = timeit.Timer("dequeueNItems(myqueue, n)",
      "from __main__ import enqueueNItems, dequeueNItems, n; "
      "from queue import Queue; myqueue = Queue(); "
      "enqueueNItems(myqueue, 700000)"
   )
   altqueueDeqTimer = timeit.Timer("dequeueNItems(myqueue, n)",
      "from __main__ import enqueueNItems, dequeueNItems, n; "
      "from queue import QueueAlt; myqueue = QueueAlt(); "
      "enqueueNItems(myqueue, 700000)"
   )
   print("n      Queue-enq     Queue-deq    QueueAlt-enq     QueueAlt-deq")
   print("===============================================================")
   global n
   for n in range(10,101,10):
      queueEnqTime = queueEnqTimer.timeit(number=1000)
      altqueueEnqTime = altqueueEnqTimer.timeit(number=1000)
      queueDeqTime = queueDeqTimer.timeit(number=1000)
      altqueueDeqTime = altqueueDeqTimer.timeit(number=1000)
      print("%d,%10.3f,%10.3f,%10.3f,%10.3f" % 
            (n, queueEnqTime, queueDeqTime, altqueueEnqTime, altqueueDeqTime))

if __name__ == "__main__":
   testEnqueue()
