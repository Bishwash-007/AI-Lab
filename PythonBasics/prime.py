from math import sqrt, ceil

def PrintPrime(num1, num2):
    for num in range(num1, num2+1):
        if num > 1:
            for i in range(2, ceil(sqrt(num)) + 1):
                if (num % i) == 0:
                    break
            else:
                print(num)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("Prime numbers between", num1, "and", num2, "are:")
PrintPrime(num1, num2)
