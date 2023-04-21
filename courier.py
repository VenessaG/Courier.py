# Courier

# Ask user for inputs and create variables to store inputs
price_input = float(input("Enter the purchase amount: "))
price = price_input
distance_input = float(input("Enter the distance for delivery: "))
distance = distance_input
# Add variables for prices of items
air = 0.26
freight = 0.25
full = 50.00
limited = 25.00
gift = 50.00
no_gift = 0
priority = 100.00
standard = 20.00

# Ask user for inputs to calculate the costs
delivery_method = input("Choose a delivery method: Air or Freight: ")

# Calculate between the two options from user, multiply the option with the distance from user input
if delivery_method == air:
     del_cost = air * distance
else:
    del_cost = freight * distance

# Get input from user and store value to new variable ins_cost with value from given variable full/limited
ins_choice = input("Select between insurance: Full or Limited: ")

if ins_choice == full:
    ins_cost = full
else:
    ins_cost = limited

# Get input from user and store value to new variable gift_cost with value from given variable gift/no_gift
gift_choice = input("Gift or No Gift?: ")

if gift_choice == gift:
    gift_cost = gift
else:
    gift_cost = no_gift

# Get input from user and store value to new variable urgency_cost with value from given variable priority/standard
urgency_choice = input("Choose between the following options: Priority @R100.00 or Standard @R20.00: ")

if urgency_choice == priority:
    urgency_cost = priority
else:
    urgency_cost = standard

# Get sum of all inputs and print the total cost
total_price = price_input + del_cost + ins_cost + gift_cost + urgency_cost
print("The total cost of your purchase is: R" + str(total_price))
