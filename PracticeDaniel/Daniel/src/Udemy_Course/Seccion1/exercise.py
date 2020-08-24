lottery_numbers = {13, 21, 22, 5, 8}

"""
A player looks like this:

{
    'name': 'PLAYER_NAME',
    'numbers': {1, 2, 3, 4, 5}
}

Define a list with two players (you can come up with their names and numbers).
"""

# players = []

"""
For each of the two players, print out a string like this: "Player PLAYER_NAME got 3 numbers right.".
Of course, replace PLAYER_NAME by their name, and the 3 by the amount of numbers they matched with lottery_numbers.
You'll have to access each player's name and numbers, and calculate the intersection of their numbers with lottery_numbers.
Then construct a string and print it out.

Remember: the string must contain the player's name and the amount of numbers they got right!
"""

players = (
    {'name': 'Daniel ',
     'numbers': {14, 21, 73, 34, 5}},
    {'name': 'Alejandro',
     'numbers': {13, 2, 22, 4, 5}}
)
numbers_player1= players[0]["numbers"]
numbers_player2= players[1]["numbers"]

resultado_1 = numbers_player1.intersection(lottery_numbers)
cantidad_numeros_1 = str(len(resultado_1))

resultado_2 = numbers_player2.intersection(lottery_numbers)
cantidad_numeros_2 = str(len(resultado_2))

print("Player " + players[0]["name"] + " got " + cantidad_numeros_1 + " numbers right")


print("Player " + players[1]["name"] + " got " + cantidad_numeros_2 + " numbers right")
