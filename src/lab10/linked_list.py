class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __repr__(self):
        return f"Node({self.value})"

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1
    
    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        if self.tail is None:
            self.tail = new_node
        self._size += 1
    
    def insert(self, idx, value):
        if idx < 0 or idx > self._size:
            raise IndexError(f"Index {idx} out of bounds")
        
        if idx == 0:
            self.prepend(value)
            return
        if idx == self._size:
            self.append(value)
            return
        
        new_node = Node(value)
        current = self.head
        for _ in range(idx - 1):
            current = current.next
        new_node.next = current.next
        current.next = new_node
        self._size += 1
    
    def remove(self, value):
        if self.head is None:
            return
        
        if self.head.value == value:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self._size -= 1
            return
        
        current = self.head
        while current.next and current.next.value != value:
            current = current.next
        
        if current.next:
            if current.next == self.tail:
                self.tail = current
            current.next = current.next.next
            self._size -= 1
    
    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next
    
    def __len__(self):
        return self._size
    
    def __repr__(self):
        values = list(self)
        return f"SinglyLinkedList({values})"
    
    def display(self):
        current = self.head
        result = []
        while current:
            result.append(f"[{current.value}]")
            current = current.next
        result.append("None")
        return " -> ".join(result)
