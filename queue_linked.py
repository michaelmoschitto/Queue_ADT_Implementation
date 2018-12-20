
class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

class Queue:
    '''Implements an link-based ,efficient first-in first-out Abstract Data Type'''

    def __init__(self, capacity):
        '''Creates an empty Queue with a capacity'''
        self.capacity = capacity
        self.num_items = 0
        self.head = None
        self.tail = None


    def is_empty(self):
        '''Returns True if the Queue is empty, and False otherwise'''
        return self.num_items == 0


    def is_full(self):
        '''Returns True if the Queue is full, and False otherwise'''
        return self.num_items == self.capacity


    def enqueue(self, item):
        newNode = Node(item)
        '''If Queue is not full, enqueues (adds) item to Queue
           If Queue is full when enqueue is attempted, raises IndexError'''
        if not self.is_full():
            if self.is_empty():
                self.head = newNode
                self.tail = self.head
            else:
                self.tail.next = newNode
                self.tail = newNode
            self.num_items += 1
        else:
            raise IndexError('cannot enqueue to full queue')




    def dequeue(self):
        '''If Queue is not empty, dequeues (removes) item from Queue and returns item.
           If Queue is empty when dequeue is attempted, raises IndexError'''
        if not self.is_empty():
            dqd = self.head
            self.head = self.head.next
            self.num_items -= 1
            return dqd.data
        else:
            raise IndexError('cannot dequeue from an empty')

    def size(self):
        '''Returns the number of elements currently in the Queue, not the capacity'''
        return self.num_items
