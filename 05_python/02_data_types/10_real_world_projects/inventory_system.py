"""
Mini Project 3 — Inventory System 📦

Concepts used:
- dict (inventory indexed by SKU)
- list (purchase history)
- tuple (immutable item snapshot)
- conversions (price/quantity)

Run:
    python inventory_system.py
"""


def print_menu() -> None:
    print("\n" + "=" * 45)
    print("INVENTORY SYSTEM")
    print("=" * 45)
    print("1. Add item")
    print("2. Update stock")
    print("3. List items")
    print("4. Buy item")
    print("5. Purchase history")
    print("0. Exit")


def read_int(prompt: str) -> int | None:
    s = input(prompt).strip()
    if s.isdigit():
        return int(s)
    return None


def read_float(prompt: str) -> float | None:
    s = input(prompt).strip()
    try:
        return float(s)
    except ValueError:
        return None


def main() -> None:
    inventory: dict[str, dict[str, object]] = {}
    history: list[tuple[str, str, int, float]] = []
    # history tuple: (sku, name, qty_bought, total_price)

    while True:
        print_menu()
        choice = input("Enter choice: ").strip()

        if choice == "0":
            print("Goodbye!")
            break

        if choice == "1":
            sku = input("Enter SKU (unique id): ").strip()
            if not sku:
                print("SKU cannot be empty.")
                continue
            if sku in inventory:
                print("SKU already exists.")
                continue
            name = input("Enter item name: ").strip()
            price = read_float("Enter price: ")
            stock = read_int("Enter stock qty: ")
            if price is None or price < 0 or stock is None or stock < 0:
                print("Invalid price/stock.")
                continue
            inventory[sku] = {"name": name, "price": price, "stock": stock}
            print("Item added.")

        elif choice == "2":
            sku = input("Enter SKU: ").strip()
            item = inventory.get(sku)
            if item is None:
                print("Item not found.")
                continue
            new_stock = read_int("Enter new stock qty: ")
            if new_stock is None or new_stock < 0:
                print("Invalid stock.")
                continue
            item["stock"] = new_stock
            print("Stock updated.")

        elif choice == "3":
            if not inventory:
                print("No items yet.")
                continue
            print("\nSKU | Name | Price | Stock")
            print("-" * 45)
            for sku, item in inventory.items():
                print(f"{sku} | {item['name']} | {float(item['price']):.2f} | {int(item['stock'])}")

        elif choice == "4":
            sku = input("Enter SKU: ").strip()
            item = inventory.get(sku)
            if item is None:
                print("Item not found.")
                continue
            qty = read_int("Enter quantity to buy: ")
            if qty is None or qty <= 0:
                print("Invalid quantity.")
                continue
            stock = int(item["stock"])
            if qty > stock:
                print("Not enough stock.")
                continue

            price = float(item["price"])
            total = qty * price
            item["stock"] = stock - qty
            history.append((sku, str(item["name"]), qty, total))
            print(f"Purchased {qty} x {item['name']} for {total:.2f}")

        elif choice == "5":
            if not history:
                print("No purchases yet.")
                continue
            print("\nPurchase history:")
            for i, (sku, name, qty, total) in enumerate(history, start=1):
                print(f"{i}. {sku} | {name} | qty={qty} | total={total:.2f}")

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
