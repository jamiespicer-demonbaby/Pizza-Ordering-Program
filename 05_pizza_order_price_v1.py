# functions
def string_checker(question, num_letters, valid_responses):

    error = "Please choose a valid input"

    while True:
        response = input(question).lower()

        for item in valid_responses:
            if response == item[:num_letters] or response == item:
                return item

        print(error)


def calc_pizza_price(var_pizza):
    price = 0
    if var_pizza == "cheese":
        price = 7.5

    elif var_pizza == "meat lovers":
        price = 9

    elif var_pizza == "pepperoni":
        price = 8

    elif var_pizza == "ham":
        price = 8

    elif var_pizza == "hawaiian":
        price = 8.5

    return price


# pizza valid options
pizzas_list = ["cheese", "meat lovers", "pepperoni", "ham", "hawaiian"]
# main routine


print("Please remember to be specific with the pizza order, e.g. \"cheese\" ")
which_pizza = string_checker("Which pizza do you want: ", 1, pizzas_list)
if which_pizza == "cheese":
    print()
    print("You selected a cheese pizza")
    pass
elif which_pizza == "meat lovers":
    print()
    print("You selected a meat lovers pizza")
    pass
elif which_pizza == "pepperoni":
    print()
    print("You selected a pepperoni pizza")
    pass
elif which_pizza == "ham":
    print()
    print("You selected a ham pizza")
    pass
elif which_pizza == "hawaiian":
    print()
    print("You selected a hawaiian pizza")
    pass
# calculate the pizzas price based on the selected option using the calc_pizza_price function.
pizza_cost = calc_pizza_price(which_pizza)

print("You ordered a {} pizza which costs ${:.2f}".format(which_pizza, pizza_cost))
