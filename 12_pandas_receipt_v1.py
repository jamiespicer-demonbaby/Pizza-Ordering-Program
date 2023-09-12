import pandas
PIZZA_SOLD_LIST = ["[small, cheese]", "[large, pepperoni]", "[large pepperoni]", "[small, ham]"]
PRICES_LIST = [7.50, 12.00, 13.00, 9.00]
TOPPING_PICKED = ["[None]", "[olives, olives]", "[ham, bacon, olives]", "[pineapple]"]

pizza_order_dict = {
    "Type of Pizza": PIZZA_SOLD_LIST,
    "Price": PRICES_LIST,
    "Extras": TOPPING_PICKED
    }

pizza_order_frame = pandas.DataFrame(pizza_order_dict)


print(pizza_order_frame)
