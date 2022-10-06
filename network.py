import socket



class Network:
	def __init__(self):
		self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server = "127.0.0.1"
		self.port = 49815
		self.addr = (self.server, self.port)
		self.id = self.connect()
		print(self.id)

	def connect(self):
		try:
			self.client.connect(self.addr)
			return self.client.recv(2048).deocde()
		except Exception as e:
			print(e)
	
	def send(self, data):
		try:
			self.client.send(str.encode(data))
			return self.client.recv(2048).deocde()
		except (Exception, socket.error) as e:
			print(e)
		

a = Network()

a.connect()