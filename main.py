from student import *
print("#-----------WELCOME TO STUDENT MANAGEMENT LIBRARY------------#")
print("--> To add info enter A")
print("--> To view all students enter V")
print("--> To search student enter S")
print("--> To update record enter U")
print("--> To delete record enter D")
print("--> To display student with highest marks enter H")
print("--> To exit enter E\n")
ui= input("Enter your input: ").upper()
if ui == "A":
    adding = eval(input("Add student info in this order [Student ID, Student Name, Age, Marks]: "))
    obj= Students()
    obj.student_info(adding)
if ui=="V":
    print(obj.a)