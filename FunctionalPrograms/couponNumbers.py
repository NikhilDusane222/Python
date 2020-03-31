# Coupon Numbers

while True:
    try:
        # get input from user to genearte n random coupon number
        number_of_coupon = int(input("Enter how many distinct coupons want to generate :"))
        if number_of_coupon > 0:
            break
        else:
            print("Invalid input!!")
    except:
        print("Invalid input !!")

#function for generate coupon number
def coupon_number(number_of_coupons):
    import random
    coupons=0
    random_numbers=0
    random_nums=[]
    while coupons!=number_of_coupon:
        number=random.randint(1,number_of_coupon)
        if number not in random_nums:
            random_nums.append(number)
            coupons+=1
    print(random_nums)
coupon_number(number_of_coupon)