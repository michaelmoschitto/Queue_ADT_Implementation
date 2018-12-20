import unittest
from queue_array import Queue
# from queue_linked import Queue

'''Trivial test to ensure method names and parameters are correct'''
class TestLab1(unittest.TestCase):
    def test1(self):
        q = Queue(5)
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)
        q.enqueue(5)
        print(q.items)
        print(q.dequeue())
        print(q.dequeue())
        print(q.dequeue())
        print(q.dequeue())
        print(q.dequeue())
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)
        q.enqueue(5)




    def test_queue1(self):

        # HAVE TO ADD MORE TESTS TO THIS
        q = Queue(5)
        q.enqueue('thing')
        q.enqueue('thing1')
        q.enqueue('thing2')
        q.enqueue('thing3')
        q.enqueue('thing4')
        self.assertTrue(q.is_full())
        for i in range(q.num_items):
            q.dequeue()
        self.assertTrue(q.is_empty())

    '''Tests the functionality of the is empty method'''
    def test_is_empty(self):

        q = Queue(5)
        q.enqueue('thing')
        q.enqueue('thing1')
        q.enqueue('thing2')
        self.assertFalse(q.is_empty())
        for i in range(q.num_items):
            q.dequeue()
        self.assertTrue(q.is_empty())

    '''Tests the functionality of the is full method'''
    def test_is_full(self):
            q = Queue(5)
            q.enqueue('thing')
            q.enqueue('thing1')
            q.enqueue('thing2')
            self.assertFalse(q.is_full())
            q.enqueue('thing3')
            q.enqueue('thing4')
            self.assertTrue(q.is_full())
    #
    # def test_array_enqueue(self): #will only work for the array implementation
    #     for i in range(q.capacity):
    #         q.enqueue(i)
    #     self.assertEqual(q.items,[0,1,2,3,4])

    '''tests both the enqueue and dequeue methods and their functionality'''
    def test_enqueue_and_dequeue(self):
        q = Queue(5)
        for i in range(q.capacity):
            q.enqueue(i)
        with self.assertRaises(IndexError):
            q.enqueue(10)
        for i in range(5):
            # print(q.items)
            # print(q.front)
            self.assertEqual(q.dequeue(), i)
            # print(q.size())
        self.assertTrue(q.is_empty())
        with self.assertRaises(IndexError):
            q.dequeue()

    '''Tests the functionality of the size function'''
    def test_size(self):
        q = Queue(5)
        for i in range(q.capacity):
            q.enqueue(i)
        self.assertEqual(q.size(), 5)

    '''Tests implementation of queue when it wraps around from items[capacity] to items[0]'''
    def test_circular_implementation(self):
        q = Queue(5)
        q.enqueue(23)
        q.enqueue(45)
        q.dequeue()
        self.assertEqual(q.size(), 1)
        # self.assertEqual(q.front, 1)
        # self.assertEqual(q.back, 1)
        q.enqueue(143)
        # self.assertEqual(q.back, 2)
        # self.assertEqual(q.front, 1)
        self.assertEqual(q.size(), 2)
        q.enqueue(2345)
        q.enqueue(1)
        # self.assertEqual(q.front, 1)
        # self.assertEqual(q.back, 4)
        self.assertEqual(q.size(), 4)
        q.enqueue(0)
        # self.assertEqual(q.front, 1)
        # self.assertEqual(q.back, 0)
        self.assertEqual(q.size(), 5)
        q.dequeue()
        q.dequeue()
        q.dequeue()
        q.dequeue()
        # print(q.items)
        # self.assertEqual(q.front, 0)
        # self.assertEqual(q.back, 0)
        q.enqueue(2)
        self.assertEqual(q.size(), 2)

        # q = Queue(5)
        # q.enqueue(1)
        # q.enqueue(2)
        # q.enqueue(3)
        # self.assertEqual(q.dequeue(), 1)
        # self.assertEqual(q.dequeue(), 2)
        # q.enqueue(4)
        # q.enqueue(5)
        # q.enqueue(6)
        # self.assertEqual(q.dequeue(), 3)
        # self.assertEqual(q.dequeue(), 4)
        # self.assertEqual(q.dequeue(), 5)
        # self.assertEqual(q.dequeue(), 6)
        # self.assertTrue(q.is_empty())

    def test_two(self): #NOT MY TEST
        r = Queue(5)
        r.enqueue(1)
        r.enqueue(2)
        r.enqueue(3)
        self.assertEqual(r.num_items,3)
        self.assertEqual(r.dequeue(),1)
        self.assertEqual(r.dequeue(),2)
        self.assertEqual(r.num_items,1)
        with self.assertRaises(IndexError):
            while True:
                r.enqueue(1)


    def test_queue(self):  #NOT MY TESTS
        '''Trivial test to ensure method names and parameters are correct'''
        q = Queue(5)
        self.assertTrue(q.is_empty())
        self.assertFalse(q.is_full())
        q.enqueue('thing')
        self.assertEqual(q.dequeue(),'thing')
        self.assertEqual(q.size(),0)
        for i in range(5): q.enqueue(i)
        self.assertTrue(q.is_full())
        self.assertFalse(q.is_empty())
        with self.assertRaises(IndexError):
            q.enqueue(1)
        self.assertEqual(q.size(),5)
        with self.assertRaises(IndexError):
            e = Queue(1)
            e.dequeue()



if __name__ == '__main__':
    unittest.main()
