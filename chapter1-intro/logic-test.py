import unittest
from logic import AndGate, OrGate, NotGate, NandGate, Connector, HalfAdder

class LogicTest(unittest.TestCase):
   def test_distributive_not(self):
      # NOT ( (A AND B) OR (C AND D) )
      g1 = AndGate("g1")
      g2 = AndGate("g2")
      g3 = OrGate("g3")
      g4 = NotGate("g4")
      c1 = Connector(g1, g3)
      c2 = Connector(g2, g3)
      c3 = Connector(g3, g4)
      
      # NOT (A AND B) AND NOT (C AND D)
      g5 = NandGate("g5")
      g6 = NandGate("g6")
      g7 = AndGate("g7")
      c4 = Connector(g5, g7)
      c5 = Connector(g6, g7)

      a = 1
      b = 0
      c = 1
      d = 0

      g1.pinA = a
      g1.pinB = b
      g2.pinA = c
      g2.pinB = d

      g5.pinA = a
      g5.pinB = b
      g6.pinA = c
      g6.pinB = d

      self.assertEqual(g4.performGateLogic(), g7.performGateLogic())

   def test_half_adder(self):
      ha = HalfAdder()

      ha.performLogic(0,0)
      self.assertEqual(ha.outsum, 0)
      self.assertEqual(ha.outcarry, 0)

      ha.performLogic(1,0)
      self.assertEqual(ha.outsum, 1)
      self.assertEqual(ha.outcarry, 0)

      ha.performLogic(1,1)
      self.assertEqual(ha.outsum, 0)
      self.assertEqual(ha.outcarry, 1)

if __name__ == '__main__':
   unittest.main()
