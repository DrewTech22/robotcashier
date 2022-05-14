#Robot Store cashier

from tkinter.messagebox import YES


print("Welcome to Csquare Creations LLC!")

name = input("What is your name?\n")

print("Hello " + name + ", Thank you for choosing us use to provide you services!")

print(name + ", What could I possible sell you today?")


menu = "Laptop, Phone, TV?"

print(menu)

order = input()

price = 10

quantity = input("How many orders do you want?\n")

total = price * int(quantity)
print(total)

print("Thank you! The total amount will be $" + str(total) + " dollars")

print(input("Is that amount ok?\n"))
if YES:
        print("Sounds good " + name + " your " + order + " is coming soon!")
else:
        print("Sorry " + name + " but I can not work for you.")



