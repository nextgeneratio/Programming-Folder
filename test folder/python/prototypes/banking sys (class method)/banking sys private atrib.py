import os
from cryptography.fernet import Fernet

class BankAccount:
    FILE_NAME = ".balance.dat"  # Hidden file for security
    KEY_FILE = ".key.dat"  # File to store the encryption key

    def __init__(self):
        self.__key = self.load_or_generate_key()  # Load encryption key
        self.__cipher = Fernet(self.__key)
        self.__balance = self.load_balance()  # Load encrypted balance

    def deposit(self, deposit_amount):
        if deposit_amount > 0:
            self.__balance += deposit_amount
            print(f"✅ Deposited: {deposit_amount}, New Balance: {self.__balance}")
        else:
            print("❌ Deposit amount must be positive!")

    def withdraw(self, withdraw_amount):
        if withdraw_amount > self.__balance:
            print("❌ Insufficient balance!")
        elif withdraw_amount <= 0:
            print("❌ Withdrawal amount must be positive!")
        else:
            self.__balance -= withdraw_amount
            print(f"✅ Withdrawn: {withdraw_amount}, Remaining Balance: {self.__balance}")

    def get_balance(self):
        return self.__balance

    def save_balance(self):
        """Encrypt and save balance to file."""
        encrypted_balance = self.__cipher.encrypt(str(self.__balance).encode())
        with open(self.FILE_NAME, "wb") as file:
            file.write(encrypted_balance)

    def load_balance(self):
        """Load and decrypt balance from file if it exists."""
        if os.path.exists(self.FILE_NAME):
            with open(self.FILE_NAME, "rb") as file:
                encrypted_balance = file.read()
                try:
                    return float(self.__cipher.decrypt(encrypted_balance).decode())
                except (Fernet.InvalidToken, ValueError):
                    return 0  # If decryption fails, reset balance
        return 0  # Default balance if file doesn't exist

    def load_or_generate_key(self):
        """Generate or load encryption key."""
        if os.path.exists(self.KEY_FILE):
            with open(self.KEY_FILE, "rb") as file:
                return file.read()
        else:
            key = Fernet.generate_key()
            with open(self.KEY_FILE, "wb") as file:
                file.write(key)
            return key

    @staticmethod
    def get_valid_amount(prompt):
        """Helper function to safely get a valid numeric input."""
        while True:
            try:
                valid_amount = float(input(prompt))
                return valid_amount
            except ValueError:
                print("❌ Invalid input! Please enter a number.")


# User interaction
account = BankAccount()

while True:
    print("\n1. Deposit Money")
    if account.get_balance() > 0:  # Show withdraw only if balance > 0
        print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        amount = account.get_valid_amount("Enter deposit amount: ")
        account.deposit(amount)

    elif choice == "2" and account.get_balance() > 0:
        amount = account.get_valid_amount("Enter withdrawal amount: ")
        account.withdraw(amount)

    elif choice == "3":
        print(f"💰 Your balance is: {account.get_balance()}")

    elif choice == "4":
        account.save_balance()  # Save encrypted balance before exiting
        print("🔐 Balance securely saved! 🚪 Exiting... Thank you!")
        break

    else:
        print("❌ Invalid choice! Please enter a valid option.")
