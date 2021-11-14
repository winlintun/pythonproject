# range function
for number in range(3):
    print(number, end=' ')

color = ['red', 'green', 'blue']
for i in range(len(color)):
    print(color[i])
    #print(i)
    #print(color)

# reversed()
for i in range(len(color)-1, -1, -1):
    print(color[i], end=' ')
print()

for color in reversed(color):
    print(color, end=' ')
