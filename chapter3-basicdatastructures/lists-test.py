import unittest
import pdb
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

    def test_index(self):
        mylist = UnorderedList()
        mylist.append(1)
        mylist.append(2)

        self.assertEqual(mylist.index(1), 1)
        self.assertEqual(mylist.index(2), 2)

    def test_insert(self):
        mylist = UnorderedList()
        mylist.insert(1, 0)
        mylist.insert(3, 1)
        mylist.insert(2, 1)

        self.assertEqual(mylist.index(1), 1)
        self.assertEqual(mylist.index(2), 2)
        self.assertEqual(mylist.index(3), 3)


if __name__ == '__main__':
   unittest.main()
