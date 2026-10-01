"""
====== EXPENSE TRACKER CODE ======
"""


# Add expense
def add_expense(expenses):
    categories = [
        "Food",
        "Transport",
        "Entertainment",
        "Bills",
        "Shopping",
        "Health",
        "Education",
        "Groceries",
        "Other"
    ]

    while True:
        expense_name = input(
            "Enter the expense name (press 'q' to exit): "
        ).strip().capitalize()

        if expense_name.lower() == "q":
            print("Exiting...")
            return

        while True:
            try:
                amount = float(input("Enter the amount: "))

                if amount <= 0:
                    print("Please enter a valid amount.")
                    continue

            except ValueError:
                print("Please enter a valid amount.")
                continue

            break

        print("\n====== CATEGORY ======")

        for i, category in enumerate(categories):
            print(f"{i}: {category}")

        while True:
            try:
                category_choice = int(
                    input("Please select a category: ")
                )

                if category_choice < 0 or category_choice >= len(categories):
                    print("Please enter a valid category.")
                    continue

            except ValueError:
                print(
                    f"Please choose a valid category "
                    f"from 0 to {len(categories) - 1}."
                )
                continue

            break

        expenses.append({
            "name": expense_name,
            "amount": amount,
            "category": categories[category_choice]
        })

        print(f"Expense: {expense_name} added successfully.\n")
        return


# View expenses
def view_expense(expenses):
    if not expenses:
        print("Expense list is empty! Nothing to show.")
        return

    print("====== EXPENSES ======")

    for i, expense in enumerate(expenses, start=1):
        print(f"{i}: {expense['name']}")
        print(f"Amount: ${expense['amount']}")
        print(f"Category: {expense['category']}")
        print()


# Search expense
def search_expense(expenses):
    if not expenses:
        print("Expense list is empty! Nothing to show.")
        return

    expense_name = input(
        "Enter the expense name to search: "
    ).strip().capitalize()

    found = False

    for item in expenses:
        if item["name"] == expense_name:
            print("\nExpense found!")
            print(f"Name: {item['name']}")
            print(f"Amount: ${item['amount']}")
            print(f"Category: {item['category']}")
            print()

            found = True

    if not found:
        print(f"Expense: {expense_name} not found in the system.")


# Calculate total expense
def total_expense(expenses):
    if not expenses:
        print("Expense list is empty! Total expense is $0.")
        return

    total = 0

    for item in expenses:
        total += item["amount"]

    print(f"Total expense: ${total}")


# Delete expense
def delete_expense(expenses):
    if not expenses:
        print("Expense list is empty! Nothing to delete.")
        return

    to_delete = input(
        "Enter the expense name to delete: "
    ).strip().capitalize()

    found = False

    for i, item in enumerate(expenses):
        if item["name"] == to_delete:
            deleted_item = expenses.pop(i)

            print(
                f"Expense: {deleted_item['name']} "
                f"successfully deleted."
            )

            found = True
            break

    if not found:
        print(f"Expense: {to_delete} does not exist in the system.")


# Main program
def expense_tracker():
    expenses = []

    while True:
        print("\n====== EXPENSE TRACKER ======")
        print("1. Add expense")
        print("2. View expense")
        print("3. Search expense")
        print("4. Calculate total expense")
        print("5. Delete expense")
        print("6. Exit")

        try:
            menu_choice = int(input("Please select a choice: "))

            if menu_choice < 1 or menu_choice > 6:
                print("Please enter a valid choice!")
                continue

        except ValueError:
            print("Please enter a valid choice!")
            continue

        match menu_choice:
            case 1:
                add_expense(expenses)

            case 2:
                view_expense(expenses)

            case 3:
                search_expense(expenses)

            case 4:
                total_expense(expenses)

            case 5:
                delete_expense(expenses)

            case 6:
                print("Exiting...")
                return


expense_tracker()