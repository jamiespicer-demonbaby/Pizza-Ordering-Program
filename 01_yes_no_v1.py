# functions


# main routine
while True:
    want_instructions = input("Do you want instructions and the menu? ").lower()

    if want_instructions == "yes" or want_instructions == "y":
        print("**Instructions and menu go here (add later)**")
    elif want_instructions == "no" or want_instructions == "n":
        pass
    else:
        print("please answer with either yes / no")


