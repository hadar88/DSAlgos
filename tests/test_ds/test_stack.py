import unittest
from DataStructures import Stack

class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_create_and_empty(self):
        self.assertIsNotNone(self.stack)
        self.assertTrue(self.stack.IsEmpty())

    def test_push_and_pop(self):
        self.stack.Push(10)
        self.stack.Push(20)
        self.assertFalse(self.stack.IsEmpty())

        self.assertEqual(self.stack.Pop(), 20)
        self.assertEqual(self.stack.Pop(), 10)
        
        self.assertTrue(self.stack.IsEmpty())

    def test_pop_empty(self):
        val = self.stack.Pop()
        self.assertEqual(val, -1)

    def test_display(self):
        self.stack.Push(1)
        self.stack.Display()

    def test_pop_order(self):
        for v in [5, 10, 15, 20]:
            self.stack.Push(v)
        self.assertEqual(self.stack.Pop(), 20)
        self.assertEqual(self.stack.Pop(), 15)
        self.assertEqual(self.stack.Pop(), 10)
        self.assertEqual(self.stack.Pop(), 5)
        self.assertTrue(self.stack.IsEmpty())

    def test_pop_until_empty(self):
        self.stack.Push(1)
        self.stack.Push(2)
        self.stack.Pop()
        self.stack.Pop()
        self.assertEqual(self.stack.Pop(), -1)

    def test_display_empty(self):
        self.stack.Display()

    def test_negative_and_zero(self):
        self.stack.Push(0)
        self.stack.Push(-10)
        self.stack.Push(-1)
        self.assertEqual(self.stack.Pop(), -1)
        self.assertEqual(self.stack.Pop(), -10)
        self.assertEqual(self.stack.Pop(), 0)

    def test_interleaved_push_pop(self):
        self.stack.Push(1)
        self.stack.Push(2)
        self.assertEqual(self.stack.Pop(), 2)
        self.stack.Push(3)
        self.assertEqual(self.stack.Pop(), 3)
        self.assertEqual(self.stack.Pop(), 1)
        self.assertTrue(self.stack.IsEmpty())

    def test_large_input(self):
        for i in range(1, 101):
            self.stack.Push(i)
        self.assertFalse(self.stack.IsEmpty())
        self.assertEqual(self.stack.Pop(), 100)
