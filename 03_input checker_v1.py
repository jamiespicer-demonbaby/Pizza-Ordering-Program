# functions or list
def string_checker(question, num_letters, valid_responses):

    error = "Please choose a valid input"

    while True:
        response = input(question).lower()

        for item in valid_responses:
            if response == item[:num_letters] or response == item:
                return item

        print(error)


pizzas_list = ["cheese", "ham", "pepperoni"]

# routine
string_checker("Which pizza do you want: ", 1, pizzas_list)

print("A correct input was put in! ")
