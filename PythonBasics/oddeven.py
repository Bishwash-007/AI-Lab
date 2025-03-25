# WAP to check if a given input is odd or even

def oddEven(number):
    if number%2 == 0:
        print("number is even")
    else:
        print("number is odd")
        
num = input();
oddEven(int(num))