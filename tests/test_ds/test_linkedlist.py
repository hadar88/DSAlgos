import unittest
from DataStructures import LinkedList

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.ll = LinkedList()

    def test_create_and_empty(self):
        self.assertIsNotNone(self.ll)
        self.assertTrue(self.ll.IsEmpty())
        self.assertEqual(self.ll.Size(), 0)
        self.assertIsNone(self.ll.GetHead())

    def test_insert_and_size(self):
        self.ll.Insert(10)
        self.assertFalse(self.ll.IsEmpty())
        self.assertEqual(self.ll.Size(), 1)

        self.ll.Insert(20)
        self.assertEqual(self.ll.Size(), 2)

        head = self.ll.GetHead()
        self.assertIsNotNone(head)
        self.assertEqual(head.GetData(), 20)
        self.assertEqual(head.GetNext().GetData(), 10)

    def test_insert_last(self):
        self.ll.InsertLast(100)
        self.ll.InsertLast(200)
        self.assertEqual(self.ll.Size(), 2)

        head = self.ll.GetHead()
        self.assertEqual(head.GetData(), 100)
        self.assertEqual(head.GetNext().GetData(), 200)

    def test_delete(self):
        self.ll.Insert(10)
        self.ll.Insert(20)
        self.ll.Insert(30)

        self.ll.Delete(20)
        self.assertEqual(self.ll.Size(), 2)

        head = self.ll.GetHead()
        self.assertEqual(head.GetData(), 30)
        self.assertEqual(head.GetNext().GetData(), 10)

        self.ll.Delete(99)
        self.assertEqual(self.ll.Size(), 2)

    def test_display(self):
        self.ll.Insert(1)
        self.ll.Insert(2)
        self.ll.Display()

    def test_edge_cases(self):
        self.ll.Delete(10)
        self.assertIsNone(self.ll.GetHead())
        self.ll.Display()

    def test_delete_head(self):
        self.ll.Insert(1)
        self.ll.Insert(2)
        self.ll.Delete(2)
        self.assertEqual(self.ll.Size(), 1)
        head = self.ll.GetHead()
        self.assertEqual(head.GetData(), 1)

    def test_delete_tail(self):
        self.ll.InsertLast(10)
        self.ll.InsertLast(20)
        self.ll.Delete(20)
        self.assertEqual(self.ll.Size(), 1)
        head = self.ll.GetHead()
        self.assertEqual(head.GetData(), 10)

    def test_single_element(self):
        self.ll.Insert(42)
        self.assertEqual(self.ll.Size(), 1)
        self.ll.Delete(42)
        self.assertTrue(self.ll.IsEmpty())

    def test_mixed_insert(self):
        self.ll.Insert(2)
        self.ll.InsertLast(3)
        self.ll.Insert(1)
        self.assertEqual(self.ll.Size(), 3)

        head = self.ll.GetHead()
        self.assertEqual(head.GetData(), 1)
        self.assertEqual(head.GetNext().GetData(), 2)
        self.assertEqual(head.GetNext().GetNext().GetData(), 3)

    def test_delete_middle(self):
        self.ll.InsertLast(10)
        self.ll.InsertLast(20)
        self.ll.InsertLast(30)
        self.ll.Delete(20)
        self.assertEqual(self.ll.Size(), 2)
        head = self.ll.GetHead()
        self.assertEqual(head.GetData(), 10)
        self.assertEqual(head.GetNext().GetData(), 30)

    def test_negative_values(self):
        self.ll.Insert(-5)
        self.ll.Insert(-1)
        self.assertEqual(self.ll.Size(), 2)
        head = self.ll.GetHead()
        self.assertEqual(head.GetData(), -1)
