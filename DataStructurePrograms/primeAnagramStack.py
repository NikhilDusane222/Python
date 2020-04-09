#Prime Numbers that are Anagram in the Range of 0 ­ 1000 in a Stack using the Linked List
#Global variables:
START=1
END=1000
#Node class
class Node:

    #Function for initialise the node object
    def __init__(self, data):
        self.data = data  #Assign data
        self.next = None  #Initialize next as null
        self.prev = None  #Initialize prev as null

#Stack class contains a Node object
class Stack:
    #Function for initialize head
    def __init__(self):
        self.head = None

    #Function for add an element data in the stack
    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            new_node.prev = None
            self.head = new_node

    #Function for pop top element
    def pop(self):
        if self.head is None:
            return None
        else:
            temp = self.head.data
            self.head = self.head.next
            self.head.prev = None
            return temp

    #Function for return top element in the stack
    def top(self):
        return self.head.data

    #Function for return the size of the stack
    def size(self):
        temp = self.head
        count = 0
        while temp is not None:
            count = count + 1
            temp = temp.next
        return count

    #Function to check if the stack is empty or not
    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    #Function for print the stack
    def printstack(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end="->")
            temp = temp.next

#Function for prime number
def primes(START,END):
    a = []
    for i in range(START,END):
        count = 0
        for j in range(2, i):
            if i % j == 0:
                count += 1

        if count == 0 and i != 1:
            print(i,end=",")
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