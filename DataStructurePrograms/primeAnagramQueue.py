#Prime Numbers that are Anagram in the Range of 0 ­ 1000 in a Queue using the Linked List
START=1
END=1000
class Node:
    def __init__(self, value):
        self.data = value
        self.front = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def en_queue(self, value):
        new_node = Node(value)

        if self.tail is not None:
            #make the front attribute of old node point to new node
            self.tail.front = new_node

        else:
            #if first ever node in Queue both front and tail will point to it
            self.head = new_node

        self.tail = new_node
        self.count += 1

    def de_queue(self):
        if not self.is_empty():
            #point head to next node
            self.head = self.head.front
            self.count -= 1
            print("Deletion Sucess")
        else:
            print("Empty QUEUE")

    def is_empty(self):
        if self.head is None and self.tail is None:
            return True
        else:
            return False

    #Function for prime number
    def primes(START, END):
        a = []
        for i in range(START, END):
            count = 0
            for j in range(2, i):
                if i % j == 0:
                    count += 1

            if count == 0 and i != 1:
                print(i, end=",")
        return a

    #Function for anagram number
    def anagram(a):
        # initialize a list
        anagram_list = []
        for i in a:
            for j in a:
                if i != j and (sorted(str(i)) == sorted(str(j))):
                    anagram_list.append(i)
        return anagram_list

    print(" The Prime and Anagram elements are: ")
    a = primes(START,END)
    a=anagram(a)