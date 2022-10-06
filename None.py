print(type(None))

print(None == None)

print(None is None)


class Apple:
    def __eq__(self, other):
        return True

a = Apple()
print(a == None)

