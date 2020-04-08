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

#Function for anagram number
def anagram(a):
    # initialize a list
    anagram_list = []
    for i in a:
        for j in a:
            if i != j and (sorted(str(i)) == sorted(str(j))):
                anagram_list.append(i)
    return anagram_list

#print the elements
print(primes(START,END))
print()
print("Prime Numbers between 0 to 100:")
T100 = a[:25]
print(T100, "\n")
print("The Anagram elements from 0 to 100 :", anagram(T100), "\n")
print("Prime Numbers between 101 to 200:")
T200 = a[25:46]
print(T200, "\n")
print("The Anagram elements from 101 to 200 :", anagram(T200), "\n")
print("Prime Numbers between 201 to 300:")
T300 = a[46:62]
print(T300, "\n")
print("The Anagram elements from 201 to 300 :", anagram(T300), "\n")
print("Prime Numbers between 301 to 400:")
T400 = a[62:78]
print(T400, "\n")
print("The Anagram elements from 301 to 400 :", anagram(T400), "\n")
print("Prime Numbers between 401 to 500:")
T500 = a[78:95]
print(T500, "\n")
print("The Anagram elements from 401 to 500 :", anagram(T500), "\n")
print()
print("Prime Numbers between 501 to 600:")
T600 = a[95:109]
print(T600, "\n")
print("The Anagram elements from 501 to 600 :", anagram(T600), "\n")
print("Prime Numbers between 601 to 700:")
T700 = a[109:125]
print(T700, "\n")
print("The Anagram elements from 601 to 700 :", anagram(T700), "\n")
print("Prime Numbers between 701 to 800:")
T800 = a[125:139]
print(T800, "\n")
print("The Anagram elements from 701 to 800 :", anagram(T800), "\n")
print()
print("Prime Numbers between 801 to 900:")
T900 = a[139:154]
print(T900, "\n")
print("The Anagram elements from 801 to 900 :", anagram(T900), "\n")
print("Prime Numbers between 901 to 1000:")
T1000 = a[154:168]
print(T1000, "\n")
print("The Anagram elements from 901 to 1000 :", anagram(T1000), "\n")