# factorial of a number

def factorial(n):
    if n<0 :
        return "Factorial doesn't exist for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else :
        result = 1
        for i in range(2, n+1):
            result*=i
        return result
        
number = int(input("Enter your number: "))
print(f" The factorial of the {number} is {factorial(number)}")