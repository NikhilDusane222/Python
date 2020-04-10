#Class Queue
class Queue:
    def __init__(self):
        self.balance = 0
        print("Welcome to the Bank Cash Counter..")
        print("This is a Banking portal")

    #Function for deposite amount
    def enqueue_deposit(self):
        amount = int(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\nAmount Deposited:", amount)

    #Function for withdraw amount
    def dequeue_withdraw(self):
        amount = int(input("Enter amount to be Withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\nYou Withdrew:", amount)
        else:
            print("\nInsufficient balance ")

    #Function for display amount
    def queue_display(self):
        print("\nNet Available Balance=", self.balance)

    #Function for exit
    def queue_exit(self):
        exit()

#Main function
if __name__ == '__main__':
    q = Queue()
    try:
        while True:
            print("Please Enter the option that you want to make a transaction:")
            #Choice for Deposite and Withdrawn amount
            choiceNo = int(input(
                " 1. Deposite Amount to the account \n 2. Withdraw Amount from the account \n "
                "3. Display the amount \n 4. Cancel Transaction \n"))
            if choiceNo == 1:
                q.enqueue_deposit()
            elif choiceNo == 2:
                q.dequeue_withdraw()
            elif choiceNo == 3:
                q.queue_display()
            elif choiceNo == 4:
                q.queue_exit()
            else:
                print("Invalid Choice...!! Press the Correct choice")
    except ValueError:
        print("Invalid Choice...!! Press the Correct choice")
