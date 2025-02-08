from node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> " if current.next else "")
            current = current.next
        print()  

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def insertion_sort(self):
        if not self.head or not self.head.next:
            return
        sorted_list = None
        current = self.head
        while current:
            next_node = current.next
            if not sorted_list or sorted_list.data >= current.data:
                current.next = sorted_list
                sorted_list = current
            else:
                sorted_node = sorted_list
                while sorted_node.next and sorted_node.next.data < current.data:
                    sorted_node = sorted_node.next
                current.next = sorted_node.next
                sorted_node.next = current
            current = next_node
        self.head = sorted_list

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def from_list(self, values):
        for value in values:
            self.append(value)

def merge_and_sort_lists(list1, list2):
    merged_list = LinkedList()
    merged_list.from_list(list1.to_list() + list2.to_list())
    merged_list.insertion_sort()
    return merged_list
