from audioop import reverse


class Node:
    def __init__(self,data:int):
        self.data = data
        self.next = None
        self.previous = None

obj_1 = Node(10)
obj_2 = Node(20)
obj_3 = Node(30)

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
        self.tail = self.head

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def append(self,data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = self.head
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self,data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = self.head
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
        self.length += 1

    def insert_at_index(self,data,index:int):
        new_node = Node(data)
        if index < 0 or index > self.length:
            print("Index unavailable")
            return False
        elif index == 0:
            self.prepend(data)
        elif index == self.length:
            self.append(data)
        else:
            temp = self.head
            for i in range(index-1):
                temp = temp.next
            new_node.previous = temp
            new_node.next = temp.next
            temp.next = new_node
            new_node.next.previous = new_node
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

    def display_reverse(self):
        #reverse the display
        if self.is_empty():
            print("Nothing is there to print")
        else:
            temp = self.tail
            while temp:
                print(temp.data,end="")
                if temp.previous:
                    print("->",end="")
                temp = temp.previous
            print()

    def reverse_util(self,current):
        if current is None:
            return None

        temp = current.previous
        current.previous = current.next
        current.next = temp

        if current.previous is None:
            return current

        return self.reverse_util(current.previous)

    def reverse(self):
        self.head = self.reverse_util(self.head)


    def delete(self,data):
        if self.is_empty():
            print("Nothing to delete")
        else:
            temp = self.head
            if temp.data == data:
                self.head = self.head.next
                if self.head is None or self.head.next is None:
                    self.tail = self.head
                if self.head is not None:
                    self.head.previous = None
                self.length -= 1
                return
            else:
                try:
                    while temp.next and temp.next.data != data:
                        temp = temp.next
                    if temp is not None:
                        temp.next = temp.next.next
                        if temp.next is not None:
                            temp.next.previous = temp
                        else:
                            self.tail = temp
                        self.length -= 1
                        return
                except:
                    print("Value not found")



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


linked_list = DoublyLinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(40)
linked_list.delete(30)
linked_list.prepend(90)
# linked_list.display_reverse()
linked_list.display()
linked_list.reverse()
linked_list.display()



