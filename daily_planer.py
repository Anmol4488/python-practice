import datetime
from tabulate import tabulate

print("----- Personal Expense Tracker -----")

username = input("Enter your name: ")
salary = float(input("Enter your salary: "))

print(f"Welcome, {username}")

expenses = {}

while True:
    product = input("Enter product (or 'exit' to finish): ")

    if product.lower() == "exit":
        break

    price = float(input("Enter price: "))

    if product in expenses:
        expenses[product] += price
    else:
        expenses[product] = price

total_expense = sum(expenses.values())
remaining = salary - total_expense

print("\nDate:", datetime.datetime.now())

print("\nExpense Report")
print(tabulate(
    expenses.items(),
    headers=["Product", "Price"],
    tablefmt="grid"
))

print("\nTotal Expense:", total_expense)

if remaining < 0:
    print("Insufficient Balance!")
else:
    print("Remaining Salary:", remaining)
