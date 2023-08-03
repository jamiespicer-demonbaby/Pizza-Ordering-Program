# functions
def yes_no(question):

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Incorrect input. Please enter yes or no")


# main routine
while True:
    want_instructions = yes_no("Do you want instructions and the menu? ")

    if want_instructions == "yes":
        print("**Instructions and menu go here (add later)**")
        print()
    elif want_instructions == "no":
        print("program continues...")
        print()
