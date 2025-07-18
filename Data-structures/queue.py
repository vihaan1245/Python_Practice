from collections import deque
from ctypes import memmove


class Queue:
    def __init__(self,capacity):
        self.capacity = capacity
        self.data = [None]*capacity
        self.front = 0 #increase when dequeue happens
        self.rear = -1 #increase when enqueue happens
        self.size = 0

    def is_empty(self):
        if self.size == 0:
            print("Queue is empty")
            return True
        else:
            return False

    def is_full(self):
        if self.rear == self.capacity-1:
            print("The queue is full")
            return True
        else:
            return False

    def enqueue(self,element):
        if self.is_full():
            return
        else:
            self.rear += 1
            self.data[self.rear] = element
            self.size += 1

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            temp = self.data[self.front]
            self.front += 1
            self.size -= 1
            return temp

    def peak(self):
        if self.is_empty():
            return None
        else:
            return self.data[self.front]

    def display(self):
        if self.is_empty():
            return None
        else:
            for i in range(self.front, self.rear+1):
                print(self.data[i])

class SuperQueue(Queue):
    def __init__(self, capacity):
        super().__init__(capacity)
        self.delete = []

    def delete_front(self):
        self.delete.append(super().dequeue())

movie_line = SuperQueue(5)
movie_line.enqueue("Suhaan")
movie_line.enqueue("Marc")
movie_line.enqueue("Kaivito")
movie_line.enqueue("Soham")
movie_line.enqueue("Mathew")
movie_line.dequeue()
movie_line.enqueue("Mathewelanel")
movie_line.display()

# 1 2 3 4 5 6



