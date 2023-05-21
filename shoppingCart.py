# define products as list of dictionary
products = [
    {
        "name": "Product A",
        "price": 20
    },
    {
        "name": "Product B",
        "price": 40
    },
    {
        "name": "Product C",
        "price": 50
    }
]

# define cart as list of objects
cart = []

# collect purchase and gift wrap
for product in products:
    purchasedQuantity = 0
    try:
        purchasedQuantity = int(input("Please enter the purchased quantity of " + product['name']) or 0)
    except:
        pass
    purchasedItem = {"name": product['name'], "quantity": purchasedQuantity}
    gitWrapRequired = input("Do you wish to gift wrap" + product['name'] + " Yes/No") or "No"
    purchasedItem["giftWrap"] = True if gitWrapRequired.lower() == "yes" else False
    cart.append(purchasedItem)

print(cart)