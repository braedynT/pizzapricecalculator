print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
cost = 0 
if size == "S":
    if add_pepperoni == "Y":
        cost = 17
    else:
        cost = 15
elif size == "M":
    if add_pepperoni == "Y":
        cost = 23
    else:
        cost = 20
else:
    if add_pepperoni == "Y":
        cost = 28
    else:
        cost = 25
if extra_cheese == "Y":
    cost = cost + 1
print(f"Your final bill is: ${cost}.")