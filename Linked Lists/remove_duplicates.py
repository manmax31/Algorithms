# Remove Duplicates: Write code to remove duplicates from an unsorted linked list.


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

    def remove(self, node_value):
        prev = Node(None, None)
        runner = self.head
        while runner is not None:
            if runner.data == node_value:
                if prev is not None:
                    prev.next = runner.next
                else:
                    self.head = runner.next
                break
            else:
                prev = runner
                runner = runner.next
        if runner.next is None:
            self.tail = runner
        if self.head is None:
            self.tail = None

    def remove_duplicates(self):
        """
        O(n) time
        :return:
        """
        runner = self.head
        hash_set = set()
        previous = Node(None, None)
        while runner is not None:
            if runner.data in hash_set:
                previous.next = runner.next
            else:
                hash_set.add(runner.data)
                previous = runner
            runner = runner.next

    def remove_duplicates_without_buffer(self):
        """
        O(n^2)
        :return:
        """
        current =self.head
        while current is not None:
            runner = current
            while runner.next is not None:
                if runner.next.data == current.data:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            current = current.next

if __name__ == "__main__":
    ll = SinglyLinkedList()
    ll.append('M')
    ll.append('A')
    ll.append('N')
    ll.append('A')
    ll.append('B')
    ll.prepend('R')
    ll.display()
    ll.remove_duplicates()
    ll.display()

    ll = SinglyLinkedList()
    ll.append('M')
    ll.append('A')
    ll.append('N')
    ll.append('A')
    ll.append('B')
    ll.prepend('R')
    ll.display()
    ll.remove_duplicates_without_buffer()
    ll.display()








