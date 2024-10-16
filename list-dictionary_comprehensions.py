from map_filter_enumerate import yell

family = [
    {"first_name": "Caren", "last_name": "Khachatrian"},
    {"first_name": "Hripsime", "last_name": "Shirvanian"},
    {"first_name": "Gregory", "last_name": "Khachatrian"},
    {"first_name": "Anais", "last_name": "Khachatrian"},
]


# LIST Comprehensions
khachatrians_list = [{"first_name": member["first_name"], "last_name": member["last_name"]} for member in family]
print(khachatrians_list)

# DICTIONARY Comprehensions
khachatrians_dictionary = {member["first_name"]: member["last_name"] for member in family}
print(khachatrians_dictionary)

# SET Comprehensions
test_set = {member["first_name"] for member in family}
print(test_set)

# DELETE dictionary object
del khachatrians_dictionary['Caren']
print(khachatrians_dictionary)

# Using a generator object
khachatrians = [
    member["first_name"] for member in family if member["last_name"].lower() == "khachatrian"
]
print(type(member["first_name"] for member in family if member["last_name"].lower() == "khachatrian"))

yell(*sorted(khachatrians))