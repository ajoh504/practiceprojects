# index_of.py -- find an index in an unsorted list
#                receives a list of numbers, and a number to search for
#                returns int or None

class indexOf:
    def __init__(self, list_of_numbers, number):
        self.list_of_numbers = list_of_numbers
        self.number = number

    def index_of(self) -> int | None:
        for i in self.list_of_numbers:
            if i == self.number:
                return self.number
