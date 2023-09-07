# functions
def string_checker(question, num_letters, valid_responses):

    error = "Please choose a valid input"

    while True:
        response = input(question).lower()

        for item in valid_responses:
            if response == item[:num_letters] or response == item:
                return item

        print(error)


topping_list = ["pineapple", "ham", "bacon", "cheese", "olives", "xxx"]
pizza_cost = 0
# main routine

which_topping = 'none'
temp_toppings = []

while which_topping != 'xxx':
    which_topping = string_checker("Which extra topping do you want on your pizza? (type in \'xxx\' to quit): ",
                                   1, topping_list)
    if which_topping == "pineapple":
        print()
        print("You selected pineapple as an additional topping")
        pizza_cost = pizza_cost + 1
        temp_toppings.append(which_topping)
        pass
    elif which_topping == "ham":
        print()
        print("You selected ham as an additional topping!")
        pizza_cost = pizza_cost + 1
        temp_toppings.append(which_topping)
        pass
    elif which_topping == "bacon":
        print()
        print("You selected bacon as an additional topping!")
        pizza_cost = pizza_cost + 1
        temp_toppings.append(which_topping)
        pass
    elif which_topping == "cheese":
        print()
        print("You selected cheese as an additional topping!")
        pizza_cost = pizza_cost + 1
        temp_toppings.append(which_topping)
        pass
    elif which_topping == "olives":
        print()
        print("You selected olives as an additional topping!")
        pizza_cost = pizza_cost + 1
        temp_toppings.append(which_topping)
        pass
    elif which_topping == 'xxx':
        if len(temp_toppings) > 0:
            print()
            print("Further toppings will not be added!")
        else:
            print("No toppings will be added then!")
            temp_toppings.append("none")

print("You ordered the toppings {} for a cost of ${:.2f}".format(temp_toppings, pizza_cost))
