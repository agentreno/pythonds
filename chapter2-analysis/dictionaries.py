import timeit
import random

print("List vs Dict contains")
for i in range(10000,100001,10000):
   t = timeit.Timer("random.randrange(%d) in x" % i,
         "from __main__ import random, x")
   x = list(range(i))
   lst_time = t.timeit(number=1000)
   
   x = { j:None for j in range(i) }
   d_time = t.timeit(number=1000)
   print("%d,%10.3f,%10.3f" % (i, lst_time, d_time))

print("Dict set value")
for i in range(10000,100001,10000):
   t = timeit.Timer("x[0] = 1",
         "from __main__ import x")
   x = { k:None for k in range(i) }
   set_time = t.timeit(number=1000)
   
   print("%d,%10.8f" % (i, set_time))

print("Dict get item")
for i in range(10000,100001,10000):
   t = timeit.Timer("x.get(0)",
         "from __main__ import x")
   x = {k:None for k in range(i)}
   get_time = t.timeit(number=1000)

   print("%d,%10.8f" % (i, get_time))
