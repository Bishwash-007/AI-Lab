# WAP to input the percentage and display the division


def division(percentage):
    if percentage >=80:
        print("Disctinction")
    elif percentage >=65:
        print("First Division")
    elif percentage >=55:
        print("Second Division")
    elif percentage >= 40:
        print("Third Division")
    else :
        print("fail")

percentage = float(input("Enter percentage: "))
division(percentage)
    
    