# Your code below:
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

prices = [2, 6, 1, 3, 2, 7, 2]

num_two_dollar_slices = prices.count(2)

num_pizzas = len(toppings)
print("____________________________________________")
print("we sell " + str(num_pizzas) + " different kinds of pizza!")

print("____________________________________________")
pizza_and_prices = [[2, "pepperoni"], 
                    [6, "pineapple"],
                    [1, "cheese"],
                    [3, "sausage"],
                    [2, "olives"],
                    [7, "anchovies"],
                    [2, "mushrooms"]]


print(pizza_and_prices)
print("___________________________________________")
pizza_and_prices.sort()
print("Sorted List :")
print(pizza_and_prices)
print("____________________________________________")

cheapest_pizza = pizza_and_prices[0][1]

print("Cheapest Pizza :",cheapest_pizza)

priciest_pizza = pizza_and_prices[-1][1]

print("Expensive Pizza :",priciest_pizza)

pizza_and_prices.pop()
print("____________________________________________")
print("New List :")
print(pizza_and_prices)

print("___________________________________________")

print("New Pizza : peppers added")
pizza_and_prices.append([2.5, "peppers"])
print(pizza_and_prices)

print("____________________________________________")

three_cheapest = pizza_and_prices[:3]

print("Three Cheapest Pizza :")
print(three_cheapest)

print("____________________END_______________________")
