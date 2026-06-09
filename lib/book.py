#!/usr/bin/env python3

class Book:
    def __init__(self,title,page_count):
        self.title =title
        if isinstance(page_count,int):
            self._page_count = page_count
        else:
            print("page_count must be an integer")
            self._page_count = 0
    
    @property
    def page_count(self):
        return self._page_count
    
    @page_count.setter
    def page_count(self,value):
        if isinstance(value,int):
            self._page_count = value
        else:
            print("page_count must be an integer")

    def turn_page(self):
        print("flipping the page")    


 # Create a book
novel = Book("The Great Gatsby", 180)
novel.turn_page()   # Output: Flipping the page
