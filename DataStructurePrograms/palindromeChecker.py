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
    print(string, "is Palindrome ")
    match = True
    while (pal_dq.size() > 1 and match):
        front = pal_dq.remove_front()
        rear = pal_dq.remove_rear()
        if front != rear:
            match = False
            print(string, "is not Palindrome ")
    return match

string = input("Enter a string: ")
print(pal_check(string))
