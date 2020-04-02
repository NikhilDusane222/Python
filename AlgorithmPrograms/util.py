
class util:

    #Function for anagram or not
    @staticmethod
    def anagram(string1,string2):
        # the sorted strings are checked
        if (sorted(string1) == sorted(string2)):
            return True
        else:
            return False

    #Function for prime number in range
    @staticmethod
    def primerange(start,end):
        list=[]
        for i in range(start,end):
            count=0
            for j in range(2,i):
                if i%j==0:
                    count+=1

            if count==0 and i!=1:
                print(i)

    #Function for array list
    @staticmethod
    def arrayList(array):
        number = int(input("Enter how many elements you want to add : "))
        print("Enter elements : ")
        for i in range(number):
            array.append(int(input()))
        return array

    #function for binary search
    @staticmethod
    def binarySearch(array, low, high, num):
        if high >= low:
            mid = int((low + high) / 2)
            if array[mid] == num:
                return mid
            elif array[mid] > num:
                return util.binarySearch(array, low, mid - 1, num)
            else:
                return util.binarySearch(array, mid + 1, high, num)
        else:
            return -1
    #Function for insertion sort
    @staticmethod
    def insertionSort(array):
        for i in range(len(array)):
            temp = array[i]
            j = i - 1
            while j >= 0 and temp < array[j]:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = temp
        return array

    #function for bubble sort
    @staticmethod
    def bubbleSort(array):
        for i in range (len(array)):
            for j in range (i+1,len(array)):
                if array[i]>array[j]:
                    temp=array[i]
                    array[i]=array[j]
                    array[j]=temp
        return array



#main function
def main():
    choiceNo=int(input("Enter the choice number:  \n 1. Check the Anagram: \n 2. Prime number in range: \n 3. Binary search of integer: \n" 
                       " 4. Binary search of string: \n 5. Insertion sort for integer: \n 6. Insertion sort for string: \n "
                       "7. Bubble sort for integer: \n 8. Bubble sort for string \n "))

    #anagram function calling
    if choiceNo==1:
        string1=input("Enter first string: ")
        string2=input("Enter second string: ")
        if (util.anagram(string1, string2)):
            print("Strings are anagram ")
        else:
            print("Strings are not anagram")

    #prime number in range function calling
    elif choiceNo==2:
        start=int(input("Enter start number of range: "))
        end=int(input("Enter end number of range: "))
        list=util.primerange(start,end)

    #binary search function calling for integer
    elif choiceNo == 3:
        array = []
        array = util.arrayList(array)
        length = len(array)
        num = int(input("Enter number to search in the list : "))
        result = util.binarySearch(array, 0, length - 1, num)
        if result != -1:
            print("Element found in the list at the position of: ", result)
        else:
            print("Element not found in the list ")

    #binary search function calling for string/char
    elif choiceNo == 4:
        array = []
        number = int(input("Enter how many elements/char you want to add : "))
        print("Enter the elements : ")
        for i in range(number):
            array.append(input())
        length = len(array)
        string = input("Enter string to search in list : ")
        result = util.binarySearch(array, 0, length - 1, string)
        if result != -1:
            print("Element found in the list at the position of ", result)
        else:
            print("Element not found in the list ")

    #sort the elements using insertion sort function
    elif choiceNo == 5:
        array = []
        array = util.arrayList(array)
        array = util.insertionSort(array)
        print("The sorted list is : ", array)

    #sort the string/char using the insertion sort function
    elif choiceNo == 6:
        array = []
        number = int(input("Enter how many elements/char you want to add : "))
        print("Enter elements : ")
        for i in range(number):
            array.append(input())
        array = util.insertionSort(array)
        print("The sorted list is : ", array)

    #sort the element list using bubble sort
    elif choiceNo == 7:
        array = []
        array = util.arrayList(array)
        array = util.bubbleSort(array)
        print("The sorted list is : ", array)

    # sort the string list using bubble sort
    elif choiceNo == 8:
        array = []
        number = int(input("Enter how many elements you want to add : "))
        print("Enter the elements : ")
        for i in range(number):
            array.append(input())
        array = util.bubbleSort(array)
        print("The sorted list is : ", array)


    else:
        print("Invalid choice !! ")
main()
