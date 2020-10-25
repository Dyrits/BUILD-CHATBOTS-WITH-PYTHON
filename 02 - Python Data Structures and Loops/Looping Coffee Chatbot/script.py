def coffee_bot():
    print("Welcome to the cafe!")
    drinks = {}
    get_a_drink(drinks)
    while get_another():
        get_a_drink(drinks)
    name = input("Can I get your name please? \n")
    print(f"Thanks, {name}! So, it will be: ")
    for drink, size in drinks.items():
        print(f"- {size} {drink}")


def get_size(invalid_selection=False):
    if invalid_selection:
        print_message()
    sizes = {
        "a": "small",
        "b": "medium",
        "c": "large"
    }
    size = sizes.get(input("What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n"))
    return size if size else get_size(True)


def get_drink_type(invalid_selection=False):
    if invalid_selection:
        print_message()
    drinks = {
        "a": "brewed coffee",
        "b": "mocha",
        "c": "latte"
    }
    drink = drinks.get(input("What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n"))
    return order_latte() if drink == "latte" else drink if drink else get_drink_type(True)


def order_latte(invalid_selection=False):
    if invalid_selection:
        print_message()
    milks = {
        "a": "latte",
        "b": "non-fat latte",
        "c": "soy latte"
    }
    milk = milks.get(input("And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n"))
    return milk if milk else order_latte(True)


def get_a_drink(drinks):
    size = get_size()
    drink = get_drink_type()
    print(f"Alright, that's a {size} {drink}!")
    drinks[drink] = size


def get_another(invalid_selection=False):
    if invalid_selection:
        print_message()
    options = {
        "Y": True,
        "YES": True,
        "YEAH": True,
        "SURE": True,
        "OF COURSE": True,
        "N": False,
        "NO": False,
        "NAH": False,
        "STOP": False,
        "BYE": False
    }
    option = options.get(input("Would you like to order another drink? (Y/N)").upper())
    return option if option is not None else (get_another(True))


def print_message():
    print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")


coffee_bot()
