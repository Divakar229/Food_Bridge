FOOD_TYPE_MAPPING = {
    "cooked_item": [
        "rice", "chapati", "idli", "dosa", "pulao", "sambar", "dal",
        "roti", "paratha", "upma", "poha", "curry", "biryani", "khichdi",
        "paneer", "chicken curry", "fish curry", "egg curry"
    ],
    "snack_packet": [
        "chips", "biscuits", "namkeen", "cookies", "popcorn", "chocolate",
        "cracker", "wafer", "peanuts", "trail mix"
    ],
    "fruit": [
        "apple", "banana", "orange", "mango", "grapes", "watermelon",
        "pineapple", "papaya", "kiwi", "strawberry", "pear", "pomegranate"
    ],
    "meal_box": [
        "tiffin", "lunch box", "meal", "combo meal", "packed meal",
        "bento box", "thali", "plate"
    ],
    "fast_food": [
        "sandwich", "pizza", "burger", "pasta", "noodles", "hotdog",
        "wrap", "roll", "fries", "samosa", "spring roll"
    ],
    "beverages": [
        "tea", "coffee", "juice", "milkshake", "smoothie", "soft drink",
        "coconut water", "lemonade"
    ],
    "dessert": [
        "cake", "ice cream", "brownie", "pastry", "gulab jamun",
        "rasgulla", "kheer", "pudding", "donut", "cupcake"
    ]
}

POINTS_PER_UNIT = {
    "cooked_item": 2,
    "snack_packet": 1,
    "fruit": 1,
    "meal_box": 3,
    "fast_food": 2,
    "beverages": 1,
    "dessert": 2,
    "other": 1
}

def calculate_points(item_name: str, quantity: int) -> int:
    food_type = get_food_type(item_name)
    return POINTS_PER_UNIT.get(food_type, 0) * quantity

def get_food_type(item_name: str) -> str:
    item_name = item_name.lower()
    for food_type, items in FOOD_TYPE_MAPPING.items():
        for i in items:
            if i in item_name:  # partial match to cover "veg pizza", "cheese sandwich"
                return food_type
    return "other"



