import timeit

# Creating a list of consecutive integers using concatenation
def createIntListConcat():
   l = []
   for i in range(1000):
      l = l + [i]
   return l

# Creating a list of consecutive integers using append
def createIntListAppend():
   l = []
   for i in range(1000):
      l.append(i)
   return l

# Creating a list of consecutive integers using a comprehension
def createIntListComprehension():
   return [i for i in range(1000)]

# Creating a list of consecutive integers using range
def createIntListRange():
   return list(range(1000)) 

if __name__ == "__main__":
   t1 = timeit.Timer("createIntListConcat()", "from __main__ import createIntListConcat")
   print("concat ", t1.timeit(number=1000), "milliseconds")
   t2 = timeit.Timer("createIntListAppend()", "from __main__ import createIntListAppend")
   print("append ", t2.timeit(number=1000), "milliseconds")
   t3 = timeit.Timer("createIntListComprehension()", "from __main__ import createIntListComprehension")
   print("comprehension ", t3.timeit(number=1000), "milliseconds")
   t4 = timeit.Timer("createIntListRange()", "from __main__ import createIntListRange")
   print("range ", t4.timeit(number=1000), "milliseconds")

   popzero = timeit.Timer("x.pop(0)", "from __main__ import x")
   popend = timeit.Timer("x.pop()", "from __main__ import x")
   print("pop(0)   pop()")
   for i in range(1000000,100000001,1000000):
      x = list(range(i))
      pt = popend.timeit(number=1000)
      x = list(range(i))
      pz = popzero.timeit(number=1000)
      print("%15.5f, %15.5f" % (pz, pt))