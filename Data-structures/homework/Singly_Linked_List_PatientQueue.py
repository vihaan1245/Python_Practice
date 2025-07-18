# Patient Queue Management System (Singly Linked List)
# Scenario:
# A hospital uses a system to manage patient check-ins. Patients are added to the queue based on their arrival time. However, if a patient has a high-priority condition (like an emergency), they need to be added to the front of the queue.
#
# Task:
#
# Implement a PatientQueue class using a singly linked list.
# Create methods to:
# Add a patient (add_patient(name)) at the end of the list.
# Add an emergency patient (add_emergency_patient(name)) at the front.
# Remove a patient after they are treated (remove_patient()).
# Display the current queue (display_queue()).


class Node:
    def __init__(self, name):
        self.name = name
        self.next = None

class PatientQueue:
    def __init__(self):
        self.head = None
        self.length = 0

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def add_patient(self, name):
        new_patient = Node(name)
        if self.is_empty():
            self.head = new_patient
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_patient
        self.length += 1

    def add_emergency_patient(self, name):
        er_patient = Node(name)
        er_patient.next = self.head
        self.head = er_patient
        self.length += 1

    def remove_patient(self,name):
        if self.is_empty():
            print("There are no patients to remove or the patient you are trying to remove is not there.")
        else:
            temp = self.head
            if temp.name == name:
                self.head = self.head.next
                self.length -= 1
                return
            else:
                while temp.next.name != name:
                    temp = temp.next
                    if temp.next is not None:
                        temp.next = temp.next.next
                        self.length -= 1
                    else:
                        print("Value not found")

    def display_queue(self):
        if self.is_empty():
            print("The queue is empty, your free to go for today!")
        else:
            temp = self.head
            for _ in range(self.length):
                print(f"Patient : {temp.name}\n")
                temp = temp.next

john = PatientQueue()
john.add_patient("Ron")
john.add_patient("John")
john.add_emergency_patient("Rishit")
john.add_emergency_patient("Vihaan")
john.remove_patient("John")
john.display_queue()