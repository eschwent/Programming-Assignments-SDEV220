#Emily Schwent
#Module 2 Case Study - if, else and while

#Accepts the name and GPA of student
FName = (input("Please enter the students first name: "))
LName = (input("Please enter the students last name: "))
Grade = float(input("Please enter the students grade point average:"))
EndLoop = "ZZZ"
#While loop and if/elif statements to test data entered
while LName != EndLoop:
    if Grade >= 3.5:
        print(FName, LName, ", has made the Dean's List.")
        FName = (input("Please enter the students first name: "))
        LName = (input("Please enter the students last name: "))
        Grade = float(input("Please enter the students grade point average:"))
    elif Grade >= 3.25:
        print(FName, LName, ", has made the Honor Roll.")
        FName = (input("Please enter the students first name: "))
        LName = (input("Please enter the students last name: "))
        Grade = float(input("Please enter the students grade point average:"))
    elif Grade < 3.25:
        print(FName, LName, ", has not made Honor Roll or the Dean's List.")
        FName = (input("Please enter the students first name: "))
        LName = (input("Please enter the students last name: "))
        Grade = float(input("Please enter the students grade point average:"))

