import random
import pandas
# functions

# function that prints the menu and instructions,
# can be called by entering yes at the start of ordering each pizza


def show_instructions():
    print('''\n
***** Instructions *****

For each pizza order...
- Type the name of the pizza into the input box, press enter to continue.
- !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\
!!!!!!!!!!!!!!!!!!!!!!!!!!!
- Payment method (cash / credit)


The program will then display the pizzas details
including the cost of each pizza and the total cost.

A raffle will also be entered for the user which will allow them \
to have a 20% chance of winning for each order.


***** Menu *****

Please select which pizza you would like to order by typing it's name:
1. Cheese $7.50
2. Meat lovers $9.00
3. Pepperoni $8.00
4. Ham $8.00
5. Hawaiian $8.50

At the end of an order there is a 20% chance to win
 a mitre ten gift voucher

***************************''')

# function which can be called to show possible toppings
# and their cost.


def show_toppings():
    print('''\n
***** Possible extra toppings *****

Please select the topping you want by typing in the name of
the topping:
1. Pineapple (+$1.00)
2. Ham (+$1.00)
3. Bacon (+$1.00)
4. Cheese (+$1.00)
5. Olives (+1.00)
***************************''')


def not_blank(question):
    # this function checks if the input is blank
    # and does not continue until it has been filled
    while True:
        response = input(question)

        if response == "":
            print("Sorry this field cannot be blank. "
                  "Please try again")
        else:
            return response


def num_check(question):
    # checks if users input is an integer, tells user
    # to put one in if it is not an integer.
    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("Please enter an integer.")


def currency(x):
    # converts item to 2 decimal places with a money symbol
    return "${:.2f}".format(x)


def string_checker(question, num_letters, valid_responses):
    # checks if input matches the valid answers in a pre-made list,
    # tells user if input is invalid.
    error = "Please choose a valid input"

    while True:
        response = input(question).lower()

        for item in valid_responses:
            if response == item[:num_letters] or response == item:
                return item

        print(error)


def clean(x):
    # cleans up look of the printed lists by removing
    # ugly useless brackets
    return x.replace('[', '').replace(']', '')\
        .replace("'", '').replace(',', '')


def stringer(x):
    # converts item to a string and returns it
    return str(x)


def calc_pizza_price(var_pizza):
    # calculates the cost of a pizza based on the users
    # choice and returns value
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

# main routine starts

# lists to hold details about pizzas sold


pizza_sold_list = []
prices_list = []
topping_picked = []

# predetermined valid options for inputs and raffle 1-5 list
yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]
pizzas_list = ["cheese", "meat lovers", "pepperoni", "ham", "hawaiian"]
size_list = ["large", "small"]
topping_list = ["pineapple", "ham", "bacon", "cheese", "olives", "xxx"]
raffle = [1, 2, 3, 4, 5]
delivery_option = ["delivery", "pickup"]

pizza_order_dict = {
    "Type of Pizza": pizza_sold_list,
    "Price": prices_list,
    "Extras": topping_picked
    }
