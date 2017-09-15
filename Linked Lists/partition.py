# Implement an algorithm to find the kth from last element of a singly linked list.


class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class SinglyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def display(self):
        runner = self.head
        while runner is not None:
            print(runner.data, end='')
            print('->', end='')
            runner = runner.next
        print(None)

    def append(self, data):
        new_node = Node(data, None)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data, None)
        new_node.next = self.head.next
        self.head = new_node

    def partition(self, val):
        before_start = None
        before_end = None
        after_start = None
        after_end = None

        node = self.head
        while node:
            next_ = node.next
            if node.data < val:
                if before_start is None:
                    before_start = node
                    before_end = before_start
                else:
                    # Add to end of before list
                    before_end.next = node
                    before_end = node
                    before_end.next = None
            else:
                if after_start is None:
                    after_start = node
                    after_end = after_start
                else:
                    after_end.next = node
                    after_end = node
                    after_end.next = None
            node = next_

        # if before_start is None:
        #     return after_start

        # Merge
        before_end.next = after_start
        self.head = before_start


if __name__ == "__main__":
    ll = SinglyLinkedList()
    ll.append(3)
    ll.append(5)
    ll.append(8)
    ll.append(5)
    ll.append(10)
    ll.append(2)
    ll.append(1)
    ll.append(1)
    ll.display()
    ll.partition(5)
    ll.display()









