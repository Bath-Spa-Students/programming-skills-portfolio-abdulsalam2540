#hot drinks menu
hot_drinks = [
    {'item_code':'H1',
    'item_name':'Cappuccino ☕',
    'item_stock':10,
    'item_price':10}
    ,
    {'item_code':'H2',
    'item_name':'Turkish coffee ☕',
    'item_stock':10,
    'item_price':10}
    ,

    {'item_code':'H3',
    'item_name':'Mocha ☕',
    'item_stock':6,
    'item_price':9}
    ,
    {'item_code':'H4',
    'item_name':'Caramel Macchiato ☕',
    'item_stock':7,
    'item_price':15}
    ,
    {'item_code':'H5',
    'item_name':'Hot Chocolate ☕',
    'item_stock':10,
    'item_price':10}
    ]
#teas menu
teas = [
    {'item_code':'T1',
    'item_name':'Chai 🍵',
    'item_stock':10,
    'item_price':1}
    ,
    {'item_code':'T2',
    'item_name':'Green Tea 🍵',
    'item_stock':8,
    'item_price':5}
    ,
    {'item_code':'T3',
    'item_name':'Saffron Tea 🍵',
    'item_stock':9,
    'item_price':5}
    ,
    {'item_code':'T4',
    'item_name':'Hibiscus Tea 🍵🌺',
    'item_stock':5,
    'item_price':4}
    ,
    {'item_code':'T5',
    'item_name':'Black Tea 🍵',
    'item_stock':8,
    'item_price':6}
    ,
    {'item_code':'T6',
    'item_name':'Chamomile Tea 🍵🌼',
    'item_stock':8,
    'item_price':8}
    ,
    {'item_code':'T7',
    'item_name':'Peach Iced Tea 🍑🧋',
    'item_stock':5,
    'item_price':10}
    ,
    {'item_code':'T8',
    'item_name':'Raspberry Iced Tea 🍓🧋',
    'item_stock':5,
    'item_price':10}
]
#snacks menu
snacks = [
    {'item_code':'S1',
    'item_name':'Bugles Cheese Chips 🫓',
    'item_stock':10,
    'item_price':6}
    ,
    {'item_code':'S2',
    'item_name':'Finns Chilli Chips 🌶️🫓',
    'item_stock':5,
    'item_price':5}
    ,
    {'item_code':'S3',
    'item_name':'Pringles Salty Chips (small size) 🫓',
    'item_stock':5,
    'item_price':5}
    ,
    {'item_code':'S4',
    'item_name':'Pringles Salty Chips (large size) 🫓',
    'item_stock':5,
    'item_price':5}
    ,
    {'item_code':'S5',
    'item_name':'Chocolate Chip Cookie 🍪',
    'item_stock':7,
    'item_price':6}
    ,
    {'item_code':'S6',
    'item_name':'Popcorn 🍿',
    'item_stock':7,
    'item_price':7}
    ,
    {'item_code':'S7',
    'item_name':'Tiffany Glucose Biscuits 🥮',
    'item_stock':7,
    'item_price':5}
]
#list = ["a","b","c","d","e","f"]
#for letters in list:
#    print(letters)
#for printing out item name, price, stock and code in each category
def menu():
    print("-----------------------------Please grab the food that you like-----------------------------")

    print("----------------------------- HOT DRINKS : -----------------------------")

    for item_data in hot_drinks:
        print(f"{item_data['item_code']}\t{item_data['item_name']}\titem stock:{item_data['item_stock']}\titem price:{item_data['item_price']}")

    print("----------------------------- TEAS: -----------------------------")

    for item_data in teas:
        print(f"{item_data['item_code']}\t{item_data['item_name']}\titem stock:{item_data['item_stock']}\titem price:{item_data['item_price']}")

    print("----------------------------- SNACKS: -----------------------------")
    for item_data in snacks:
        print(f"{item_data['item_code']}\t{item_data['item_name']}\titem stock:{item_data['item_stock']}\titem price:{item_data['item_price']}")
menu()

#user input
user_money = int(input("ENTER MONEY: "))
print(f"You have entered {user_money} dhs")
user_choice = str(input("ENTER ITEM CODE: "))

#if the user inputs the wrong format for item code, ask them to try again
#hot drinks
if user_choice == "h1":
    print("Invalid input, please try again !")
    menu()
if user_choice == "h2":
    print("Invalid input, please try again !")
    menu()
if user_choice == "h3":
    print("Invalid input, please try again !")
    menu()
if user_choice == "h4":
    print("Invalid input, please try again !")
    menu()
if user_choice == "h5":
    print("Invalid input, please try again !")
    menu()

#teas
if user_choice == "t1":
    print("Invalid input, please try again !")
    menu()
if user_choice == "t2":
    print("Invalid input, please try again !")
    menu()
if user_choice == "t3":
    print("Invalid input, please try again !")
    menu()
