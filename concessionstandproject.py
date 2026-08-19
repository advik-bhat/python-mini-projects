print("WELCOME TO OUR CONCESSION STAND")

menu = {
    "Popcorn": 500,
    "Soda": 250,
    "Water": 100,
    "Nachos": 400,
    "Pizza": 550,
    "Garlic Bread": 300,
    "Burger": 400,
    "French Fries": 200,
    "Chips": 50
}

order = {}
total = 0

running = True

while running:

    pick = input("enter your food choice: ").title()

    if pick in menu:
        price = menu[pick]

        # If item already exists, increase its quantity
        if pick in order:
            order[pick] += 1
        else:
            order[pick] = 1

        total += price

    else:
        print("Item doesn't exist, pick again")
        continue

    f = 0
    while f == 0:
        ask = input("more? (y or n): ")
        if ask.lower() == "n":
            running = False
            break
        elif ask.lower() == "y":
            f = 1
        else:
            print("Huh, Try Again")


print("----------YOUR ORDER--------------")
for item, quantity in order.items():
    price = menu[item]
    print(f"{item} ({quantity}) : {price * quantity}")

print("\nTotal : ", total)