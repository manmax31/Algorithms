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

    def delete_node(self, n):
        if n is None or n.next is None:
            return False
        next = n.next
        n.data = next.data
        n.next = next.next
        next = None
        return True

if __name__ == "__main__":
    ll = SinglyLinkedList()
    ll.append("F")
    ll.append("O")
    ll.append("L")
    ll.append("L")
    ll.append("O")
    ll.append("W")
    ll.append("G")
    ll.append("U")
    ll.append("P")
    ll.display()








