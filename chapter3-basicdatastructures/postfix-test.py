import unittest
from postfix import infixToPostfix

class PostfixTest(unittest.TestCase):
   def test_infix_postfix_conversion(self):
      conversions = {}
      conversions['A + B'] = 'A B +'
      conversions['A + B * C + D'] = 'A B C * + D +'
      conversions['( A + B ) * C - ( D - E ) * ( F + G )'] = \
         'A B + C * D E - F G + * -'
      for conversion in conversions.keys():
         self.assertEqual(infixToPostfix(conversion), conversions[conversion])

if __name__ == '__main__':
   unittest.main()
