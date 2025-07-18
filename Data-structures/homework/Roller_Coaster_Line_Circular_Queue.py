# Roller Coaster Line (Circular Queue)
# Scenario:
# A roller coaster line allows riders to queue. If the ride is full, the system prevents further entries. Riders are boarded in a circular manner, and new riders take their place as space becomes available.
#
# Task:
#
# Implement a RollerCoasterLine class using a circular queue.
# Create methods to:
# Join the ride queue (join(name)).
# Board the ride (board()).
# Display the current queue (show_queue()).
class RollerCoasterLine:
    def __init__(self,capacity):
        self.capacity = capacity
        self.data = [None] * capacity
        self.size = 0
        self.front = 0
        self.rear = -1

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

    def join(self, name):
        if self.is_full():
            print("Queue is full cannot join.")
        else:
            self.rear = (self.rear + 1)%self.capacity
            self.data[self.rear] = name
            self.size += 1

    def board(self):
        if self.is_empty():
            print("Cannot board.")
        else:
            temp = self.data[self.front]
            self.data[self.front] = None
            self.front = (self.front + 1)%self.capacity
            self.size -= 1
            print(f"Boarded : {temp}")
        pass

    def show_queue(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            queue = []
            for i in range(self.size):
                index = (self.front + i)%self.capacity
                queue.append(self.data[index])
            print("Current queue:", queue)


# Testing
if __name__ == "__main__":
    line = RollerCoasterLine(3)
    line.join("Anna")
    line.join("Elsa")
    line.show_queue()
    line.board()
    line.join("Kristoff")
    line.show_queue()

# Queue: ['Anna', 'Elsa', None]
# Boarded: Anna
# Queue: [None, 'Elsa', 'Kristoff']
