class Student:
    def __init__(self, name, house=None):
        self.name = name
        self.house = house
    
    def __str__(self):
        return f"{self.name} is from {self.house}"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Student's name is missing.")
        self._name = name
    
    @property
    def house(self):
        return self._house
    
    @house.setter
    def house(self, house):
        if house not in ["Cyprus", "USA", "Armenia", "Russia"]:
            raise ValueError("Invalid house.")
        self._house = house

def main():
    student = get_student()
    print(student)

#return class - mutable
def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

#return tuple - immutable
def get_student_tuple():
    name = input("Name: ")
    house = input("House: ")
    return name, house

#return dict - mutable
def get_student_dict():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}

if __name__ == "__main__":
    main()