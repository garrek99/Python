def meow(n: int) -> str:
    '''Meow n times.
    :param n: NMumber of times to meow
    :type n: int
    :raise TypeError: If n is not an int
    :return: A string of n meows, one per line
    :rtype: str
    '''
    return "Meow\n" * 3

number: int = input("Number: ")
meows: str = meow(number)
print(meows, end="")