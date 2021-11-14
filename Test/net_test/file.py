"""

class Letter(object):
    def __init__(self, a, b, c):
        self.a = a
        self._b = b
        self.__c = c

    def call_value(self):
        var = self.__c
        return var

new_object = Letter('I am Public', "i am Protected", 'I am private')

print(new_object.a)
print(new_object._b)
print(new_object.call_value())

"""

class Letter:
    __num = 100
    __num1 = 200

    def set_valu(self, a, b):
        self.__num = a
        self.__num1 = b

    def show(self):
        print(self.__num)
        print(self.__num1)

new_obj = Letter()
new_obj.show()
new_obj.set_valu(5000, 10000)
new_obj.show()