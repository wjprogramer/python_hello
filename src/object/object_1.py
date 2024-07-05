class Student:
    def __init__(self, age, sex, name):
        self.age = age
        self.sex = sex
        self.name = name

    def fullname(self):
        print(f'{self.name}')


def object_1():
    stu_1 = Student(26, 'man', 'Benny')
    stu_1.fullname()

    # `物件.dict` 來取得該物件的所有屬性和對應的值。
    print(stu_1.__dict__)



