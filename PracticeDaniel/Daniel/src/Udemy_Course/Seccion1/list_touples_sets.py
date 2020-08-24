# ------------------ lists in python ------------------
print("List in python")
friends = ["Rolf", "Bob", "Anne"]
print(friends[0])
print(friends[1])
print(friends[2])

print(len(friends))  # print the length of the list

friends_list_list = [
    ["Rolf", 24],
    ["Bob", 25],
    ["Anne", 26]
]
print(friends_list_list[0])
print(friends_list_list[0][0])

friends.append("Daniel")  # Agregar registro a la linea
print(friends)

friends.remove("Anne")
print(friends)

# ------------------ tuples in python ------------------
print("Tuples in Python")

short_tuple = "rolf", "bob"
tuple = ("Rolf", "Bob")
tuple_in_list = [("Rolf", "Bob")]  # tuple inside a list

friends_tuple = ("TRolf", "Bob", "Anne")
# you cannot append to a tuple.
friends_tuple = friends_tuple + ("Jen",)
# youre not adding to a tuple, youre creating a new tuple with the old one a new one ("jenn",)
print(friends_tuple)

# ------------------ sets in python ------------------
# Sets doesnt hold order and duplicated elements
print("Sets in python")
art_friends = {"Rolf", "Anne", "Jen"}
science_friends = {"Jen", "Charlie"}
# art_friends.add("Jen")
# print(art_friends)
# art_friends.remove("Rolf")
# print(art_friends)

art_but_not_science = art_friends.difference(science_friends)
science_but_not_art = science_friends.difference(art_friends)

print(art_but_not_science)
print(science_but_not_art)

not_in_both = art_friends.symmetric_difference(science_friends)
print(not_in_both)
art_and_science = art_friends.intersection(science_friends)
print(art_and_science)

all_friends = art_friends.union(science_friends)
print(all_friends)

set_1 = {1, 2, 3, 4, 5}
set_2 = {3, 4, 5, 6, 7}

# Combine set_1 and set_2
print(set_1.union(set_2))  # {1, 2, 3, 4, 5, 6, 7}

# Find common elements in set_1 and set_2
print(set_1.intersection(set_2))  # {3, 4, 5}

# Find elements in set_1 which are not in set_2
print(set_1.difference(set_2))  # {1, 2}

# ------------------ dictionary in python ------------------
#dictionary keeps order, can add new keys, cannot have duplicate keys
print("Dictionary in python")
friend_ages_dict = {"Rolf":24, "Adam":3, "Anne":27}
print(friend_ages_dict)
friend_ages_dict["Bob"] = 20
friend_ages_dict["Rolf"] = 25
print(friend_ages_dict)

friends_dict = (
    {"name": "Rolf", "age" :24},
    {"name": "Adam", "age" :28},
    {"name": "Anna", "age" :32}
)
print(friends_dict[0]["name"])
print(friends_dict[1]["name"])
print(friends_dict[2]["name"])

#to convert a tuple into dictionary

friend_ages_tuple = [("Rolf",24), ("Adam",34), ("Anne",27)]
friend_ages_convert_dict = dict(friend_ages_tuple)
print(friend_ages_convert_dict)


#--------------------- Joining Lists -------------
#retreive a list and separete the values with the character you want
print("Joining List")

friends = ["Rolf","Anne", "Charlie"]
comma_separated = ", ".join(friends) #you can separated with any character
print(f"My Friends are {comma_separated}")