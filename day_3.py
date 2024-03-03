#number = int(input("Enter the number: "))

#if number % 2 == 0:
 # print("This is an even number.")
#else:
 # print("This is an odd number.")

height = int(input("Enter Height: "))
age = int(input("Enter your age: "))
bill = 0
if height>=120:
    print("You can ride")
    if age < 12:
        bill = 5
        print("$5 Ticket")
    elif  age <=18:
        bill = 7
        print("$7 ticket")
    elif age >= 45 and age <=55:
        bill = 0
        print("Free cost")
    else:
        bill = 12
        print("$12 Ticket")
    
    pch = input("You want a Photo Y or N: ")
    if pch == "Y":
        bill +=5 
    print(f"Your final bill: ${bill}")
    
    
else:
    print("you cant ride")


