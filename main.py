restaurant_menu = [
    {
        "dish": "Classic Cheeseburger",
        "description": "Juicy beef patty with melted cheese, lettuce, tomato, and pickles on a sesame seed bun",
        "price": 9.99,
        "quantity": 50
    },
    {
        "dish": "Vegetarian Pad Thai",
        "description": "Stir-fried rice noodles with tofu, bean sprouts, peanuts, and tamarind sauce",
        "price": 12.99,
        "quantity": 30
    },
    {
        "dish": "Grilled Salmon",
        "description": "Fresh Atlantic salmon fillet grilled to perfection and served with steamed vegetables",
        "price": 17.99,
        "quantity": 20
    },
    {
        "dish": "Mushroom Risotto",
        "description": "Creamy Arborio rice cooked with mushrooms, garlic, and Parmesan cheese",
        "price": 14.99,
        "quantity": 25
    },
    {
        "dish": "Tiramisu",
        "description": "Classic Italian dessert made with layers of coffee-soaked ladyfingers and mascarpone cheese",
        "price": 6.99,
        "quantity": 40
    },
    {
        "dish": "Mediterranean Grilled Chicken Salad",
        "description": "Grilled chicken salad with mixed greens, cherry tomatoes, feta cheese, olives, and "
                       "lemon vinaigrette.",
        "price": 12.99,
        "quantity": 25
    },
    {
        "dish": "Spaghetti Carbonara",
        "description": "Pasta with bacon, eggs, Parmesan cheese, and black pepper.",
        "price": 14.99,
        "quantity": 20
    },
    {
        "dish": "Thai Basil Beef Stir-Fry",
        "description": "Beef stir-fry with Thai basil, bell peppers, onions, and garlic.",
        "price": 15.99,
        "quantity": 18
    },
    {
        "dish": "Vegetarian Chickpea Curry",
        "description": "Chickpea curry with tomatoes, onions, garlic, and Indian spices.",
        "price": 13.99,
        "quantity": 22
    },
    {
        "dish": "BBQ Pulled Pork Sandwich",
        "description": "Pulled pork sandwich with barbecue sauce, coleslaw, and pickles.",
        "price": 11.99,
        "quantity": 30
    }
]


def greeting():
    greeting_message = ("\nWelcome to SavorSquare Bistro!\nWe're delighted to have you dine with us today. Our team is "
                        "here to ensure you have a fantastic culinary experience.\nPlease feel free to ask any "
                        "questions or let us know how we can make your visit memorable.\nBon appétit!\n")
    print(greeting_message)


def print_menu():
    lines = "--------------------------------------------------------------------------------------------------------"
    print(lines)
    print("------------------------------------------------- MENU -------------------------------------------------")
    print(lines)
    for item in restaurant_menu:
        print(f"Dish: {item['dish']}")
        print(f"Description: {item['description']}")
        print(f"Price: ${item['price']}")
        print(lines)
    print(lines)
    print(lines)


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
