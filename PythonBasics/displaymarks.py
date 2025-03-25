# WAP to enter the marks of 10 students and diplay it 
def displayMarks():
    studentNumber=[]
    for i in range (1,10):
        print(f"please eneter the number of {i}th student")
        studentNumber.append(input())
    return studentNumber

marks=displayMarks()
for index,mark in enumerate (marks):
    print(f"The marks of {index+1} student is {mark}")
    
