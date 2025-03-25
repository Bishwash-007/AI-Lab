# WAP calculate the sum , difference , product and difference from two input numbers using a single fuction

def calculate(num1, num2):
    sum = num1 + num2
    difference = num1 - num2
    product = num1 * num2
    difference = abs(num1 - num2)

    return sum, difference, product, difference

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))


sum, difference, product, difference = calculate(num1, num2)

print("Sum: ", sum)
print("Difference: ", difference)
print("Product: ", product)
print("Differenceabs: ", difference)