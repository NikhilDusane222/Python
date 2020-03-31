# print harmonic number

number = int(input("Enter upto how many numbers you want to print: "))


def harmonicNumber(number):
    a = 0
    for i in range(1, number+1):
        print(f"1 / {i}",end=" + ")
        a+=1 / i

    #print("")
    print(a)
harmonicNumber(number)
