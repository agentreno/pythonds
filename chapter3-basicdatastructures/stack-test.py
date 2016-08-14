import unittest
from stack import Stack, revstring

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

if __name__ == '__main__':
   unittest.main()
