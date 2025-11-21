# Mini ATM Simulator

# Initial variables
balance = 1000.0
PIN = "1234"
transactions = []


def authenticate():
    # Ask user to input PIN and check validity
    entered_pin = input("Enter your PIN: ")
    if entered_pin == PIN:
        return True
    else:
        print("Incorrect PIN. Try again.")
        return False


def show_menu():
    # Display menu options
    print("Select action:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")


def deposit():
    # Deposit funds
    try:
        amount = float(input("Enter amount to deposit: "))
        if amount <= 0:
            print("Amount must be positive.")
            return
        global balance
        balance += amount
        transactions.append(f"Deposited: {amount}")
        print(f"Deposited {amount}. New balance: {balance}")
    except ValueError:
        print("Invalid input. Use numbers only.")


def withdraw():
    # Withdraw funds
    try:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Amount must be positive.")
            return
        global balance
        if amount > balance:
            print("Insufficient balance.")
            return
        balance -= amount
        transactions.append(f"Withdrew: {amount}")
        print(f"Withdrew {amount}. New balance: {balance}")
    except ValueError:
        print("Invalid input. Use numbers only.")


def main():
    # Main ATM loop
    if not authenticate():
        return
    while True:
        show_menu()
        action = input("Enter your choice (1/2/3/4): ")
        if action == "1":
            print(f"Current balance: {balance}")
        elif action == "2":
            deposit()
        elif action == "3":
            withdraw()
        elif action == "4":
            print("Exiting. Thank you for using Mini ATM Simulator.")
            break
        else:
            print("Invalid option. Please choose 1, 2, 3 or 4.")

        # Display recent transactions
        print("Transactions:", transactions)

    if __name__ == "__main__":
        main()
