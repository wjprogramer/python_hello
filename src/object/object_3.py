# Demo 1 --------------------------------------------------
class A:
    @staticmethod
    def x1():
        print('This is static method')


# Demo 2 --------------------------------------------------
# Inheritance
class Student:
    school_name = 'ABC School'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print(f'Hi, I am {self.name} and I am {self.age} years old.')


class Leader(Student):
    def __init__(self, name, age, position):
        super().__init__(name, age)
        self.position = position

    def talk(self):
        print(f'Hi, I am {self.name} and I am {self.age} years old. I am the {self.position} of the class.')

    # Magic method 又稱作 Dunder method (前後有兩條底線)
    def __repr__(self):
        # __repr__ 通常用在表示該物件生成時的樣態，讓開發者能夠快速理解這個物件和類別的用途。
        return f'Leader({self.name}, {self.age}, {self.position})'

    # __str__ : 通常是描述這個物件的屬性，讓使用者能夠快速了解物件的屬性和使用的方法。
    def __str__(self):
        return f'{self.name} - {self.age} - {self.position}'


# Demo 3 --------------------------------------------------
# Property decorators — Getter, Setters and Deleters
class User:
    def __init__(self):
        self.password_hash = ''

    @property
    def password(self):
        raise AttributeError('password is not readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


def generate_password_hash(password):
    return password


def check_password_hash(password_hash, password):
    return password_hash == password


def object_3():
    # Demo 1
    A.x1()

    # Demo 2
    leader = Leader('John', 20, 'President')
    print(f'isInstance {isinstance(leader, Leader)}')
    print(f'isSubclass {issubclass(Leader, Student)}')
    leader.talk()

    student = Student('Jane', 18)
    student.talk()

    # Demo 3
    user = User()
    print(f'user.password_hash: {user.password_hash}')
    user.password = 'password'
    print(f'user.password_hash: {user.password_hash}')





