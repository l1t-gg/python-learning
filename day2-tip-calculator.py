print("Welcome to the tip calculator.")
amount = input(print("What was the total bill?"))
tip = input(print("What percentage would you like to give? 10, 12 or 15?"))
div = input(print("How many people to split the bill?"))
total = float(amount)+((float(tip)/100)*float(amount))
sum_per_head = float(total)/int(div)
print(round(sum_per_head, 2))