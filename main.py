import argparse
from decimal import Decimal, InvalidOperation
import json
from datetime import date

'''Understand the code
- import json — imports Python's JSON module.
- open("expenses.json", "r") — opens the file in read mode.
- json.load(file) — converts the JSON data into Python objects.
- expenses — now holds a list of dictionaries.
- print(expenses) — displays the loaded data.
'''
def load_expenses():

    try:
        with open("expenses.json","r") as file:
            expenses = json.load(file) #json.load(file) — converts the JSON data into Python objects.

        return expenses
    except (FileNotFoundError, ValueError):
        return []
    

'''
Understand the important parts:
- "w" opens the file in write mode, replacing its existing contents.
- expenses is the Python list we want to save.
- indent=4 makes the JSON file readable.
'''

def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)


'''Requirements:
- If expenses contain IDs 1, 2, and 3, return 4.
- If expenses contain IDs 1 and 3, return 4.
- If the list is empty, return 1.
'''
def get_next_id(expenses):

     if len(expenses) == 0:
        return 1

     next_id = max(expense["id"] for expense in expenses) + 1
   
     return next_id

def validate_description(description):
    if not isinstance(description, str) or not description.strip():
        raise ValueError("Description cannot be empty")

    return description.strip()

from decimal import Decimal, InvalidOperation

def validate_amount(amount):
    try:
        value = Decimal(str(amount))
    except (InvalidOperation, ValueError):
        raise ValueError("Amount must be a valid number")

    if not value.is_finite() or value <= 0:
        raise ValueError("Amount must be greater than zero")

    return value

def validate_category(category):
    if not isinstance(category, str) or not category.strip():
            raise ValueError("category cannot be empty")
    
    return category.strip()


def add_expense(description, amount, category):
    description = validate_description(description)
    amount = validate_amount(amount)
    category = validate_category(category)

    load_expense = load_expenses()
    next_id = get_next_id(load_expense)

    expense_list = {
        "id": next_id,
        "date": date.today().isoformat(),
        "description": description,
        "category": category,
        "amount": str(amount)
        }

    load_expense.append(expense_list)
    save_expenses(load_expense)

    return expense_list["id"]


def no_expenses(expenses):
    expenses = load_expenses()
    
    if not expenses:
       print("No expenses found.")
    return
    
def list_expenses():
    expenses = load_expenses()

    if not expenses:
        print("No expenses found.")
        return

    print(
        f"{'ID':<5}"
        f"{'Date':<13}"
        f"{'Description':<20}"
        f"{'Category':<15}"
        f"{'Amount':>12}"
    )

    for expense in expenses:
        print(
            f"{expense['id']:<5}"
            f"{expense['date']:<13}"
            f"{str(expense.get('description') or 'No description'):<20}"
            f"{expense.get('category', 'Uncategorized'):<15}"
            f"{'QAR ' + format(float(expense['amount']), '.2f'):>12}"
        )
list_expenses()


def summarize_expenses():

    expenses = load_expenses()
    if not expenses:
        no_expenses(expenses)
        return None
    total = 0

    for exp in expenses:
        total = float(exp["amount"]) + total

    return total

def summarize_by_category():

    expenses = load_expenses()
    category_totals = {}

    for exp in expenses:
       
       category = exp.get("category") or ("Uncategorized")
       amount = float(exp.get("amount", 0))
    
       if category not in category_totals:
           category_totals[category] = 0

       category_totals[category] += amount
       
    return category_totals    
  
def print_category_summary():

    sum_cat = summarize_by_category()
    print("Expense Summary by Category")
    print("---------------------------") 
    
    for category, amount in sum_cat.items():
        print(f"{category:<15} QAR {amount:.2f}"  )   
print_category_summary()           

def show_menu():
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. List Expenses")
    print("3. Total Expenses")
    print("4. Category Summary")
    print("5. Exit")

    return input("Enter your choice (1-5): ")



def main_lo():
    while True:
        choice = show_menu()
        match choice:
            case "1":
                description = input("Enter expense description: ")
                category = input("Enter expense category: ")

                try:
                    amount = float(input("Enter expense amount (QAR): "))
                except ValueError:
                    print("Please enter a valid number.")
                    continue

                try:
                    new_id = add_expense(description, amount, category)
                    print(f"Expense added successfully! ID: {new_id}")  
                    
                except ValueError as error:
                    print(f"Error: {error}")

            case "2":
                print("List Expenses selected")
                list_expenses()

            case "3":
                total_exp = summarize_expenses()

                if total_exp is not None:
                    print(f"Total Expenses: QAR {total_exp:.2f}")

            case "4":
                print("Category Summary selected")
                print_category_summary()

            case "5":
                print("Exiting Expense Tracker. Goodbye!")
                break

            case _:
                print("Invalid choice. Please enter a number from 1 to 5.")
if __name__ == "__main__":
    main_lo()         