class Veichle:
	def __init__(self, price, color):
		self.color = color
		self.price = price
		self.gas = 0

	def fillUpTank(self):
		self.gas = 100

	def emptyTank(self):
		self.gas = 0

	def gasLeft(self):
		return self.gas 

class Truck(Veichle):
	def __init__(self, price, color, tires):
		super().__init__(price, color)
		self.tires = tires


	def beep(self):
		print("Honk honk")



class Car(Veichle):
	def __init__(self, price, color, speed):
		super().__init__(price, color)
		self.speed = speed

	def beep(self):
		print("Beep Beep")