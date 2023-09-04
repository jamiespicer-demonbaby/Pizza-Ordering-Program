# functions
def string_checker(question, num_letters, valid_responses):

    error = "Please choose a valid input"

    while True:
        response = input(question).lower()

        for item in valid_responses:
            if response == item[:num_letters] or response == item:
                return item

        print(error)


def show_instructions():
    print('''\n
***** Instructions *****

For each pizza order...
- Type the name of the pizza into the input box.
- !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
- Payment method (cash / credit)

When you have entered all the pizzas, press 'xxx' to finalise order.

The program will then display the pizzas details
including the cost of each pizza, the total cost
and the total profit.

A raffle will also be entered for the user which will allow them to have a 20% chance of winning for each order.

This information will automatically written to a text file.

***** Menu *****

Please select which pizza you would like to order by typing it's name:
1. Cheese $7.50
2. Meat lovers $9.00
3. Pepperoni $8.00
4. Ham $8.00
5. Hawaiian $8.50

At the end of an order there is a 20% chance to win a mitre ten gift voucher

***************************''')


yes_no_list = ["yes", "no"]

# main routine

want_instructions = string_checker("Do you want to read the "
                                   "instructions and menu (y/n): ",
                                   1, yes_no_list)

if want_instructions == "yes":
    show_instructions()
