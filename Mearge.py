import adminaccess as aa
from User import user as us
user=us(str,str,str,str,str,str,str)
a=int(input("Do you wish to log in as\n1.Admin\n2.User\n3.Exit\n"))
if a==1:
    Username=input("Enter the Username: ").lower()
    Password=input("Enter the Password: ")
    if aa.admin_login[Username]==Password:
        print("You have logged in Successfully!")
        admin=True
        while admin:
            b=int(input("Enter your preferred choice\n1.Add new Item\n2.Edit Item\n3.Edit the element in Item\n4.Delete an Item\n5.Display the Itemm\n6.Update Stock\n7.Update discount\n8.Exit Menu\n"))
            if b==1:
                aa.add_item()
            elif b==2:
                aa.editItems()
            elif b==3:
                aa.editItems()
            elif b==4:
                aa.delete()
            elif b==5:
                aa.show()
            elif b==6:
                aa.stock()
            elif b==7:
                aa.discount()
            elif b==8:
                exit()
            else:
                print("Invalid Input!!")
    else:
        print("Invalid Credentials!!")
elif a==2:
    print("Welcome to the user Panel!")
    userchoose=int(input("Do you wish to \n1.Log in\n2.Register\n"))
    if userchoose==1:
        user=input("Enter your username\n")
        passwrd= input("Enter your password\n")
        if us.users(user,passwrd):
            print(f"You have successfully logged in {user}!")
            users=True
            while users:
                userchoice=(int(input(f"{user} what do wish to \n1.Place a new order\n2.Order History\n3.Update profile\n4.Exit\n")))
                if userchoice==1:
                    us.addorder()
                elif userchoice==2:
                    us.history()
                elif userchoice==3:
                    us.profile()
                elif userchoice==4:
                    print("You have exited the Menu!")
                    exit()
                else:
                    print("Invalid choice!")
    elif userchoose==2:
        nphone=int(input("Enter new phone: "))
        if nphone in us.users.keys():
            print("Already exists!")
        else:
            print("Enter the details in following: ")
            nname=input("Enter your name: ")
            nphone=int(input("Enter your phone number: "))
            nemail=input("Enter your email: ")
            nage=int(input("Enter your current age: "))
            naddress=input("Enter your address: ")
            nusername=input("Enter your username: ")
            npassword=input("Enter new password: ")
            user=us(nname,nphone,nemail,nage,naddress,nusername,npassword)
            print("You have registered Successfully!!")

    else:
        print("Invalid Credentials!!")
else:
    exit()