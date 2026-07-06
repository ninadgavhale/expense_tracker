import json

store = []

def expense_tracker():
    while True:
        try:
            user_expense = float(input("Enter the amount you spent: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        description = input("Describe where you spent the money: ")
        store.append({
            "amount": user_expense,
            "description": description
        })
        
        another = input("do you want to add another expence? (yes/no) ").strip().lower()
        if another == 'yes':
            pass
        elif another == "no":  
            print("thank you for using expence tracker") 
            break
        else:
            print("thank you for using expence tracker")
            break
    print(f"your total expence is {sum(expense['amount'] for expense in store)}")  # 
    save_data()

def view_expenses(): 
    print("your expences are :")
    for expense in store:
        print(f"{expense['description']} : {expense['amount']}")


def delete_expenses():

    description_to_delete = input("enter the description of the expense you want to delete: ")
    deletation = None
    for expense in store:
        if expense['description'].strip().lower() == description_to_delete.strip().lower():
            deletation = expense
            break
    if deletation:
        store.remove(deletation)
        print("expense deleted successfully.")
    else:
        print("expense not found.")
    save_data()
            

def show_total_expenses():
    total_amount = 0

    for expense in store:
        total_amount += expense['amount']

    print(f"Total expenses: {total_amount}")


def save_data():
    with open("storage.json", "w") as f:
        json.dump(store, f)


def load_data():
    try:
        with open("storage.json", "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def main():
    while True:
        
        
        print(". Expense Tracker Menu:")
        print(". Add Expense")
        print(". View Expenses")
        print(". Delete Expense")
        print(". Show Total Expenses")
        print(". Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            expense_tracker()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            delete_expenses()
        elif choice == '4':
            show_total_expenses()
        elif choice == '5':
            print("Thank you for using the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

store = load_data()
if __name__ == "__main__": main()