if user_choice == "t4":
    print("Invalid input, please try again !")
    menu()
if user_choice == "t5":
    print("Invalid input, please try again !")
    menu()
if user_choice == "t6":
    print("Invalid input, please try again !")
    menu()
if user_choice == "t7":
    print("Invalid input, please try again !")
    menu()
if user_choice == "t8":
    print("Invalid input, please try again !")
    menu()
#snacks
if user_choice == "s1":
    print("Invalid input, please try again !")
    menu()
if user_choice == "s2":
    print("Invalid input, please try again !")
    menu()
if user_choice == "s3":
    print("Invalid input, please try again !")
    menu()
if user_choice == "s4":
    print("Invalid input, please try again !")
    menu()
if user_choice == "s5":
    print("Invalid input, please try again !")
    menu()
if user_choice == "s6":
    print("Invalid input, please try again !")
    menu()
if user_choice == "s7":
    print("Invalid input, please try again !")
    menu()

#for detecting user choice and matching it with present item data in hot drinks 
def item_choice_hot_drinks():
    for item_data in hot_drinks:
        item_code = item_data['item_code']
        while user_choice in item_code:
            item_name = item_data['item_name']
            print(f"{item_name}  has been dispensed")
            item_price= item_data["item_price"]
            change_money = user_money-item_price
            print(f"You recieved {change_money} dhs back")
            break

#for detecting user choice and matching it with present item data in teas 
def item_choice_teas():
    for item_data in teas:
        item_code = item_data['item_code']
        while user_choice in item_code:
            item_name = item_data['item_name']
            print(f"{item_name}  has been dispensed")
            item_price= item_data["item_price"]
            change_money = user_money-item_price
            print(f"You recieved {change_money} dhs back")
            break

#for detecting user choice and matching it with present item data in snacks 
def item_choice_snacks():
    for item_data in snacks:
        item_code = item_data['item_code']
        while user_choice in item_code:
            item_name = item_data['item_name']
            print(f"{item_name}  has been dispensed")
            item_price= item_data["item_price"]
            change_money = user_money-item_price
            print(f"You recieved {change_money} dhs back")
            break
item_choice_hot_drinks()
item_choice_snacks()
item_choice_teas()

#recommendations list : hot drinks
if user_choice == "H1":
    print("Cappuccino goes well with Chocolate Chip Cookie, would you like to buy a Chocolate Chip Cookie?")
if user_choice == "H2":
    print("Turkish Coffee goes well with Tiffany Glucose Biscuits, would you like to buy Tiffany Glucose Biscuits?")
if user_choice == "H3":
    print("Mocha goes well with Pringles Salty Chips (small size), would you like to buy Pringles Salty Chips (small size)?")
if user_choice == "H4":
    print("Caramel Macchiato goes well with Chocolate Chip Cookie, would you like to buy Chocolate Chip Cookie?")
if user_choice == "H5":
    print("Hot Chocolate goes well with Chocolate Chip Cookie, would you like to buy Chocolate Chip Cookie?")

#recommendations list : teas 
if user_choice == "T1":
    print("Chai goes well with Tiffany Glucose Biscuits, would you like to buy Tiffany Glucose Biscuits?")
if user_choice == "T2":
    print("Green Tea goes well with Caramel Macchiato, would you like to buy Caramel Macchiato?")
if user_choice == "T3":
    print("Saffron Tea goes well with Pringles Salty Chips (small size), would you like to buy Pringles Salty Chips (small size)?")
if user_choice == "T4":
    print("Hibiscus Tea goes well with Tiffany Glucose Biscuits, would you like to buy Tiffany Glucose Biscuits?")
if user_choice == "T5":
    print("Black Tea goes well with Chocolate Chip Cookie, would you like to buy a Chocolate Chip Cookie?")
if user_choice == "T6":
    print("Chamomile Tea goes well with Tiffany Glucose Biscuits, would you like to buy Tiffany Glucose Biscuits?")
if user_choice == "T7":
    print("Peach Iced Tea goes well with Tiffany Glucose Biscuits, would you like to buy Tiffany Glucose Biscuits?")
if user_choice == "T8":
    print("Raspberry Iced Tea goes well with Pringles Salty Chips (small size), would you like to buy Pringles Salty Chips (small size)?")

#asking the user if they want to buy more items 
more_items = input("Would you like more items with that? (Yes/No): ")
#printing out menu if user input = yes
if more_items  == "Yes":
    menu()
    user_choice = str(input("Enter item code: "))
    item_choice_hot_drinks()
    item_choice_snacks()
    item_choice_teas()

if more_items  == "yes":
    menu()
    user_choice = str(input("Enter item code: "))
    item_choice_hot_drinks()
    item_choice_snacks()
    item_choice_teas()

if more_items == "No":
    print("Thank you for buying ! 🌸")

if more_items == "no":
    print("Thank you for buying ! 🌸")
