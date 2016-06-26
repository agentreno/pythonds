class LogicGate:

   def __init__(self, n):
      self.label = n
      self.output = None

   def getLabel(self):
      return self.label

   def getOutput(self):
      self.output = self.performGateLogic()
      return self.output

class BinaryGate(LogicGate):

   def __init__(self, n):
      LogicGate.__init__(self, n)

      self.pinA = None
      self.pinB = None

   def getPinA(self):
      if self.pinA == None:
         return int(input("Enter Pin A input for gate " + self.getLabel() + "-->"))
      elif isinstance(self.pinA, Connector):
         return self.pinA.getFrom().getOutput()
      else:
         return self.pinA

   def getPinB(self):
      if self.pinB == None:
         return int(input("Enter Pin B input for gate " + self.getLabel() + "-->"))
      elif isinstance(self.pinB, Connector):
         return self.pinB.getFrom().getOutput()
      else:
         return self.pinB

   def setNextPin(self, source):
      if self.pinA == None:
         self.pinA = source
      elif self.pinB == None:
         self.pinB = source
      else:
         raise RuntimeError("Error: no empty pins")


class UnaryGate(LogicGate):

   def __init__(self, n):
      LogicGate.__init__(self, n)

      self.pin = None

   def getPin(self):
      if self.pin == None:
         return int(input("Enter Pin input for gate " + self.getLabel() + "-->"))
      else:
         return self.pin.getFrom().getOutput()

   def setNextPin(self, source):
      if self.pin == None:
         self.pin = source
      else:
         raise RuntimeError("Error: no empty pins")

class AndGate(BinaryGate):

   def __init__(self, n):
      BinaryGate.__init__(self, n)

   def performGateLogic(self):
      a = self.getPinA()
      b = self.getPinB()
      if a == 1 and b == 1:
         return 1
      else:
         return 0

class OrGate(BinaryGate):

   def __init__(self, n):
      BinaryGate.__init__(self, n)

   def performGateLogic(self):
      a = self.getPinA()
      b = self.getPinB()
      if a == 1 or b == 1:
         return 1
      else:
         return 0

class NotGate(UnaryGate):

   def __init__(self, n):
      UnaryGate.__init__(self, n)

   def performGateLogic(self):
      pin = self.getPin()
      if pin == 1:
         return 0
      else:
         return 1

class NandGate(AndGate):

   def __init__(self, n):
      AndGate.__init__(self, n)

   def performGateLogic(self):
      if super().performGateLogic() == 1:
         return 0
      else:
         return 1

class NorGate(OrGate):

   def __init__(self, n):
      OrGate.__init__(self, n)

   def performGateLogic(self):
      if super().performGateLogic() == 1:
         return 0
      else:
         return 1

class XorGate(BinaryGate):

   def __init__(self, n):
      BinaryGate.__init__(self, n)

   def performGateLogic(self):
      a = self.getPinA()
      b = self.getPinB()
      if a == b:
          return 0
      else:
          return 1

class Connector:

   def __init__(self, fgate, tgate):
      self.fromgate = fgate
      self.togate = tgate

      tgate.setNextPin(self)

   def getFrom(self):
      return self.fromgate

   def getTo(self):
      return self.togate

class HalfAdder:

    def __init__(self):
        self.pinA = None
        self.pinB = None
        self.outsum = None
        self.outcarry = None

        self.xorgate = XorGate("xorgate")
        self.andgate = AndGate("andgate")

    def performLogic(self, a, b):
        self.xorgate.pinA = a
        self.xorgate.pinB = b
        self.andgate.pinA = a
        self.andgate.pinB = b

        self.outsum = self.xorgate.performGateLogic()
        self.outcarry = self.andgate.performGateLogic()


# TODO: Extend it to be a full adder
