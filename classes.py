# Instructions
# Create a Pizza type for representing pizzas in Python. Think about some basic properties that would define a pizza's values; things like size, crust type, and toppings would help. Define those in the __init__ method so each instance can have its own specific values for those properties.

# Add a method for interacting with a pizza's toppings, called add_topping.

# Add a method for outputting a description of the pizza (sample output below).

# Make two different instances of a pizza. If you have properly defined the class, you should be able to do something like the following code with your Pizza type.

# meat_lovers = Pizza()
# meat_lovers.size = 16
# meat_lovers.style = "Deep dish"
# meat_lovers.add_topping("Pepperoni")
# meat_lovers.add_topping("Olives")
# meat_lovers.print_order()
# You should produce output in the terminal similiar to the following string.

# "I would like a 16-inch, deep-dish pizza with Pepperoni and Olives."


class Pizza:

    def __init__(self):
        # Establish the properties of each book
        # with a default value
        self.size = 0
        self.crust = ""
        self.toppings = []

    def add_topping(self, topping):
        self.toppings.append(topping)
        # print(f'You start reading {self.title} at page {self.current_page}')

    def print_order(self):
        # to put it together into a list--
        self.toppings = ', '.join(self.toppings)
        print(
            f'I would like a {self.size} inch {self.crust} pizza with {self.toppings}')


veggie_lovers = Pizza()
veggie_lovers.size = 12
veggie_lovers.crust = "deep dish"
veggie_lovers.add_topping("Mushroom")
veggie_lovers.add_topping("Bell Pepper")
veggie_lovers.add_topping("Onions")

veggie_lovers.print_order()
