class Node:
    def __init__(self, element=None, next_node=None, prev_node=None):
        self.element = element
        self.next = next_node
        self.prev = prev_node

    def __str__(self):
        if self.element:
            return self.element.__str__()
        else:
            return 'Empty Node'

    def __repr__(self):
        return self.__str__()

    def equals(self, toFind):
        return self == toFind


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(element='Head')
        self.tail = Node(element='Tail')

        self.head.next = self.tail
        self.tail.prev = self.head

    def size(self):
        count = 0
        current = self.head.next

        while current is not None and current != self.tail:
            count += 1
            current = current.next

        return count

    def push(self, data):
        node = Node(element=data, next_node=self.head.next, prev_node=self.head)
        self.head.next.prev = node
        self.head.next = node

    def append(self, data):
        node = Node(element=data, next_node=self.tail, prev_node=self.tail.prev)
        self.tail.prev.next = node
        self.tail.prev = node

    def insert(self, data, position):
        if position == 0:
            self.insert_front(data)
        elif position == self.size():
            self.insert_last(data)
        else:
            if 0 < position < self.size():
                current_node = self.head.next
                count = 0
                while count < (position - 1):
                    current_node = current_node.next
                    count += 1

                node = Node(element=data, next_node=current_node.next, prev_node=current_node)
                current_node.next.prev = node
                current_node.next = node
            else:
                raise IndexError

    def pop(self):
        self.head = self.head.next
        self.head.prev = None

    def truncate(self):
        self.tail = self.tail.prev
        self.tail.next = None

    def remove(self, position):
        if position == 0:
            self.remove_first()
        elif position == self.size():
            self.remove_last()
        else:
            if 0 < position < self.size():
                current_node = self.head.next
                current_pos = 0

                while current_pos < position:
                    current_node = current_node.next
                    current_pos += 1

                next = current_node.next
                prev = current_node.prev

                next.prev = prev
                prev.next = next
            else:
                raise IndexError

    def fetch(self, position):
        if 0 <= position < self.size():
            current_node = self.head.next
            current_pos = 0

            while current_pos < position:
                current_node = current_node.next
                current_pos += 1
            return current_node.element

        else:
            raise IndexError

    def find(self, _value):
        if _value is None:
            raise ValueError('Cannot search for a value=None item to a list')

        current = self.head
        found = False
        while current and not found:
            if current.element == _value:
                found = True
            else:
                current = current.next
        return current
