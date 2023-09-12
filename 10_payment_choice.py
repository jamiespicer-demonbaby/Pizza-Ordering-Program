# functions
def string_checker(question, num_letters, valid_responses):

    error = "Please choose a valid input"

    while True:
        response = input(question).lower()

        for item in valid_responses:
            if response == item[:num_letters] or response == item:
                return item

        print(error)


payment_list = ["cash", "credit"]

# main program

final_cost = 100

which_pay = string_checker("Would you like to pay in cash or credit (%5 fee): ", 1, payment_list)

if which_pay == "cash":
    print("Paying with cash. Your final cost remains at ${:.2f} ".format(final_cost))
elif which_pay == "credit":
    final_cost = final_cost * 1.05
    print("Paying with credit. Your final cost is ${:.2f}".format(final_cost))
