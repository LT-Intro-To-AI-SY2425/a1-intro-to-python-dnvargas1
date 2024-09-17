# Complete your individualized AI problems here

# 1: Write a Python program that prints "Hello, World!" to the console.

print("Hello, World!")

# 2: Write a Python program that asks the user to input two numbers, adds them together, and then prints the result.

num1 = int(input("Enter the first whole number: "))
num2 = int(input("Enter the second whole number: "))

sum = num1+num2

print("The sum of " + num1 + " and " + num2 + " is " + sum)

#3: Write a Python program that takes a number from the user and checks if the number is even or odd. Print a message indicating the result.

num = int(input("Enter a whole number: "))
if (int % 2) == 0:
    print("Your number is even!")
else:
    print("Your number is odd!")



def fizbuzz(input_num):
    if(input_num%3==0):
        if(input_num%5==0):
            return 'FizzBuzz'
        return 'Fizz'
    elif(input_num%5==0):
        return 'Buzz'
    else:
        return input_num

assert fizbuzz(1) == 1, "fizzbuzz 1 test"
assert fizbuzz(3) == "Fizz", "fizzbuzz 3 test"
assert fizbuzz(4) == 4, "fizzbuzz 4 test"
assert fizbuzz(5) == "Buzz", "fizzbuzz 5 test"
assert fizbuzz(6) == "Fizz", "fizzbuzz 6 test"
assert fizbuzz(15) == "FizzBuzz", "fizzbuzz 15 test"

