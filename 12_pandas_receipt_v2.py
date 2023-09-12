import pandas


# functions
def currency(x):
    return "${:.2f}".format(x)


def clean(x):
    return x.replace('[', '').replace(']', '')


PIZZA_SOLD_LIST = ["[small, cheese]", "[large, pepperoni]", "[large pepperoni]", "[small, ham]"]
PRICES_LIST = [7.50, 12.00, 13.00, 9.00]
TOPPING_PICKED = ["[None]", "[olives, olives]", "[ham, bacon, olives]", "[pineapple]"]

pizza_order_dict = {
    "Type of Pizza": PIZZA_SOLD_LIST,
    "Price": PRICES_LIST,
    "Extras": TOPPING_PICKED
    }

pizza_order_frame = pandas.DataFrame(pizza_order_dict)

add_dollars = ['Price']
for var_item in add_dollars:
    pizza_order_frame[var_item] = pizza_order_frame[var_item].apply(currency)

add_extra = ['Extras']
for var_item in add_extra:
    pizza_order_frame[var_item] = pizza_order_frame[var_item].apply(clean)

add_pizza = ['Type of Pizza']
for var_item in add_pizza:
    pizza_order_frame[var_item] = pizza_order_frame[var_item].apply(clean)

print(pizza_order_frame)
