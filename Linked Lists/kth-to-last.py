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

    def remove_duplicates_without_buffer(self, k):
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

    def find_kth_from_last(self, k):
        """
        Time Complexity: O(n)
        Såpace complexity: O(1)
        :return:
        """
        p1 = self.head
        p2 = self.head
        for i in range(0, k):
            if p1 is None:
                return None
            p1 = p1.next
        while p1.next:
            p1 = p1.next
            p2 = p2.next
        return p2.data


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
    print(ll.find_kth_from_last(3))







