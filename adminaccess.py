admin_login={"admin":"Password@123"}

Menu={1:{"Name":"Masala Papad","Price":60,"Quantity":2},
     2:{"Name":"Chilly Prawns","Price":120,"Quantity":4},
     3:{"Name":"Soup","Price":90,"Quantity":3},
     4:{"Name":"Chhole","Price":180,"Quantity":2},
     5:{"Name":"Buttter Chicken","Price":270,"Quantity":5},
     6:{"Name":"Paneer Masala","Price":240,"Quantity":4},
     7:{"Name":"Gulab Jamun","Price":50,"Quantity":2},
     8:{"Name":"Ice cream","Price":110,"Quantity":4},
     9:{"Name":"Brownie with ice cream","Price":260,"Quantity":2}}
a=len(Menu)
def add_item():
    print(Menu)
    name=input("Enter the item name you wanna add list\n")
    price=int(input("Eneter the price of item\n"))
    quantity=int(input("Enetr the quantity of item\n"))
    global a
    Menu[a+1]={"Name":name,
            "Price":price,
            "Quantity":quantity,
           }
    print(f"The {name} has been added successfully in ID {a}!")
    print(Menu)
    return Menu
#print(add_item())

def editItems():
    print(Menu)
    choose1 = int(input("Enter the Id of item you wanna edit\n"))
    if choose1 not in range(a):
        print("You have entered the wrong ID!")
    elif choose1 in range(a):
        choice1 = int(input("Do you wish to edit the \n1.Item in Menu\n2.Elements in Item\n"))
        if choice1==1:
            name2=input("Enter the updated name of item\n")
            price2=int(input("Enter the updated price of the item\n"))
            quantity2=int(input("Enter the updated quantity of the item\n"))
            Menu[choose1]["Name"]=name2
            Menu[choose1]["Price"]=price2
            Menu[choose1]["Quantity"]=quantity2
            print(f"The ID {choose1} has been successfully edited!")
        elif choice1==2:
                c=int(input("Which element you wish to edit\n1.Name\n2.Price\n3.Quantity\n"))
                if c==1:
                    x=input("Enter the updated name\n")
                    Menu[choose1]["Name"] = x
                    print(f"The Name of ID {choose1} has been successfully edited!")
                    return Menu
                if c==2:
                    y=int(input("Enter the updated Price\n"))
                    Menu[choose1]["Price"] = y
                    print(f"The Price of ID {choose1} has been successfully edited!")
                    return Menu
                if c == 2:
                    z=input("Enter the updated Quanity\n")
                    Menu[choose1]["Quantity"] = z
                    print(f"The Quantity of ID {choose1} has been successfully edited!")
                    return Menu
    print(Menu)
    return Menu
#print(editItems())

def show():
    print("Welcome to Admin Panel!")
    d = int(input("Enter the ID of item to be displayed\n"))
    if d in range(a):
        print("item Name: ", Menu[d]["Name"])
        print("item Quantity: ", Menu[d]["Quantity"])
        print("item Price: ", Menu[d]["Price"])
    return (f"The Menu for Item ID {d} is displayed above")
    print(Menu)
#print(show())

def delete():
    while True:
        d = int(input("Enter the Id of element to be deleted\n"))
        q = len(Menu)
        if d in range(q):
            del (Menu[d])
            print(Menu)
        for key, value in list(Menu.items()):
            if key > d:
                Menu[key-1] = value
                del Menu[key]
        print(Menu)
        delMore=(input("Do you wish delete any more elements Y/N?\n")).lower()
        if delMore=="y":
            pass
        elif delMore=="n":
            break
        else:
            print("Invalid Input!!")
    print(Menu)
#print(delete())

def stock():
    print(Menu)
    for i in Menu:
        e=int(input("Enter the ID of Item you wish to update Stock\n"))
        c=(Menu[e]["Quantity"])
        if e in range(a):
            d=int(input("Enter the updated Stock Value\n"))
            Menu[e]["Quantity"]=d
            print(Menu[e])
            print(f"The quantity of Item ID {e} updated suceessfully!")
            r=(c-Menu[e]["Quantity"])
            return(f"The available stock of Item Id {e} are {r}")
    print(Menu)
#print(stock())

def discount():
        r=int(input("Enter the Item ID you wish to apply discount on\n"))
        e=Menu[r]["Price"]
        q=int(input("Enter the Percentage of Discount you wish to provide\n"))
        c=(q/100)*e
        print(c)
        d=e-c
        Menu[r]["Price"]=d
        print(d)
        print(f"The amount {e} after updating discount is {d}!")
        print(Menu[r])
        print (Menu)
#print(discount())
