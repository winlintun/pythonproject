class Dog():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sit(self):
        print("Dog is Sitting")
    def brak(self):
        print("Dog is Braking")
dog1 = Dog("Aung Net",5)
print("My Dog Name is",dog1.name)
print("It is",dog1.age,'years old')
dog1.sit()
dog1.brak()

print()
print()
print("Inheritance")
class Dgo():
    def __int__(self,name,age):
        self.name = name
        self.age = age
    def sit(self):
        print("Dog is Sitting")
    def bark(self):
        print("Dog is barking")
class Hound(Dog):
    def __int__(self, name,age):
        super().__init__(name,age)
    def play(self):
        print("Dog is Playing")
    def hunting(self):
        print("Dog is Hunting")
dog1 = Hound("Aung Net",5)
print(dog1.name)
print(dog1.age)
dog1.sit()
dog1.brak()
dog1.play()
dog1.hunting()