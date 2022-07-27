import adminaccess as ad
class user():
    users={}
    def __init__(self,name,age,phone,email,address,username,password):
        self.name=name
        self.age=age
        self.phone=phone
        self.email=email
        self.address=address
        self.username=username
        self.password=password
        user.users[self.phone]={"Email":self.email,
                                "Full_Name":self.name,
                                "Phone":self.phone,
                                "Age":self.age,
                                "Address":self.address,
                                "Username":self.username,
                                "Password":self.password
                                }
        k = []

        def addorder():
            print(ad.Menu)
            choice = int(input("Do you wish to continue with order\n1.Yes\n2.No\n"))
            if choice == 1:
                d = int(input("How many items do you wish to order?\n"))
                total = 0
                for i in range(d):
                    l = []
                    itemid = int(input("Enter the Id of item you wish to order\n"))
                    quantity = int(input("Enter the quanitity of item you wish to order\n"))
                    e = ad.Menu[itemid]
                    z = ad.Menu[itemid]
                    k.append(z)
                    l.append(e)
                    total += ad.Menu[itemid]["Price"] * quantity
                    print(k)
                    print(total)
                q = int(input("Do you have any Discount Coupon\n1.Yes\n2.No\n"))
                if q == 1:
                    w = input("Enter the Coupon Code!\n")
                    a = "DISCOUNT10"
                    if w == a:
                        discount = (10 / 100) * total
                        discount10 = total - discount
                        print(f"Your total of {total} after applying discount is {discount10}!")
                        print(discount10)
                        confirm = int(input("Do you wish to confirm the order \n1.Yes\n2.No\n"))
                        if confirm == 1:
                            print(f"Your order of {l} of INR {discount10} has beem Successfully placed!")
                            return ("Thank you for placing your order!!")
                        elif confirm == 2:
                            print("The order has been cancelled!")
                            print(l)
                            del (l)
                            return ("Cart is Empty! Continue Ordering!")
                        else:
                            print("Invalid input")
                    else:
                        print("Invalid Input")
                elif q == 2:
                    print("Continue without discount")
                    print(l)
                    print(total)
                    final = int(input("Do you wish to place the order?\n1.Yes\n2.No\n"))
                    if final == 1:
                        return ("Thank you for placing your order!!")
                    elif final == 2:
                        print("The order has been cancelled!")
                        print(l)
                        del (l)
                        return ("Cart is Empty! Continue Ordering!")
                    else:
                        print("Invalid Input!")
                else:
                    print("Invalid input")
            elif choice == 2:
                print("You have exited the Menu")
                exit()
            else:
                print("Invalid input!!")
        def history(self):
            print(k)

        def profile(self):
            phone=input("Enter your phone: ")
            if phone in user.users.keys():
                print("You can Edit your profile!!")
                del user.users[phone]

                nphone = int(input("Enter your Phone: "))
                nemail = input("Enter your Email: ")
                nname = input("Enter your Name: ")
                nage= int(input("Enter your age: "))
                naddress = input("Enter your Address: ")
                nusername=input("Enter your username: ")
                npassword = input("Enter your  Password: ")

                user.users[self.phone] = {"Email": nemail,
                                          "Full_Name": nname,
                                          "Phone": nphone,
                                          "Age": nage,
                                          "Address": naddress,
                                          "Username": nusername,
                                          "Password": npassword
                                          }
                print(user.users[self.phone])
                print("Profile has been updated")
            else:
                print("Invalid Credentials!!")

        @classmethod
        def login(cls,phone,password):
            if phone in cls.users.keys():
                if cls.users.get(phone)["Password"]==password:
                    print(f"{cls.users.get(phone)[name]} logged in successfully!!")
                    return True
                else:
                    print("Invalid Credentials!!")
                    return False
            else:
                print(f"{phone} not registered!!")
                return False

#to be ignored!!
# obj=user('abc',21,123, 'abc@gamil.com' , 's-198', 'abc12',"abc@123")
# user.users(obj)
#
#
# def check_user(self, phone, password):
#     if phone in user.users.keys():
#         if user.users[phone]['Password'] == password:
#             print("Now...  You are Loggedin  ")
#         else:
#             print("Password does not Matched")
#     else:
#         print(f"{phone} Not Registered Yet.. First Register then Come Again !!!!! ")
# print(check_user())