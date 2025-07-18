# Undo Feature in Text Editor (Doubly Linked List)
# Scenario:
# A text editor tracks user operations to implement an undo feature. Each operation (insert, delete, etc.) is recorded, and users can undo actions in the reverse order.
#
# Task:
#
# Implement a TextEditor class using a doubly linked list.
# Create methods to:
# Record operations (record_operation(operation)).
# Undo the last operation (undo()).
# Display the operation history (display_operations()).

class Node:
    def __init__(self, operation):
        self.operation = operation
        self.next = None
        self.prev = None

class TextEditor:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def record_operation(self, operation):
        new_operation = Node(operation)
        if self.is_empty():
            self.head = new_operation
            self.tail = self.head
        else:
            new_operation.prev = self.tail
            self.tail.next = new_operation
            self.tail = new_operation
        self.length += 1
        # Record a new operation
        pass

    def undo(self):
        if self.is_empty():
            print("Nothing to delete")
        elif self.head == self.tail:
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1

    def display_operations(self):
        if self.is_empty():
            print("Cannot display.")
        else:
            temp = self.head
            while temp:
                print(f"{temp.operation}", end=" -> ")
                temp = temp.next

skibidi = TextEditor()
skibidi.record_operation("Delete")
skibidi.record_operation("Add")
skibidi.record_operation("Duplicate")
skibidi.display_operations()
skibidi.undo()
print()
skibidi.display_operations()
