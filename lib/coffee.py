#!/usr/bin/env python3

class Coffee:
    def __init__(self,size,price):
        if size in ["Small","Meduim","Large"]:
            self._size = size 
        else:
            print("size must be small, Meduim, or Large")
            self._size = None
            self.price = price

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self,value):
        if value in ["Small","Meduim","Large"]:
            self._size = value
        else:
            print("size must be Small, Medium, or Large")

    def tip(self):
        print("Here's a tip")
        self.price += 1 

# Create a coffee
latte = Coffee("Medium", 3.5)
latte.tip()         # Output: This coffee is great, here’s a tip!
print(latte.price)  # 4.5                          