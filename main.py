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
