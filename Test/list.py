"""game = [[1, 2, 4], [5, 6, 7], [8, 9, 10]]
count = 0
for row in game:
    print(count, row)
    count +=1

print()

for value, row in enumerate(game):
    print(value, row)


game = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]


def game_bard(player=0, row=0, col=0):
    game[row][col] = player
    for count, row in enumerate(game):
        print(count, row)


game_bard(player=1, row=1, col=1)

"""


from mysql.connector import connect, errors

try:
    with connect(
        host = "localhost",
        user = "root",
        password = "toor",
    ) as connection:
        print(connection)


except errors as e:
    print(e)