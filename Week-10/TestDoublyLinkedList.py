import unittest
from random import randint
from DoublyLinkedList import DoublyLinkedList
from DoublyLinkedList import Node

class TestDoublyLinkedList(unittest.TestCase):
    names = ['Bob Belcher',
             'Linda Belcher',
             'Tina Belcher',
             'Gene Belcher',
             'Louise Belcher']

    def test_init(self):
        dll = DoublyLinkedList()
        self.assertIsNotNone(dll.head)
        self.assertIsNotNone(dll.tail)
        self.assertEqual(dll.size(), 0)

    def test_insert_front(self):
        dll = DoublyLinkedList()
        for name in TestDoublyLinkedList.names:
            dll.insert_front(name)

        self.assertEqual(dll.fetch(0), TestDoublyLinkedList.names[4])
        self.assertEqual(dll.fetch(1), TestDoublyLinkedList.names[3])
        self.assertEqual(dll.fetch(2), TestDoublyLinkedList.names[2])
        self.assertEqual(dll.fetch(3), TestDoublyLinkedList.names[1])
        self.assertEqual(dll.fetch(4), TestDoublyLinkedList.names[0])

    def test_insert_last(self):
        dll = DoublyLinkedList()
        for name in TestDoublyLinkedList.names:
            dll.insert_last(name)

        for i in range(len(TestDoublyLinkedList.names) - 1):
            self.assertEqual(dll.fetch(i), TestDoublyLinkedList.names[i])

    def test_insert(self):
        dll = DoublyLinkedList()
        for name in TestDoublyLinkedList.names:
            dll.insert_last(name)

        pos = randint(0, len(TestDoublyLinkedList.names) - 1)

        dll.insert('Teddy', pos)
        self.assertEqual(dll.fetch(pos), 'Teddy')

    def test_remove_first(self):
        dll = DoublyLinkedList()
        for name in TestDoublyLinkedList.names:
            dll.insert_last(name)

        for i in range(dll.size(), 0, -1):
            self.assertEqual(dll.size(), i)
            dll.remove_first()

    def test_remove_last(self):
        dll = DoublyLinkedList()
        for name in TestDoublyLinkedList.names:
            dll.insert_last(name)

        for i in range(dll.size(), 0, -1):
            self.assertEqual(dll.size(), i)
            dll.remove_last()

    def test_remove(self):
        dll = DoublyLinkedList()
        for name in TestDoublyLinkedList.names:
            dll.insert_last(name)

        dll.remove(1)

        self.assertEqual(dll.fetch(0), 'Bob Belcher')
        self.assertEqual(dll.fetch(1), 'Tina Belcher')
        self.assertEqual(dll.fetch(2), 'Gene Belcher')
        self.assertEqual(dll.fetch(3), 'Louise Belcher')


if __name__ == '__main__':
    unittest.main()