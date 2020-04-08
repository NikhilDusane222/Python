#Prime numbers is range 1-1000
START=1
END=1000
a = []
#Function for prime number
def primes(START,END):

    for i in range(START,END):
        count = 0
        for j in range(2, i):
            if i % j == 0:
                count += 1

        if count == 0 and i != 1:
            print(i,end=",")
    return a

#print the elements
print(primes(START,END))
print()
#Prime Numbers between 0 to 100
print("Prime Numbers between 0 to 100:")
T100 = a[:25]
print(T100)
print()
#Prime Numbers between 101 to 200
print("Prime Numbers between 101 to 200:")
T200 = a[25:46]
print(T200)
print()
#Prime Numbers between 201 to 300
print("Prime Numbers between 201 to 300:")
T300 = a[46:62]
print(T300)
print()
#Prime Numbers between 301 to 400
print("Prime Numbers between 301 to 400:")
T400 = a[62:78]
print(T400)
print()
#Prime Numbers between 401 to 500
print("Prime Numbers between 401 to 500:")
T500 = a[78:95]
print(T500)
print()
#Prime Numbers between 501 to 600
print("Prime Numbers between 501 to 600:")
T600 = a[95:109]
print(T600)
print()
#Prime Numbers between 601 to 700
print("Prime Numbers between 601 to 700:")
T700 = a[109:125]
print(T700)
print()
#Prime Numbers between 701 to 800
print("Prime Numbers between 701 to 800:")
T800 = a[125:139]
print(T800)
print()
#Prime Numbers between 801 to 900
print("Prime Numbers between 801 to 900:")
T900 = a[139:154]
print(T900)
print()
#Prime Numbers between 901 to 1000
print("Prime Numbers between 901 to 1000:")
T1000 = a[154:168]
print(T1000)
print()