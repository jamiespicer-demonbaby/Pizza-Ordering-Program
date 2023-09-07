# functions

def string_checker(question, num_letters, valid_responses):

    error = "Please choose a valid input"

    while True:
        response = input(question).lower()

        for item in valid_responses:
            if response == item[:num_letters] or response == item:
                return item

        print(error)


size_list = ["large", "small"]

# base component
size_choice = string_checker("Please choose from size small or large(+$2): ", 1, size_list)
# here is the code that determines the currently being ordered pizzas size.
if size_choice == "small":
    size = 0
    print()
    print("You have selected the size small for your pizza (no additional cost!)")
elif size_choice == "large":
    size = 2
    print()
    print("You have selected the size large for your pizza ($2 dollars more)")
else:
    size = 0


print("You selected a size {} for an extra cost of ${:.2f}".format(size_choice, size))
