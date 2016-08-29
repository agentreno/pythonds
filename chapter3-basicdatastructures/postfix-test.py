import unittest
from postfix import infixToPostfix, evaluatePostfix

class PostfixTest(unittest.TestCase):
   def test_infix_postfix_conversion(self):
      conversions = {}
      conversions['A + B'] = 'A B +'
      conversions['A + B * C + D'] = 'A B C * + D +'
      conversions['( A + B ) * C - ( D - E ) * ( F + G )'] = \
         'A B + C * D E - F G + * -'
      for conversion in conversions.keys():
         self.assertEqual(infixToPostfix(conversion), conversions[conversion])

   def test_postfix_evaluation(self):
      testExpression1 = "4 5 6 * +"
      testExpression2 = "7 8 + 3 2 + /"

      self.assertEqual(evaluatePostfix(testExpression1), 34)
      self.assertEqual(evaluatePostfix(testExpression2), 3)

if __name__ == '__main__':
   unittest.main()
