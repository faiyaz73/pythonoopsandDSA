items = []
def add(**data):
    items.append(data)
    print(data["name"], "Item added successfully! \n")
    
def view():
    for i in range(len(items)):
        print(f"{i+1} name : {items[i]["name"]} price : {items[i]["price"]} quantity : {items[i]["quantity"]}")
while True:
    choose = input("""
                   1. Add item 
                   2. Update item
                   3. Remove item
                   4. View items
                   5. search by name
                   6. calculate total price
                   7  . Exit
                   """)
    if  choose == "1":
        product_name = input("Enter product name: ")
        product_price = float(input("Enter product price: "))
        product_quantity = int(input("Enter product quantity: "))
        add(name=product_name, price=product_price, quantity=product_quantity)
        
        
        
    elif choose == "2":
        pass
    elif choose == "3":
        pass
    elif choose == "4":
        view()
    elif choose == "5":
        pass
    elif choose == "6":
        pass
    elif choose == "7":
        break
    else:
        print("Invalid choice. Please try again.......")
        break
    
