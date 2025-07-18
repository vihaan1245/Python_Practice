class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * capacity
        self.front = 0  # increase when dequeue happens
        self.rear = -1  # increase when enqueue happens
        self.size = 0

    def is_empty(self):
        if self.size == 0:
            print("Queue is empty")
            return True
        else:
            return False

    def is_full(self):
        if self.size == self.capacity:
            print("The queue is full")
            return True
        else:
            return False

    def enqueue(self, element):
        if self.is_full():
            return
        else:
            self.rear = (self.rear + 1)%self.capacity
            self.data[self.rear] = element
            self.size += 1

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            temp = self.data[self.front]
            self.front = (self.front + 1)%self.capacity
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
            for i in range(self.capacity):
                print(self.data[i])

movie_line = CircularQueue(5)
movie_line.enqueue("Suhaan")
movie_line.enqueue("Marc")
movie_line.enqueue("Kaivito")
movie_line.enqueue("Soham")
movie_line.enqueue("Mathew")
movie_line.dequeue()
movie_line.enqueue("Mathewelanel")
movie_line.display()
