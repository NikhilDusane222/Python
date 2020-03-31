# Prime factorization

number=int(input("Enter the number :"))

def prime_factor(number):
    prime_factors=[]
    while number>1:
        for factor in range(2,number+1):
            if number%factor==0:
                number=number//factor
                prime_factors.append(factor)
    return prime_factors

print(prime_factor(number))