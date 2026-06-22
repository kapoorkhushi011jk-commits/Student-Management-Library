class Students:
    def __init__(self):
        self.a = []

    def student_info(self, *info):
        self.a.append(info)
        return self.a
    

