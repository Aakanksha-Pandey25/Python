print("Welcome to Simple Expense Calculator")
print("Type 'done' to stop adding expenses.\n")
total = 0  
while True:
    amount = input("Enter an expense amount (or type 'done' to finish): ")
    if amount.lower() == 'done':
        break

    if amount.isdigit():
        total = total + int(amount)  
    else:
        print("Please enter a valid number.")

print("\nYour total expense is: ", total)
