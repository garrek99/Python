import copy

family = [
    {"first_name": "Caren", "last_name": "Khachatrian", "birth_year": 1977},
    {"first_name": "Hripsime", "last_name": "Shirvanian", "birth_year": 1979},
    {"first_name": "Gregory", "last_name": "Khachatrian", "birth_year": 2013},
    {"first_name": "Anais", "last_name": "Khachatrian", "birth_year": 2015}
]

# MIXED List
family_list = []
for member in family:
    family_list.append([member["first_name"], member["last_name"], member["birth_year"]])
print(family_list)

shallow_copy = copy.copy(family_list)
deep_copy = copy.deepcopy(family_list)

position = -1
for i, member in enumerate(family):
    if member["last_name"] == "Shirvanian":
        position = i
        break

family_list[position][1] = "Khachatrian"
print(shallow_copy)
print(deep_copy)