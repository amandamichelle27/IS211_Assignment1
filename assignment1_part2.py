#!/usr/bin/python

class Book(object):
    def __init__(self, author, title):
        self.author = author
        self.title = title

    def display(self):
        print self.title + ", written by", self.author

if __name__ == "__main__":
    Book("John Steinbeck", "Of Mice and Men").display()
    Book("Harper Lee", "To Kill a Mockingbird").display()
