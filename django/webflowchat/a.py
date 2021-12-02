


#user = User()


def search_product():
	print("Search Product")

def view_product():
	print("View Product")

def buy_and_add_to_card():
	user_input = input("Do you have payment: (Y/N): ")
	if user_input == 'Y' and user_input == 'y':
		print("Payment System")
		print("1: Online Payment \n 2: Cash on Delivery :")
		choose = int(input("Enter option: "))

		if choose == 1:
			print("Online Payment")
			print("Payment Successful!\n Order Placed")

		elif choose == 2:
			print("Cash on Delivery")
			print("Payment Successful\n Order Placed")
	
	elif user_input == 'N' and user_input =='n':
		return buy_and_add_to_card()

def order_place():
	print("Order Placed.")
