class name_info: # class
    """Global Scope"""
    name = "AungMoeKyaw"
    age = '22'
obj_name = name_info() # create object
p_name = obj_name.name # instant name
p_age = obj_name.age # instant age
print(p_name)
print(p_age)
print()

class car:
    car_hp = 0
    car_name = ""
    def __init__(self):
        print("****Car Inforamtion*****")
        self.car_hp = 0
        self.car_name = "Unknow"
        self.show_info()

    def set_name(self,hp):
        self.car_hp = hp

    def show_info(self):
        print("Car Name :",self.car_name)
        print("Car Hp :",self.car_hp)

first_obj = car()
print("________________________")


n_name = input("Enter Car Name: ")
first_obj.car_name = n_name


hp_unit = input("Enter Car Hp: ")
first_obj.car_hp = hp_unit

first_obj.show_info()
print("_________________________")


sec_obj = car()
print("__________________________")
sec_obj.car_name = "BMW"
sec_obj.car_hp = 2500
sec_obj.show_info()