while True:
    # this predetermined variable starts the while loop
    # allowing the program to start
    another = "yes"
    # brief introduction with light instructions and early quit function
    print("\U0001f355 Hello, welcome to the pizza ordering "
          "program! \U0001f355 ")
    print()
    print("***** After typing your inputs in this program, "
          "press enter key to continue! *****")
    print()
    start_order = string_checker("Would you like to start "
                                 "your pizza order? (y/n): "
                                 "", 1, yes_no_list)
    if start_order == "no":
        print("Okay, program ending, 0 pizzas were purchased! ")
        break

    # users details are put in and validated using the not_blank
    # and num_check function
    print()
    name = not_blank("Please enter your name so we know who "
                     "the order is for: ")
    phone = num_check("Please enter your phone number in "
                      "case we need to call you (no spaces): ")
    while another == "yes":
        # user determines the want_instructions variable
        # allowing user to decide if they want to use the print menu
        # function
        want_instructions = string_checker("Do you want to read the "
                                           "instructions"
                                           " and menu {}? (y/n)"
                                           ": ".format(name),
                                           1, yes_no_list)

        if want_instructions == "yes":
            show_instructions()
    # user uses this code to determine their choice of pizza.
        print()
        print("Please remember to be specific with the "
              "pizza order, e.g. \"cheese\" ")
        which_pizza = string_checker("Which pizza do you"
                                     " want: "
                                     "", 1, pizzas_list)
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
    # calculate the pizzas price based on the selected
        # option using the calc_pizza_price function.
        pizza_cost = calc_pizza_price(which_pizza)
    # input where the only valid options are small or large
        print()
        size_choice = string_checker("Please choose from "
                                     "size small or large(+$2)"
                                     ": ", 1, size_list)
    # here is the code that determines the currently being
        # ordered pizzas size.
        if size_choice == "small":
            size = 0
            print()
            print("You have selected the size small for your "
                  "pizza (no additional cost!)")
        elif size_choice == "large":
            size = 2
            print()
            print("You have selected the size large for your "
                  "pizza ($2 dollars more)")
        else:
            size = 0
    # implicate the size choice to the price and use the
        # which topping as none to start the while loop.
        # Temp toppings list will store the current pizzas
        # potential toppings for later appending to the main list.
        pizza_cost = pizza_cost + size
        which_topping = 'none'
        temp_toppings = []

        want_toppings = string_checker("Would you like any "
                                       "toppings on your pizza? (y/n): ",
                                       1, yes_no_list)
    # loop which allows user to get as many toppings as
        # desired, users are able to exit the look if they want to by
        # using 'xxx'
        if want_toppings == "yes":
            show_toppings()
            while which_topping != 'xxx':
                which_topping = string_checker("Type in the extra "
                                               "topping do you want "
                                               "on your pizza? "
                                               "(type in \'xxx\' to "
                                               "stop ordering toppings): ",
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
        else:
            print()
            print("No toppings will be added then!")
            temp_toppings.append("None")
            pass
    # order summary of most recent pizza
        temp_list = []
        print()
        print("***************************************************\
        ****************************")
        print("You, {}, ordered a {} {} pizza with the toppings of {} "
              "for a final cost ${:.2f}".format(name, size_choice, which_pizza,
                                                temp_toppings, pizza_cost).
              replace('[', '(').replace(']', ')').replace("'", ''))
    # adding the order details to their assigned lists.
        confirm_ord = string_checker("Would you like to confirm the "
                                     "order of this pizza? (y/n):"
                                     " ", 1, yes_no_list)
        if confirm_ord == "yes":
            temp_list.append(size_choice)
            temp_list.append(which_pizza)
            pizza_sold_list.append(temp_list)
            prices_list.append(pizza_cost)
            topping_picked.append(temp_toppings)
            print("Order of this pizza confirmed! ")
        else:
            print("Order of this pizza cancelled! ")

        print()
        another = string_checker("Would you like to order another "
                                 "pizza? (y/n): ",
                                 1, yes_no_list)
    # allows the user to decide if they want to continue on with
        # the order, ect. order another pizza
        if another == "no":
            break
    if (len(prices_list)) > 0:
        # here the orders details are displayed to the user.
        print()
        print("You selected a total of {} pizzas".format(len(prices_list)))
        print("This comes to a total cost of ${:.2f}".format(sum(prices_list)))
        print()
        print("***** Order Summary *****")
        print("Current Order:               ")
        # I created this looping list function to print out the
        # orders all put the details of the order
        for i, j, z in zip(pizza_sold_list, topping_picked, prices_list):
            print(str(i).replace('[', '').replace(']', '')
                  .replace("'", ''), "pizza with the toppings of", str(j)
                  .replace("'", '').replace('[', '(')
                  .replace(']', ')'), "with a cost of $", z)
        # this code below allows the user to choose their
        # payment from either cash or credit and uses string checker to
        # validify
        print()
        print("******PAYMENT CHOICE******")
        which_pay = string_checker("Would you like to pay "
                                   "in cash or credit (%5 fee): "
                                   "", 1, payment_list)
        # calculations based on choice finalise the cost
        if which_pay == "cash":
            print("Paying with cash. Your final cost remains at ${:.2f} "
                  "".format(sum(prices_list)))
        elif which_pay == "credit":
            final_cost = sum(prices_list) * 1.05
            print("Paying with credit. Your final cost is ${:.2f}"
                  "".format(final_cost))

        print()
        # Here is the code which gives users a 20% chance of
        # winning the raffle. It works by having a random integer
        # selected
        # from 1-5 and if it is 3 the user wins.
        winner = random.choice(raffle)
        if winner == 3:
            print("Congratulations you have won a $5 mitre ten voucher!!!! ")
        else:
            print("Unfortunately you did not win the voucher prize (20% chance)")

        print("Thank you for ordering from us {}, hope to see"
              " you soon! ".format(name))
        print()
        print("****** Here is your receipt ******")
        pizza_order_frame = pandas.DataFrame(pizza_order_dict)
        # cleaning of output for the pandas data table using
        # the clean function, and currency function but first
        # converting to
        # string if required
        add_dollars = ['Price']
        for var_item in add_dollars:
            pizza_order_frame[var_item] = pizza_order_frame[var_item]\
                .apply(currency)

        add_extra = ['Extras']
        for var_item in add_extra:
            pizza_order_frame[var_item] = pizza_order_frame[var_item]\
                .apply(stringer)
        add_pizza = ['Type of Pizza']
        for var_item in add_pizza:
            pizza_order_frame[var_item] = pizza_order_frame[var_item]\
                .apply(stringer)

        add_extra = ['Extras']
        for var_item in add_extra:
            pizza_order_frame[var_item] = pizza_order_frame[var_item]\
                .apply(clean)
        add_pizza = ['Type of Pizza']
        for var_item in add_pizza:
            pizza_order_frame[var_item] = pizza_order_frame[var_item]\
                .apply(clean)
        # pandas table is printed from this as the order recept
        print(pizza_order_frame)
        print()
        # delivery choice, adds cost based on users choice
        # allows for the input of address if needed
        delivery_choice = string_checker("Pickup or delivery (+$5), {}?:"
                                         " ".format(name),
                                         1, delivery_option)
        print()
        if delivery_choice == "delivery":
            extra_cost = 5
            address = not_blank("Enter your address for delivery: ")
            print("We will deliver to {} when ready".format(address))
            print()
        elif delivery_choice == "pickup":
            extra_cost = 0
            print("We will call your number when it is time for pickup. ")
            print()
        else:
            extra_cost = 0
        # final cost displayed with the receipt
        if which_pay == "cash":
            final_cost = sum(prices_list) + extra_cost
            print("****** Payed with cash. Your final cost {}: ${:.2f}"
                  " ******".format(name, final_cost))
        elif which_pay == "credit":
            final_cost = sum(prices_list) * 1.05 + extra_cost
            print("****** Payed with credit. Your final cost {}: ${:.2f}"
                  " ******".format(name, final_cost))

    else:
        print("You ordered 0 pizzas in total")
        print("***** Come back another day! *****")

    reset_order = string_checker("Reset program for a new"
                                 " order (y/n): ".format(name),
                                 1, yes_no_list)
    # restarts program, clears relevant lists involved.
    if reset_order == "yes":
        print("Restarting...")
        pizza_sold_list.clear()
        prices_list.clear()
        topping_picked.clear()
    # program ends
    else:
        print("Program ending...")
        print("Done")
        break
