class Stack:
   def __init__(self):
      self.items = []
   
   def isEmpty(self):
      return self.items == []

   def push(self, item):
      self.items.append(item)

   def pop(self):
      return self.items.pop()

   def peek(self):
      return self.items[-1:][0]

   def size(self):
      return len(self.items)

def revstring(string):
   charStack = Stack()
   for letter in string:
      charStack.push(letter)

   reversedString = ""
   while charStack.isEmpty() == False:
      reversedString += charStack.pop()

   return reversedString
