class Bear:
    def sound(self):
        print("Groarr")

class Dog:
    def sound(self):
        print("Woof Woof")

def makesoung(animetype):
    animetype.sound() # call sound() function

bearjob = Bear()
dogjob = Dog()

makesoung(bearjob)
makesoung(dogjob)
print()

# another program

class Document:
    def __init__(self, name):
        self.name = name

    def show(self):
        raise NotImplementedError("Subclass must implement abstract method")

class pdf(Document):
    def show(self):
        return 'Show PDF File'

class word(Document):
    def show(self):
        return 'Show Word File'

print(pdf("Document").show())


print(pdf("Document").name)
print()

#another program

class Car:
    def __init__(self, name):
        self.name = name

    def drive(self):
        raise NotImplementedError ("Sub Class must Implemnet abstract method")
    def stop(self):
        raise NotImplementedError ("Sub Class Must implement abstract method")

class Track(Car):
    def drive(self):
        return 'Drive Slowly'
    def stop(self):
        return 'Truck is Stop'

class SportCar(Car):
    def drive(self):
        return 'Dive Fast'
    def stop(self):
        return 'Spot Car is stop'

obj_tuck = Track('Truck Car')
print(obj_tuck.drive())
print(obj_tuck.stop())
print()

obj_spot = SportCar("Spot Car")
print(obj_spot.drive())
print(obj_spot.stop())