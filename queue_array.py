
class Queue:
    '''Implements an array-based, efficient first-in first-out Abstract Data Type
       using a Python array (faked using a List)'''

    def __init__(self, capacity):
        '''Creates an empty Queue with a capacity'''
        self.capacity = capacity
        self.num_items = 0
        self.front = 0
        self.back = 0
        self.items = [None]*capacity



    def is_empty(self):
        '''Returns True if the Queue is empty, and False otherwise'''
        return self.num_items == 0


    def is_full(self):
        '''Returns True if the Queue is full, and False otherwise'''
        return self.num_items == self.capacity


    def enqueue(self, item):
        '''If Queue is not full, enqueues (adds) item to Queue
           If Queue is full when enqueue is attempted, raises IndexError'''
        if not self.is_full():
            if self.back + 1 == self.capacity:
                self.items[0] = item
                self.back = 0
            else:
                if self.is_empty():
                    self.items[0] = item #don't want to add to back to make the first thing in the Q at i == 1
                else:
                    self.back += 1
                    self.items[self.back] = item
            self.num_items += 1
        else:
            raise IndexError('cannot enqueue to full queue')


    def dequeue(self):
        '''If Queue is not empty, dequeues (removes) item from Queue and returns item.
           If Queue is empty when dequeue is attempted, raises IndexError'''
        if not self.is_empty():
            if self.front == self.capacity - 1:
                dqd = self.items[self.front]
                self.front = 0
                # self.items[self.front] = None
            else:
                dqd = self.items[self.front]
                # self.items[self.front] = None
                self.front += 1
            self.num_items -= 1
            return dqd
        else:
            raise IndexError('cannot dequeue from an empty queue')


    def size(self):
        '''Returns the number of elements currently in the Queue, not the capacity'''
        return self.num_items
