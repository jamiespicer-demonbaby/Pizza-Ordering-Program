# functions
def num_check(question):

    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("Please enter an integer.")

# main routine


phone = num_check("Please enter your phone number in case we need to call you: ")

