#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count = 7):
        self.title = title
        self.page_count = page_count
    @property
    def page_count(self):
        return self._page_count
    
    @page_count.setter
    def page_count(self, page_count):
        if not type(page_count) in (int,float):
            print("page_count must be an integer")
        self._page_count = page_count

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

book = Book("The World According to Garp", 69)
print(book.turn_page())
        