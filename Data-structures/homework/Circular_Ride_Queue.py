# Circular Ride Queue (Circular Queue)
# Scenario:
# A circular queue manages a ride at an amusement park. When the ride is full, the first person boards and leaves the queue, making space for the next.
#
# Task:
#
# Implement a RideQueue class using a circular queue.
# Create methods to:
# Add a person to the queue (enqueue(name)).
# Board a person (dequeue()).
# Display the queue (show_queue()).

class RideQueue:
    def __init__(self, capacity):
        self.queue = [None] * capacity
        self.capacity = capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def is_full(self):
        if self.size == self.capacity:
            return True
        else:
            return False

    def enqueue(self, name):
        if self.is_full():
            print("Cannot add more people, queue is full.")
        else:
            self.rear = (self.rear + 1)%self.capacity
            self.queue[self.rear] = name
            self.size += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty, cannot dequeue.")
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1)%self.capacity
            self.size -= 1
            print("Dequeued :", temp)

    def show_queue(self):
        if self.is_empty():
            print("Cannot display queue, it is empty.")
        else:
            queue = []
            for i in range(self.size):
                index = (self.front + i)%self.capacity
                queue.append(self.queue[index])
            print("Current Queue : ", queue)

# Testing
if __name__ == "__main__":
    rq = RideQueue(3)
    rq.enqueue("Anna")
    rq.enqueue("Elsa")
    rq.enqueue("Olaf")
    rq.show_queue()
    rq.dequeue()
    rq.enqueue("Kristoff")
    rq.show_queue()

# Queue: ['Anna', 'Elsa', 'Olaf']
# Dequeued: Anna
# Queue: ['Kristoff', 'Elsa', 'Olaf']
