import unittest
from lists import UnorderedList, OrderedList

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


class OrderedListTest(unittest.TestCase):
    def test_add_items(self):
        mylist = OrderedList()
        mylist.add(3)
        mylist.add(2)
        mylist.add(1)

        self.assertEqual(mylist.head.getData(), 1)
        self.assertEqual(mylist.head.getNext().getData(), 2)
        self.assertEqual(mylist.head.getNext().getNext().getData(), 3)

    def test_search_item(self):
        mylist = OrderedList()
        mylist.add(1)
        mylist.add(2)
        mylist.add(3)

        self.assertEqual(mylist.search(3), True)
        self.assertEqual(mylist.search(4), False)

    def test_isempty(self):
        mylist = OrderedList()
        self.assertEqual(mylist.isEmpty(), True)
        
        mylist.add(1)
        self.assertEqual(mylist.isEmpty(), False)

    def test_size(self):
        mylist = OrderedList()
        self.assertEquals(mylist.size(), 0)

        mylist.add(1)
        self.assertEquals(mylist.size(), 1)

        mylist.add(2)
        self.assertEquals(mylist.size(), 2)

    def test_remove(self):
        mylist = OrderedList()
        mylist.add(1)
        mylist.remove(1)
        self.assertEqual(mylist.isEmpty(), True)

    def test_index(self):
        mylist = OrderedList()
        mylist.add(1)
        mylist.add(2)
        mylist.add(3)

        self.assertEqual(mylist.index(3), 3)

    def test_pop(self):
        mylist = OrderedList()
        mylist.add(1)
        mylist.add(2)
        mylist.add(3)

        self.assertEqual(mylist.pop(), 3)
        self.assertEqual(mylist.size(), 2)

if __name__ == '__main__':
   unittest.main()
