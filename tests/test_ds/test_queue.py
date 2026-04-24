import unittest
from DataStructures import Queue

class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_create_and_empty(self):
        self.assertIsNotNone(self.queue)
        self.assertTrue(self.queue.IsEmpty())

    def test_enqueue_and_dequeue(self):
        self.queue.Enqueue(100)
        self.queue.Enqueue(200)
        self.assertFalse(self.queue.IsEmpty())

        self.assertEqual(self.queue.Dequeue(), 100)
        self.assertEqual(self.queue.Dequeue(), 200)

        self.assertTrue(self.queue.IsEmpty())

    def test_dequeue_empty(self):
        val = self.queue.Dequeue()
        self.assertEqual(val, float("-inf"))

    def test_display(self):
        self.queue.Enqueue(55)
        self.queue.Display()

    def test_fifo_order(self):
        for v in [1, 2, 3, 4]:
            self.queue.Enqueue(v)
        self.assertEqual(self.queue.Dequeue(), 1)
        self.assertEqual(self.queue.Dequeue(), 2)
        self.assertEqual(self.queue.Dequeue(), 3)
        self.assertEqual(self.queue.Dequeue(), 4)
        self.assertTrue(self.queue.IsEmpty())

    def test_dequeue_until_empty(self):
        self.queue.Enqueue(7)
        self.queue.Dequeue()
        self.assertEqual(self.queue.Dequeue(), float("-inf"))

    def test_display_empty(self):
        self.queue.Display()

    def test_negative_and_zero(self):
        self.queue.Enqueue(-10)
        self.queue.Enqueue(0)
        self.queue.Enqueue(-1)
        self.assertEqual(self.queue.Dequeue(), -10)
        self.assertEqual(self.queue.Dequeue(), 0)

    def test_interleaved_enqueue_dequeue(self):
        self.queue.Enqueue(1)
        self.queue.Enqueue(2)
        self.assertEqual(self.queue.Dequeue(), 1)
        self.queue.Enqueue(3)
        self.assertEqual(self.queue.Dequeue(), 2)
        self.assertEqual(self.queue.Dequeue(), 3)
        self.assertTrue(self.queue.IsEmpty())

    def test_large_input(self):
        for i in range(1, 101):
            self.queue.Enqueue(i)
        self.assertEqual(self.queue.Dequeue(), 1)
