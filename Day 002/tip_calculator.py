print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
people = int(input("How many people to split the bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
bill_with_tip = (((bill * tip) / 100) + bill) / people
print(f"Each person should pay: ${bill_with_tip:.2f}")
