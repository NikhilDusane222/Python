#Check if leap year or not

year=int(input("Enter a year: "))

minyear=1000
maxyear=9999

if year >= minyear and year <= maxyear :
        if year % 4 == 0 and year % 100 != 0:
            print ("Entered year is a Leap Year ")
        elif year % 400 == 0:
            print("Entered year is a Leap Year ")
        else:
            print ("Entered year is not a Leap Year ")
else:
    print ("Invalid Year, Please Enter 4 digit valid year ")