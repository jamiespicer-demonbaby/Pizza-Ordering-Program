# checks user response is not blank
def not_blank(question):

    while True:
        response = input(question)

        if response == "":
            print("Sorry this can't be blank. Please try again")
        else:
            return response


# main routine goes here
while True:
    name = not_blank("Enter pizza your pizza order (or 'xxx' to quit) ")
    if name == 'xxx':
        break

print("we are done")