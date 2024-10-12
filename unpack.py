def total(galleons: int, sickles, knuts: int = 0):
    return (galleons * 17 + sickles) * 29 + knuts

coins = [100, 50, 25]

print(total(*coins))

coin_purse = {"galleons": 100, "sickles": 50, "knuts": 25}

print(total(**coin_purse))
