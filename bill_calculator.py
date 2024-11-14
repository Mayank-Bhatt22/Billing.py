while True:
    name = input("Enter customer's name: ")
    phone_no = input("Enter your phone no: ")
    total = 0

    while True:
        print("enter the amount and quantity:- ")
        amount = float(input("enter amount: "))
        quantity = float(input("enter quanity: "))
        total += amount * quantity
        repeat = input('do you want to add more item ?(yes/no): ')
        if repeat == "no" or repeat == "no":
            break
    print("_"*40)
    print("Name: ", name)
    print("Amount to be paid: ", total)
    print("_"*40)
    print("""Thank You
********* HAPPY SHOPING********* """)
    repeat1 = input("do you want to go to next customer ? (yes/no)")
