#Palindrome checker
#class Dequeue
class Deque:
    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items.insert(0, item)

    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)


def pal_check(string):
    # Palindrome checker using Deque
    pal_dq = Deque()
    for character in string:
        pal_dq.add_front(character)
    match = True
    while (pal_dq.size() > 1 and match):
        front = pal_dq.remove_front()
        rear = pal_dq.remove_rear()
        if front != rear:
            match = False
    return match

string=input("Enter string to check palindrome: ")
if (pal_check(string)):
    print(string, "is Palindrome ")
else:
    print(string, "is not Palindrome ")

