# Sample Coding Questions 01 Week 01
# Melissa Paksoy

#Defining variables
array = [1, 4, 7, 9]

print(array)

#Order of operations
a=1
b=2
c=3
d=4

e = ((a - ((b ** c) // d)) + (a % c))

print(f"e = {e}") #prints 0

#Formatting

temperature = 32.6
print("The temperature is : {:.3f}  degrees Celsius.".format(temperature))

#Common functions
userAge = int(input("Please enter your age: "))
userAge += 22
print(f"Now showing the shop items filtered by age: {userAge}")
