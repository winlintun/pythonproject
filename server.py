import socket
from _thread import *
import sys


server = "192.168.137.1" # IPV4 ADDRESS HERE
prot = 5555


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
	s.bind((server, port))
except (Exception, socket.error) as e:
	str(e)

s.listen(2)
print("Waiting for a connection, Server Started.")


def read_pos(str):
	str = str.split(",")
	return int(str[0]), int(str[1])

def make_pos(tup):
	return str(tup[0]) + "," + str(tup[1])

pos = [(0,0), (100, 100)]


def threaded_client(conn):
	conn.send(str.encode("Connection"))
	reply = ""
	while True:
		try:
			data = conn.recv(2048)
			reply = data.decode("utf-8")

			if not data:
				print("Disconnected")
				break
			else:
				print("Recieved: ", reply)
				print("Sending: ", reply)

			conn.sendall(str.encode(reply))
		except Exception as e:
			break
		
		print("Lost connection.")
		conn.close()


while True:
	conn, addr = s.accept()
	print("Connected to: ", addr)

	strat_new_thread(threaded_client, (conn, ))