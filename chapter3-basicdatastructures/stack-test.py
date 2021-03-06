import unittest
from stack import Stack, revstring, parenthesesChecker, intToBinaryStringDivideBy2

class StackTest(unittest.TestCase):
   def setUp(self):
      self.mystack = Stack()

   def tearDown(self):
      del(self.mystack)

   def test_create_empty_stack(self):
      self.assertEqual(self.mystack.isEmpty(), True)

   def test_push_element_and_peek_stack(self):
      self.mystack.push(1)
      self.assertEqual(self.mystack.peek(), 1)

   def test_push_and_pop_element_to_stack(self):
      self.mystack.push(1)
      self.assertEqual(self.mystack.isEmpty(), False)
      self.assertEqual(self.mystack.pop(), 1)
      self.assertEqual(self.mystack.isEmpty(), True)

   def test_size_of_stack(self):
      self.mystack.push(1)
      self.mystack.push(2)
      self.mystack.push(3)
      self.assertEqual(self.mystack.size(), 3)

   def test_string_reversal(self):
      testString = "abc"
      reversedString = revstring(testString)
      self.assertEqual(reversedString, "cba")

   def test_parentheses_checker(self):
      unbalancedOpens = "(()"
      unbalancedClose = "())"
      balanced = "(())"

      self.assertEqual(parenthesesChecker(unbalancedOpens), False)
      self.assertEqual(parenthesesChecker(unbalancedClose), False)
      self.assertEqual(parenthesesChecker(balanced), True)

   def test_binary_string(self):
      self.assertEqual(intToBinaryStringDivideBy2(0), '0')
      self.assertEqual(intToBinaryStringDivideBy2(1), '1')
      self.assertEqual(intToBinaryStringDivideBy2(2), '10')
      self.assertEqual(intToBinaryStringDivideBy2(3), '11')
      self.assertEqual(intToBinaryStringDivideBy2(1024), '10000000000')

if __name__ == '__main__':
   unittest.main()
