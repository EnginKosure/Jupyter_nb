
# Create a get_name method which gets the ingredients and puts them
# in alphabetical order into a nice descriptive sentence. If there are multiple ingredients,
# add the word 'Fusion' to the end but otherwise, add 'Smoothie'. Remember to change '-berries to '-berry'.


class Smoothie:
    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.cost = ([eval(v[1:])
                      for k, v in prices.items() if k in self.ingredients])
        self.x = self.cost

    def get_cost(self):
        self.x = sum(self.cost)
        return '${:.2f}'.format(self.x)

    def get_price(self):
        return '${:.2f}'.format(self.x*2.5)

    def get_name(self):
        return ' '.join(sorted(map(lambda x: x.replace('ies', 'y'), self.ingredients)))+(bool(len(self.ingredients) == 1)*' Smoothie' or bool(len(self.ingredients) > 1)*' Fusion')


prices = {
    "Strawberries": "$1.50",
    "Banana": "$0.50",
    "Mango": "$2.50",
    "Blueberries": "$1.00",
    "Raspberries": "$1.00",
    "Apple": "$1.75",
    "Pineapple": "$3.50"
}


s1 = Smoothie(["Banana"])

print(s1.ingredients)  # ➞ ["Banana"]

print(s1.get_cost())  # ➞ "$0.50"

print(s1.get_price())  # ➞ "$1.25"

print(s1.get_name())  # ➞ "Banana Smoothie"
s2 = Smoothie(["Raspberries", "Strawberries", "Blueberries"])

print(s2.ingredients)  # ➞ ["Raspberries", "Strawberries", "Blueberries"]

print(s2.get_cost())  # ➞ "$3.50"

print(s2.get_price())  # ➞ "$8.75"

print(s2.get_name())  # ➞ "Blueberry Raspberry Strawberry Fusion"
