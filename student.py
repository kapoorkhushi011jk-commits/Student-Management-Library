class Students:
    def __init__(self):
        self.a = []

    def student_info(self, *info):
        self.a.append(info)
        return self.a
    
obj=Students()
adding = eval(input("Add student info in this order []"))
print(obj.student_info(23,"dgdghf",45,242))
print(obj.a)
