class Student:
    school_name = 'ABC School'  # 1. class(static) variable

    def __init__(self, name):
        self.name = name  # 2. instance variable


class A:
    b = 'A'

    def x1(self):
        A.b = 'B'

    @classmethod
    def x2(cls):
        cls.b = 'C'


def object_2():
    a = A()
    a.x1()
    print(f'1. A.b = {A.b}')
    a.x1()
    print(f'2. A.b = {A.b}')
    a.x2()
    print(f'3. A.b = {A.b}')
