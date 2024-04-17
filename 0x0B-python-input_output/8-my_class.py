#!/usr/bin/python3
""" My class module
"""

class MyClass:
    """ My class
    """

    def __init__(self, name):
        self.name = name
        self.number = 0
        self.matrix = [
                    [1, 2, 3],
                    [4, 5, 6]
                ]
        self.my_tup = (3, 5, 6, 9)
        self.my_set = {'str', 54, (3, 6), 3.2}

    def __str__(self):
        return "[MyClass] {} - {:d}".format(self.name, self.number)
