"""
Mini Project 1 — Banking System 🏦

Concepts used:
- int, float
- dict (accounts)
- list (transactions)
- bool (validations)
- None (missing accounts)

Run:
    python banking_system.py

Sample (expected) flow:
    1) Create account
    2) Deposit
    3) Withdraw
    4) Balance
    5) Transactions
    0) Exit
"""


def print_menu() -> None:
    print("\n" + "=" * 45)
    print("BANKING SYSTEM")
    print("=" * 45)
    print("1. Create account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check balance")
    print("5. View transactions")
    print("0. Exit")


def get_float(prompt: str) -> float | None:
    value = input(prompt).strip()
    try:
        amount = float(value)
        return amount
    except ValueError:
        return None


def main() -> None:
    # account_no -> account data
    accounts: dict[int, dict[str, object]] = {}

    while True:
        print_menu()
        choice = input("Enter choice: ").strip()

        if choice == "0":
            print("Goodbye!")
            break

        if choice == "1":
            acc_str = input("Enter new account number (int): ").strip()
            if not acc_str.isdigit():
                print("Invalid account number.")
                continue
            acc_no = int(acc_str)
            if acc_no in accounts:
                print("Account already exists.")
                continue

            name = input("Enter account holder name: ").strip()
            accounts[acc_no] = {"name": name, "balance": 0.0, "tx": []}
            print("Account created.")

        elif choice == "2":
            acc_str = input("Enter account number: ").strip()
            if not acc_str.isdigit():
                print("Invalid account number.")
                continue
            acc_no = int(acc_str)
            account = accounts.get(acc_no)
            if account is None:
                print("Account not found.")
                continue

            amount = get_float("Enter deposit amount: ")
            if amount is None or amount <= 0:
                print("Invalid amount.")
                continue

            balance = float(account["balance"])
            balance += amount
            account["balance"] = balance
            tx: list[str] = account["tx"]  # type: ignore[assignment]
            tx.append(f"DEPOSIT {amount:.2f}")
            print(f"Deposited {amount:.2f}. New balance = {balance:.2f}")

        elif choice == "3":
            acc_str = input("Enter account number: ").strip()
            if not acc_str.isdigit():
                print("Invalid account number.")
                continue
            acc_no = int(acc_str)
            account = accounts.get(acc_no)
            if account is None:
                print("Account not found.")
                continue

            amount = get_float("Enter withdrawal amount: ")
            if amount is None or amount <= 0:
                print("Invalid amount.")
                continue

            balance = float(account["balance"])
            if amount > balance:
                print("Insufficient funds.")
                continue

            balance -= amount
            account["balance"] = balance
            tx: list[str] = account["tx"]  # type: ignore[assignment]
            tx.append(f"WITHDRAW {amount:.2f}")
            print(f"Withdrew {amount:.2f}. New balance = {balance:.2f}")

        elif choice == "4":
            acc_str = input("Enter account number: ").strip()
            if not acc_str.isdigit():
                print("Invalid account number.")
                continue
            acc_no = int(acc_str)
            account = accounts.get(acc_no)
            if account is None:
                print("Account not found.")
                continue
            print(f"Balance = {float(account['balance']):.2f}")

        elif choice == "5":
            acc_str = input("Enter account number: ").strip()
            if not acc_str.isdigit():
                print("Invalid account number.")
                continue
            acc_no = int(acc_str)
            account = accounts.get(acc_no)
            if account is None:
                print("Account not found.")
                continue
            tx: list[str] = account["tx"]  # type: ignore[assignment]
            if not tx:
                print("No transactions yet.")
            else:
                print("Transactions:")
                for i, t in enumerate(tx, start=1):
                    print(f"{i}. {t}")

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
