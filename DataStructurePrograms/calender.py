#Calender


def getDayNumber(date, month, year):
    y0 = year - (14 - month) // 12
    x = y0 + (y0 // 4) - y0 // 100 + y0 // 400
    m0 = month + 12 * ((14 - month) // 12) - 2
    d0 = (date + x + (31 * m0) // 12) % 7
    return d0

def leapYear(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False

def monthsData(month,year):
    nonLeap = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]
    leap = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]
    month_31 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
    month_30 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return month_31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return month_30
    elif month == 2 and leapYear(year):
        return leap
    else:
        return nonLeap

months = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September",
          "October", "November", "December"]
days = [ 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month=2
year=2020
if month == 2 and leapYear(year):
    print("      ",months[month],year)

print("Sun","Mon","Tue","Wed","Thu","Fri","Sat")

d=getDayNumber(month,1,year)
for i in range(d):
    print("  ")
    for i in range(days[month]):
        print(i+1, end= " ")
        if (i + d-1) % 7 == 0:
            print()
