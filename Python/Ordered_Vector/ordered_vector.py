import numpy as np


class Ordered_Vector:

    def __init__(self, capacity):
        self.capacity = capacity
        self.last_position = -1
        self.vals = np.empty(self.capacity, dtype=int)

    # O(n)
    def display(self):
        if self.last_position == -1:
            print('The vector is empty')
        else:
            for i in range(self.last_position + 1):
                print(i, ' - ', self.vals[i])

    # O(n)
    #When inserting items in an already ordered vector
    #you must take into acount the correct position to include the item. 
    #
    def including(self, val):
        if self.last_position == self.capacity - 1:
            print('Maximum capacity reached')
            return

        #In which position to include the new element?
        position = 0
        for i in range(self.last_position + 1):
            position = i
            if self.vals[i] > val:
                break
            if i == self.last_position:
                position = i + 1


        x = self.last_position
        while x>= position:
            self.vals[x + 1] = self.vals[x]
            x -= 1

        self.vals[position] = val
        self.last_position += 1

    # O(n) 
    #Linear search
    def linsearch (self, val):
        for i in range(self.last_position + 1):
            if self.vals[i] > val:
                return -1
            if self.vals[i] == val:
                return i
            if i == self.last_position:
                return -1

    # O(log n)
    def binsearch (self, val):
        lower_limit = 0
        upper_limit = self.last_position

        while True:
            current_position = int((lower_limit + upper_limit) / 2)

            # If it was found on the first attempt:

            if self.vals[current_position] == val:
                return current_position

            # If the value was not found:
            elif lower_limit > upper_limit:
                return -1

            # Dividing the limits
            else:
                # Lower limit
                if self.vals[current_position] < val:
                    lower_limit = current_position + 1

                # Upper Limit
                else:
                    upper_limit = current_position - 1

    # O(n)
    def excluding(self, val):
        position = self.searching(val)
        if position == -1:
            return -1
        else:
            for i in range(position, self.last_position):
                self.vals[i] = self.vals[i + 1]

            self.last_position -= 1

vector = Ordered_Vector(10)
vector.display()

print("Including items in the vector")
vector.including(8)
vector.including(9)
vector.including(4)
vector.including(1)
vector.including(5)
vector.including(7)
vector.including(11)
vector.including(13)
vector.including(2)
vector.display()

#Executing binary search: 
print("executing binary search")
vector.binsearch(7)
vector.binsearch(5)
vector.binsearch(13)
vector.binsearch(20)
vector.display()
