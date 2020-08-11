class IceCream:
    def __init__(self, flavor, num_sprinkles):
        self.flavor = flavor
        self.num_sprinkles = num_sprinkles


ice1 = IceCream("Chocolate", 13)         # value of 23
ice2 = IceCream("Vanilla", 0)           # value of 5
ice3 = IceCream("Strawberry", 7)         # value of 17
ice4 = IceCream("Plain", 18)             # value of 18
ice5 = IceCream("ChocolateChip", 3)      # value of 8


def sweetest_icecream(lst):
    value = {'Plain': 0, 'Vanilla': 5, 'ChocolateChip': 5,
             'Strawberry': 10, 'Chocolate': 10}
    # return max(map(lambda x: value[x.flavor]+x.num_sprinkles, lst))
    return max(i.num_sprinkles + value[i.flavor] for i in lst)


print(sweetest_icecream([ice1, ice2, ice3, ice4, ice5]))  # ➞ 23

print(sweetest_icecream([ice3, ice1]))  # ➞ 23

print(sweetest_icecream([ice3, ice5]))  # ➞ 17
