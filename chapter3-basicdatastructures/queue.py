class Queue:
   def __init__(self):
      self.items = []

   def isEmpty(self):
      return len(self.items) == 0

   def enqueue(self, item):
      self.items.insert(0, item)

   def dequeue(self):
      return self.items.pop()

   def size(self):
      return len(self.items)

# An alternative Queue implementation with the front at the rear of a Python list
class QueueAlt:
   def __init__(self):
      self.items = []

   def isEmpty(self):
      return len(self.items) == 0

   def enqueue(self, item):
      self.items.append(item)

   def dequeue(self):
      return self.items.pop(0)

   def size(self):
      return len(self.items)
