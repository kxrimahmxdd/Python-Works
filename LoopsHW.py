muffins = 10
cupcakes = 10

while True:
    purchase = input("Enter 'muffin' to buy a muffin, 'cupcake' to buy a cupcake, or '0' to stop: ")
    
    if purchase == "0":
        print(f"muffins: {muffins} cupcakes: {cupcakes}")
        break
    elif purchase == "muffin":
        if muffins > 0:
            muffins -= 1
        else:
            print("Out of stock")
    elif purchase == "cupcake":
        if cupcakes > 0:
            cupcakes -= 1
        else:
            print("Out of stock")
    else:
        print("Invalid input, please enter 'muffin', 'cupcake', or '0'.")