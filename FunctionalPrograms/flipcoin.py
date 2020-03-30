import random
numberOfFlips=int(input("How many times you want to flip coin: "))

def flipcoin(number_of_flips):
    head=0
    tail=0
    for i in range(number_of_flips):
        num=random.random()
        if num<0.5:
            head+=1
        else:
            tail+=1
    headPercentage=(head/numberOfFlips)*100
    tailPercentage=(tail/numberOfFlips)*100
    return headPercentage ,tailPercentage

headPercent,tailPercent=flipcoin(numberOfFlips)
print(f"Head percent is {headPercent}% ")
print(f"Tail percent is {tailPercent}% ")
