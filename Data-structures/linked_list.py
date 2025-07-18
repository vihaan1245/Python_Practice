class Node:
    def __init__(self,data:int):
        self.data = data
        self.next = None

obj_1 = Node(10)
obj_2 = Node(20)
obj_3 = Node(30)

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def append(self,data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
        self.length += 1

    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def insert_at_index(self,data,index:int):
        new_node = Node(data)
        if index < 0 or index > self.length:
            print("Index unavailable")
            return False
        elif index == 0:
            self.prepend(data)
        else:
            temp = self.head
            for i in range(index-1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1

    def display(self):
        if self.is_empty():
            print("Nothing is there to print")
        else:
            temp = self.head
            for i in range(self.length):
                print(temp.data,end="")
                if i < self.length - 1:
                    print("->",end="")
                temp = temp.next
            print()

    def delete(self,data):
        if self.is_empty():
            print("Nothing to delete")
        else:
            temp = self.head
            if temp.data == data:
                self.head = self.head.next
                self.length -= 1
                return
            else:
                while temp.next and temp.next.data != data:
                    temp = temp.next
                if temp.next is not None:
                    temp.next = temp.next.next
                    self.length -= 1
                else:
                    print("Value not found")

    def reverse_util(self,current):
        if current is None or current.next is None:
            return current

        temp = self.reverse_util(current.next)
        current.next.next = current
        current.next = None

        return temp

    def reverse(self):
        self.head = self.reverse_util(self.head)


    def search(self,data):
        if self.is_empty():
            print("Nothing to search")
        if data == self.head.data:
            print(self.head.data)

        temp = self.head
        while temp.next:
            if temp.data == data:
                print("Found the result:",data)
                return data
            temp = temp.next

        print("Not found")

list1 = LinkedList()
list1.append(10)
list1.append(20)
list1.append(30)
list1.insert_at_index(90,1)
list1.prepend(24)
list1.delete(90)
list1.search(10)
list1.display()
list1.reverse()
list1.display()
