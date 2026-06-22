from student import *
obj= Students()

print("#-----------WELCOME TO STUDENT MANAGEMENT LIBRARY------------#")
print("--> To add info enter A")
print("--> To view all students enter V")
print("--> To search student enter S")
print("--> To update record enter U")
print("--> To delete record enter D")
print("--> To display student with highest marks enter H")
print("--> To exit enter E\n")

while True:
    ui= input("What you want to do today?: ").upper()
    if ui == "A":
        id= int(input("enter student id: "))
        std_name= input("enter student name: ")
        std_age= int(input("enter student age: "))
        std_marks= int(input("enter student marks: "))
        record = (id,std_name,std_age,std_marks)
        obj.student_info(record)
    if ui=="V":
        print(obj.a)