# Expense Tracker Project
# DecodeLabs - Project 2

def main():
    print("===== EXPENSE TRACKER =====")

    total_expense = 0
    expenses = []

    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. View Total Spent")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        # Add Expense
        if choice == "1":
            try:
                amount = float(input("Enter expense amount: ₹"))

                if amount < 0:
                    print("Expense cannot be negative!")
                    continue

                expenses.append(amount)
                total_expense += amount

                print("Expense added successfully!")

            except ValueError:
                print("Please enter a valid number!")

        # View Expenses
        elif choice == "2":
            if len(expenses) == 0:
                print("No expenses added yet.")
            else:
                print("\n--- Expense List ---")
                for i, expense in enumerate(expenses, start=1):
                    print(f"{i}. ₹{expense}")

        # View Total
        elif choice == "3":
            print(f"\nTotal Spent: ₹{total_expense}")

        # Exit
        elif choice == "4":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice! Please select between 1-4.")


# Run the program
if __name__ == "__main__":
    main()