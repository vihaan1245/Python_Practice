#Exercise 1
# import threading
# import time
#
#
# class Queue:
#     def __init__(self,capacity):
#         self.capacity = capacity
#         self.data = [None]*capacity
#         self.front = 0 #increase when dequeue happens
#         self.rear = -1 #increase when enqueue happens
#         self.size = 0
#
#     def is_empty(self):
#         if self.size == 0:
#             print("Queue is empty")
#             return True
#         else:
#             return False
#
#     def is_full(self):
#         if self.rear == self.capacity-1:
#             print("The queue is full")
#             return True
#         else:
#             return False
#
#     def enqueue(self,element):
#         if self.is_full():
#             return
#         else:
#             self.rear += 1
#             self.data[self.rear] = element
#             self.size += 1
#
#     def dequeue(self):
#         if self.is_empty():
#             return None
#         else:
#             temp = self.data[self.front]
#             self.front += 1
#             self.size -= 1
#             return temp
#
#     def peak(self):
#         if self.is_empty():
#             return None
#         else:
#             return self.data[self.front]
#
#     def display(self):
#         if self.is_empty():
#             return None
#         else:
#             for i in range(self.front, self.rear+1):
#                 print(self.data[i])
#
# food_order_queue = Queue(25)
#
# def place_order(order:list):
#     for index,item in enumerate(order):
#         print("Placing order for :",item)
#         food_order_queue.enqueue(item)
#         time.sleep(1)
#
# def serve_order():
#     time.sleep(3)
#     while food_order_queue.is_empty() is not True:
#         order = food_order_queue.dequeue()
#         if order is not None:
#             print("Now serving order:", order)
#             time.sleep(2)
#
# if __name__ == "__main__":
#     orders = ["pizza","pasta","biryani","burger and fries","milkshake","noodles"]
#     t1 = threading.Thread(target=place_order, args=(orders,))
#     t2 = threading.Thread(target=serve_order)
#     t1.start()
#     t2.start()

#Exercise 2
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

def produce_binary_numbers(n):
    binary_queue = Queue(25)
    binary_queue.enqueue(1)
    for i in range(n):
        front_item = binary_queue.peak()
        print("", front_item)
        binary_queue.enqueue(str(front_item)+"0")
        binary_queue.enqueue(str(front_item)+"1")
        binary_queue.dequeue()

if __name__ == "__main__":
    produce_binary_numbers(10)

