class Private:
	def __init__(self):
		self.name = name


class NotPrivate:
	def __init__(self, name):
		self.name = name
		# self.priv = Private(name)


	def _display(self): # private
		print("Hello")

	def display(self): # public
		print("Hi")



a = NotPrivate('value-a')

a._display()
a.display()