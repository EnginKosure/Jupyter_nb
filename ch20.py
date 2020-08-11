class IceCream:

    def __init__(self, flavor, sweetness):
        self.value = {'Plain': 0, 'Vanilla': 5, 'ChocolateChip': 5,
                      'Strawberry': 10, 'Chocolate': 10}
        self.flavor = flavor
        self.sweetness = sweetness
        self.total = self.value[self.flavor]+self.sweetness


ice1 = IceCream("Chocolate", 13)         # value of 23
ice2 = IceCream("Vanilla", 0)           # value of 5
ice3 = IceCream("Strawberry", 7)         # value of 17
ice4 = IceCream("Plain", 18)             # value of 18
ice5 = IceCream("ChocolateChip", 3)      # value of 8


def sweetest_icecream(lst):
    total_l = list(map(lambda x: x.total, lst))
    return max(total_l)


print(sweetest_icecream([ice1, ice2, ice3, ice4, ice5]))  # ➞ 23

print(sweetest_icecream([ice3, ice1]))  # ➞ 23

print(sweetest_icecream([ice3, ice5]))  # ➞ 17
