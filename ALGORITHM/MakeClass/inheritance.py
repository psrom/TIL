class Animal:
    def __init__(self, age, sex):
        self.age = age
        self.sex = sex
        print('Animal class의 __init__() 함수가 호출되었습니다.')
    def walk(self):
        print("걷는다")
    def print_info(self):
        print('age: {}, sex: {}'.format(self.age, self.sex))


class Dog(Animal):
    def __init__(self, age, sex):
        Animal.__init__(self, age, sex)
        print("Dog Class의 __init__() 함수가 호출되었습니다.")
    def bark(self):
        print("짖는다")

# =======================================================
dog = Dog(3, 'male')
dog.walk()
dog.print_info()
dog.bark()