#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size

    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, size):
        if isinstance(size, int): # if I use'type' it is not iterable
            self._size = size
        else:
            print("size must be an integer")
            #raise ValueError("size must be an integer")
    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"

kshoe = Shoe("Addidas", 9)
kshoe.cobble()