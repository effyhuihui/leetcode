__author__ = 'effy'
'''
We have a integer iterator that has two methods(but you don't know how they are implemented):
1. hasNext() -- checks whether there is next integer element
2. next() -- returns the next integer element

Utilizing integer iterator to implement a positive integer iterator that has two methods:
1. hasNextPostive() -- checks whether there is next positive element
2. nextPositive() -- returns next positive integer

catch:
you can only use two known methods of an existing API to implement a new API
'''

class IntegerIterator:
    def __init__(self,list_of_number):
        "somthing"
        pass

    def hasNext(self):
        ## return Boolean
        pass

    def next(self):
        ## return the next integer
        pass


'''
next() method in IntegerIterator will move the cursor to the actual next integer!!!!
you don't want to move cursor when you implement hasNextPositive()
'''
class PositiveIntegerIterator:

    def __init__(self, list_of_numbers):
        self.nums = IntegerIterator(list_of_numbers)
        self.next_positive = None
        self.goToNextPositive()

    def goToNextPositive(self):
        while self.nums.hasNext():
            a = self.nums.next()
            if a > 0:
                self.next_positive = a
                break
        if a <= 0:
            self.next_positive = None

    def hasNextPostive(self):
        '''
        no cursor move
        '''
        if self.next_positive:
            return True
        else:
            return False

    def nextPositive(self):
        '''
        cursor moves to the next positive after the current next positive
        '''
        cur_next_positive = self.next_positive
        self.goToNextPositive()
        return cur_next_positive





