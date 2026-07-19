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

# Sample Output
===== EXPENSE TRACKER =====

Enter expense amount (or type 'done' to finish): 100
Enter expense amount (or type 'done' to finish): 50
Enter expense amount (or type 'done' to finish): 20
Enter expense amount (or type 'done' to finish): done

===== SUMMARY =====
Total Amount Spent: ₹ 170.0
Thank you for using Expense Tracker!
