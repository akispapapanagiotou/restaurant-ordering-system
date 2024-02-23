import datetime

restaurant_menu = [
    {
        "dish": "Classic Cheeseburger",
        "description": "Beef patty, cheese, lettuce, tomato, pickles, sesame seed bun",
        "price": 9.99,
        "quantity": 50
    },
    {
        "dish": "Vegetarian Pad Thai",
        "description": "Rice noodles, tofu, bean sprouts, peanuts, tamarind sauce",
        "price": 12.99,
        "quantity": 30
    },
    {
        "dish": "Grilled Salmon",
        "description": "Atlantic salmon, steamed vegetables",
        "price": 17.99,
        "quantity": 20
    },
    {
        "dish": "Mushroom Risotto",
        "description": "Arborio rice, mushrooms, garlic, Parmesan cheese",
        "price": 14.99,
        "quantity": 25
    },
    {
        "dish": "Tiramisu",
        "description": "Coffee-soaked ladyfingers, mascarpone cheese",
        "price": 6.99,
        "quantity": 40
    },
    {
        "dish": "Mediterranean Grilled Chicken Salad",
        "description": "Grilled chicken, mixed greens, cherry tomatoes, feta cheese, olives",
        "price": 12.99,
        "quantity": 25
    },
    {
        "dish": "Spaghetti Carbonara",
        "description": "Pasta, bacon, eggs, Parmesan cheese, black pepper",
        "price": 14.99,
        "quantity": 20
    },
    {
        "dish": "Thai Basil Beef Stir-Fry",
        "description": "Beef, Thai basil, bell peppers, onions, garlic",
        "price": 15.99,
        "quantity": 18
    },
    {
        "dish": "Vegetarian Chickpea Curry",
        "description": "Chickpea curry, tomatoes, onions, Indian spices",
        "price": 13.99,
        "quantity": 22
    },
    {
        "dish": "BBQ Pulled Pork Sandwich",
        "description": "Pulled pork, barbecue sauce, coleslaw, pickles",
        "price": 11.99,
        "quantity": 30
    }
]


def greeting():
    greeting_message = ("\nWelcome to SavorSquare Bistro! Join us for a memorable dining experience where our team"
                        "\nis dedicated to exceeding your expectations. We're here to make your visit special, so"
                        "\ndon't hesitate to ask us anything. Enjoy your meal!\n")
    print(greeting_message)


def print_menu():
    lines = "-" * 90
    print(lines)
    print(" " * 35 + "SavorSquare Bistro")
    print(" " * 42 + "Menu")
    print(lines)
    for item in restaurant_menu:
        print(f"Dish: {item['dish']}")
        print(f"Description: {item['description']}")
        print(f"Price: ${item['price']}")
        print(lines)
    print("")


def take_order():
    order = []

    while True:

        # ask for dish choice
        while True:
            try:
                dish_choice = int(input("Which dish would you like to order? "
                                        "(Enter dish number 1-10)\n"))
                if 1 <= dish_choice <= 10:
                    break
                else:
                    print("Invalid dish choice!")
            except ValueError:
                print("Invalid dish choice!")

        if dish_choice == 0:
            break

        dish_name = restaurant_menu[dish_choice - 1]['dish']
        available_quantity = restaurant_menu[dish_choice - 1]['quantity']

        # ask for quantity choice
        while True:
            try:
                quantity_choice = int(input(f"How many servings of {dish_name} would you like to order? "
                                            f"(Choose 1-{available_quantity})\n"))
                if 1 <= quantity_choice <= available_quantity:
                    break
                else:
                    print("Invalid quantity choice!")
            except ValueError:
                print("Invalid quantity choice!")

        print(f"You have ordered {quantity_choice} serving(s) of {dish_name}.")
        order.append([dish_choice, quantity_choice])

        continue_order = input("Would you like to order something else? (yes/no)\n")
        if continue_order.lower() != 'yes':
            break

    return order


def calculate_total_cost(order):
    total_cost = 0
    for item in order:
        dish = item[0]
        quantity = item[1]
        price = restaurant_menu[dish-1]['price']
        total_cost += quantity * price
    return total_cost


def print_receipt(order):
    lines = "-" * 90
    print(lines)
    print(" " * 35 + "SavorSquare Bistro")
    print(" " * 41 + "Receipt")
    print(lines)
    current_datetime = datetime.datetime.now()
    print(f"Date: {current_datetime.strftime("%d/%m/%y")}")
    print(f"Time: {current_datetime.strftime("%H:%M:%S")}")
    print(lines)

    print("Dish" + " " * 35 + "Quantity" + " " * 20 + "Price")
    print(lines)
    for item in order:
        dish = item[0]
        servings = item[1]
        dish_name = restaurant_menu[dish-1]['dish']
        price = restaurant_menu[dish-1]['price']
        cost = servings * price
        print(f"{dish_name}{' ' * (40 - len(dish_name))}"
              f"{servings}{' ' * (27 - len(str(servings)))}"
              f"{cost:.2f}")
    print(lines)

    print(f"Total cost: {str(calculate_total_cost(order))}€\n")
    print("Thank you for dining with us!")


def main():
    greeting()
    print_menu()
    my_order = take_order()
    print_receipt(my_order)


main()
