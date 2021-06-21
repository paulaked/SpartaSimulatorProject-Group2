# Create a waiting list.


# Using python lists we can implement a waiting list.
class WaitingList:

    # Initialise the waiting list to be empty.
    def __init__(self):
        self.items = []

    # Return True if waiting list has one group of no more than max people wanting to go to a destination.
    # Otherwise return False.
    def hasLocation(self, maximum, destination):
        for index in range(0, self.size()):
            this_group = self.items[index]
            if this_group[0] <= maximum and this_group[1] == destination:
                return True
        return False

    # Add to the waiting list.
    def put(self, group_size, destination):
        self.items.append((group_size, destination))

    # Return the number in the waiting list
    def size(self):
        return len(self.items)

    # Remove the first group of max people wanting to go to a destination.
    # If there is no such group. Do nothing.
    def take(self, maximum, destination):
        index = 0
        not_found = True
        while index < self.size() and not not_found:
            this_group = self.items[index]
            if this_group[0] <= maximum and this_group[1] == destination:
                self.items.pop(index)
                not_found = False
            else:
                index = index + 1

    # Return the total number of people still on waiting list waiting to be added to location.
    def still_waiting(self, destination):
        total = 0
        for group in self.items:
            if destination == group[1]:
                total += group[0]
            return total
