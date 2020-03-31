#Get input from user and print 2D array

#get row and column size from user
row=int(input("Enter rows size: "))
column=int(input("Enter column size: "))

#initialize empty list
element=[]

print("Enter the entries:")
for i in range(row):
    a = []
    for j in range(column):
        a.append(int(input()))
    element.append(a)

# For printing the list
print(element)