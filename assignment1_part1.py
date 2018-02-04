#!/usr/bin/python

def listDivide(numbers, divide=2):
    return sum(1 for number in numbers if not number % divide)

class ListDivideException(Exception):
    pass

def testListDivide():
    if (listDivide([1, 2, 3, 4, 5]) != 2 or
        listDivide([2, 4, 6, 8, 10]) != 5 or
        listDivide([30, 54, 63, 98, 100], 10) != 2 or
        listDivide([]) != 0 or
        listDivide([1, 2, 3, 4, 5], 1) != 5):
        raise ListDivideException()

if __name__ == "__main__":
    testListDivide()

