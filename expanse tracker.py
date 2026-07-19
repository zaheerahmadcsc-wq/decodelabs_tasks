# Expense Tracker Project
# Created by: Zaheer Ahmad

print("===== EXPENSE TRACKER =====")

total_spent = 0

while True:
    expense = input("Enter expense amount (or type 'done' to finish): ")

    if expense.lower() == "done":
        break

    total_spent = total_spent + float(expense)

print("\n===== SUMMARY =====")
print("Total Amount Spent: ₹", total_spent)
print("Thank you for using Expense Tracker!")
