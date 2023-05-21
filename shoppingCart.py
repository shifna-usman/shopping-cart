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

#common offers applied

totalCartValueDiscount = {"available": True, "name": "flat_10_discount", "limit": 200, "type": "flat", "discount": 10}
totalQuantityDiscount = {"available": True, "name": "bulk_10_discount", "limit": 20, "type": "percent", "discount": 10}

# define cart as list of objects
cart = []
totalPurchaseQuantity = 0
totalCartValue = 0
giftWrapChargePerUnit = 1
shippingFeePerPackage = 5
shippingUnitsPerPackage = 10
totalGiftWrapCost = 0
totalShippingCharge = 0
discountApplied = ""
discountValue = 0

# collect purchase and gift wrap
for product in products:
    purchasedQuantity = 0
    try:
        purchasedQuantity = int(input("Please enter the purchased quantity of " + product['name'] + "\n") or 0)
    except:
        pass
    totalPurchaseQuantity += purchasedQuantity
    totalCartValue += purchasedQuantity * product['price']
    purchasedItem = {"name": product['name'], "quantity": purchasedQuantity, "totalPrice": purchasedQuantity * product['price']}
    gitWrapRequired = input("Do you wish to gift wrap " + product['name'] + " Yes/No\n") or "No"
    purchasedItem["giftWrap"] = True if gitWrapRequired.lower() == "yes" else False
    cart.append(purchasedItem)

#check total cart value to apply flat_10_discount
if totalCartValueDiscount and totalCartValueDiscount["available"] and totalCartValue > totalCartValueDiscount["limit"]:
    discountApplied = totalCartValueDiscount["name"]
    discountValue = totalCartValueDiscount["discount"] if totalCartValueDiscount["type"] == "flat" else int(totalCartValue * (totalCartValueDiscount["discount"]/100))


#check total purchase quantity to apply bulk_10_discount
if totalQuantityDiscount and totalQuantityDiscount["available"] and totalPurchaseQuantity > totalQuantityDiscount["limit"]:
    possibleDiscount = totalQuantityDiscount["discount"] if totalQuantityDiscount["type"] == "flat" else int(totalCartValue * (totalQuantityDiscount["discount"]/100))
    if possibleDiscount > discountValue:
        discountApplied = totalQuantityDiscount["name"]
        discountValue = possibleDiscount

print("totalCartValue",totalCartValue)
print("totalPurchaseQuantity", totalPurchaseQuantity)
print("discountApplied", discountApplied)
print("discountValue", discountValue)




