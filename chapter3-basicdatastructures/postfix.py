from stack import Stack

def infixToPostfix(infixString):
   opstack = Stack()
   infix = infixString.split()

   postfix = []

   operators = {}
   operators["+"] = 1
   operators["-"] = 1
   operators["*"] = 2
   operators["/"] = 2

   for token in infix:
      if token == '(':
         opstack.push(token)
      elif token == ')':
         backtoken = opstack.pop()
         while backtoken != '(':
            postfix.append(backtoken)
            backtoken = opstack.pop()
      elif token in operators.keys():
         while not opstack.isEmpty() and \
               operators.get(opstack.peek(), False) and \
               operators.get(token, False) and \
               operators[opstack.peek()] >= operators[token]:
            postfix.append(opstack.pop())
         opstack.push(token)
      else:
         postfix.append(token)

   while not opstack.isEmpty():
      postfix.append(opstack.pop())

   return " ".join(postfix)

def evaluatePostfix(postfixString):
   opstack = Stack()
   postfix = postfixString.split()
   operators = ["+", "-", "/", "*"]

   for token in postfix:
      if token in operators:
         op2 = opstack.pop()
         op1 = opstack.pop()
         if token == "+":
            opstack.push(op1 + op2)
         elif token == "-":
            opstack.push(op1 - op2)
         elif token == "/":
            opstack.push(op1 / op2)
         elif token == "*":
            opstack.push(op1 * op2)
      else:
         opstack.push(int(token))

   return opstack.pop()
