import unittest
from lists import UnorderedList

class UnorderedListTest(unittest.TestCase):
    def test_append(self):
        mylist = UnorderedList()
        mylist.append(1)
        self.assertEqual(mylist.head.getData(), 1)
        self.assertEqual(mylist.tail.getData(), 1)

        mylist.append(2)
        self.assertEqual(mylist.head.getData(), 1)
        self.assertEqual(mylist.tail.getData(), 2)

    def test_pop(self):
        mylist = UnorderedList()
        mylist.append(1)
        mylist.append(2)
        
        self.assertEqual(mylist.pop(), 2)
        self.assertEqual(mylist.pop(), 1)
        self.assertEqual(mylist.pop(), None)


if __name__ == '__main__':
   unittest.main()
