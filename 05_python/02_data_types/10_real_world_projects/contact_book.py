"""
Mini Project 4 — Contact Book 📇

Concepts used:
- dict (contact storage)
- list (multiple phone numbers)
- string operations (search)
- None / validations

Run:
    python contact_book.py
"""


def print_menu() -> None:
    print("\n" + "=" * 45)
    print("CONTACT BOOK")
    print("=" * 45)
    print("1. Add contact")
    print("2. View all contacts")
    print("3. Search contact")
    print("4. Delete contact")
    print("0. Exit")


def normalize_name(name: str) -> str:
    return name.strip().lower()


def main() -> None:
    # normalized_name -> contact info
    contacts: dict[str, dict[str, object]] = {}

    while True:
        print_menu()
        choice = input("Enter choice: ").strip()

        if choice == "0":
            print("Goodbye!")
            break

        if choice == "1":
            name = input("Enter name: ").strip()
            key = normalize_name(name)
            if not key:
                print("Name cannot be empty.")
                continue

            phone = input("Enter phone: ").strip()
            if not phone:
                print("Phone cannot be empty.")
                continue

            email = input("Enter email (optional): ").strip()

            if key not in contacts:
                contacts[key] = {"name": name, "phones": [phone], "email": email}
                print("Contact added.")
            else:
                phones: list[str] = contacts[key]["phones"]  # type: ignore[assignment]
                phones.append(phone)
                if email and not contacts[key].get("email"):
                    contacts[key]["email"] = email
                print("Phone added to existing contact.")

        elif choice == "2":
            if not contacts:
                print("No contacts yet.")
                continue
            print("\nContacts:")
            for key, info in contacts.items():
                phones: list[str] = info["phones"]  # type: ignore[assignment]
                print(f"- {info['name']} | phones={phones} | email={info.get('email', '')}")

        elif choice == "3":
            q = normalize_name(input("Search name: "))
            if not q:
                print("Empty search.")
                continue

            # exact match first
            info = contacts.get(q)
            if info is not None:
                print("Found:", info)
                continue

            # partial match
            matches = [info for key, info in contacts.items() if q in key]
            if not matches:
                print("No matches.")
            else:
                print("Matches:")
                for m in matches:
                    print(" ", m)

        elif choice == "4":
            name = input("Enter name to delete: ").strip()
            key = normalize_name(name)
            if key in contacts:
                del contacts[key]
                print("Deleted.")
            else:
                print("Contact not found.")

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
