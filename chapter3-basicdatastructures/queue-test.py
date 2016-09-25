import unittest
from queue import Queue, QueueAlt

class QueueTest(unittest.TestCase):
   def setUp(self):
      self.myqueue = Queue()

   def tearDown(self):
      del(self.myqueue)

   def test_create_empty_queue(self):
      self.assertEqual(self.myqueue.isEmpty(), True)

   def test_enqueue_element(self):
      self.myqueue.enqueue(1)
      self.assertEqual(self.myqueue.items[0], 1)

   def test_dequeue_element(self):
      self.myqueue.items.append(1)
      self.assertEqual(self.myqueue.dequeue(), 1)

   def test_ordering_enqueue_dequeue(self):
      self.myqueue.enqueue(1)
      self.myqueue.enqueue(2)
      self.assertEqual(self.myqueue.dequeue(), 1)
      self.assertEqual(self.myqueue.dequeue(), 2)

   def test_queue_size(self):
      self.myqueue.enqueue(1)
      self.myqueue.enqueue(2)
      self.myqueue.enqueue(3)
      self.assertEqual(self.myqueue.size(), 3)

class QueueAltTest(unittest.TestCase):
   def setUp(self):
      self.myqueue = QueueAlt()

   def tearDown(self):
      del(self.myqueue)

   def test_create_empty_queue(self):
      self.assertEqual(self.myqueue.isEmpty(), True)

   def test_enqueue_element(self):
      self.myqueue.enqueue(1)
      self.assertEqual(self.myqueue.items[0], 1)

   def test_dequeue_element(self):
      self.myqueue.items.append(1)
      self.assertEqual(self.myqueue.dequeue(), 1)

   def test_ordering_enqueue_dequeue(self):
      self.myqueue.enqueue(1)
      self.myqueue.enqueue(2)
      self.assertEqual(self.myqueue.dequeue(), 1)
      self.assertEqual(self.myqueue.dequeue(), 2)

   def test_queue_size(self):
      self.myqueue.enqueue(1)
      self.myqueue.enqueue(2)
      self.myqueue.enqueue(3)
      self.assertEqual(self.myqueue.size(), 3)

if __name__ == "__main__":
   unittest.main()
