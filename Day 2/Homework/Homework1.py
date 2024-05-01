number = float(input("Enter a number:"))
if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
else:
    print("The number is negative.")

num1= float(input("enter the first number:"))
num2= float(input("enter the second number:"))
num3= float(input("enter the third number:"))
largest = max(num1, num2, num3)
smallest = min( num1,num2, num3)
print("The smallest number is " + str(smallest) + ". The largest number is " + str(largest) + ".")