#print table power of 2:

power=int(input("Enter How many power you want to print: "))

def powerOfTwo(power):
    for i in range(power+1):
        print(f"2^{i}={2**i}")
powerOfTwo(power)