from enum import Enum

class My_Class(Enum):
    AWAKE = 0
    ASLEEP = 1

print(My_Class.AWAKE)
print(My_Class["AWAKE"])
print(My_Class.AWAKE.value)
print(*My_Class)

# GLOBALS
balance = 0

def main():
    print("Balance:", balance)
    deposit(75)
    withdraw(50)
    print("Balance:", balance)

def deposit(n):
    global balance
    balance += n

def withdraw(n):
    global balance
    balance -= n

# CLOSURE
def counter():
    count = 0
    
    def increment():
        nonlocal count
        count += 1
        return count
    
    return increment

incrementor = counter()

print(incrementor())
print(incrementor())
print(incrementor())
print(incrementor())


if __name__ == "__main__":
    main()