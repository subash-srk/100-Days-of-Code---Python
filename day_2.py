#Data Types
#String
print("Hello"[4])
#Integer
print(123+345)
#Float
print(123.234)
#Boolean
print(True)

#type error, Type checking, Conversion
num_char = len(input("What is your name?"))
print(type(num_char))
new_num_char = str(num_char)
print("your name has " + new_num_char + " characters")


#F String
age = input()
# Your code below this line 👇
years = 90 - int(age)
weeks = years * 52

print(f"You have {weeks} weeks left.")
