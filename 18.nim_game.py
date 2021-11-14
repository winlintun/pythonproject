no_of_stones = 10

count = 1

player = 'Player1'


while no_of_stones > 0:

    if count%2 == 0:
        player = 'Player2'
    else:
        player = 'Player1'

    user_input = int(input(player+", would you like to remove '1' or '2' stones: "))
    while user_input != 1 and user_input != 2:
        user_input = int(input("Please enter '1' or '2'"))

    no_of_stones -= user_input # no_of_stones = no_of_stones - user_input
    print("There are",no_of_stones,'stones left.')

    count+=1

if player == 'Player1':
    player = 'Player2'
else:
    player = "Player1"
print(player,"is winner")