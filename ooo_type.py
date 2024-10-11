class Student:
    def __init__(self, name, house=None):
        self.name = name
        self.house = house
        
    def __str__(self):
        return f"{self.name} is from {self.house}"
    
    Houses = ["Cyprus", "USA", "Armenia", "Russia"]
    
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)
    
    @staticmethod
    def list_houses():
        print(Student.Houses)
    
def main():
    print(Student.Houses)
    student = Student.get()
    print(student)
    print(type(student))
    print(student.Houses)

if __name__ == "__main__":
    main()