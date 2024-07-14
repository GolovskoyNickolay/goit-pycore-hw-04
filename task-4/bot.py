def parse_input(user_input):
    # Розбирає введений користувачем рядок на команду та аргументи
    parts = user_input.strip().split()
    if len(parts) == 0:
        return None, []
    command = parts[0].lower()
    args = parts[1:]
    return command, args


def add_contact(contacts, name, phone):
    contacts[name] = phone
    print("Contact added.")


def change_contact(contacts, name, phone):
    if name in contacts:
        contacts[name] = phone
        print("Contact updated.")
    else:
        print("Contact not found.")


def show_phone(contacts, name):
    if name in contacts:
        print(contacts[name])
    else:
        print("Contact not found.")


def show_all(contacts):
    for name, phone in contacts.items():
        print(f"{name}: {phone}")


def main():
    contacts = {}
    while True:
        user_input = input("Enter command: ")
        command, args = parse_input(user_input)

        if command in ("exit", "close"):
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            if len(args) == 2:
                add_contact(contacts, args[0], args[1])
            else:
                print("Invalid command. Usage: add [name] [phone]")
        elif command == "change":
            if len(args) == 2:
                change_contact(contacts, args[0], args[1])
            else:
                print("Invalid command. Usage: change [name] [new phone]")
        elif command == "phone":
            if len(args) == 1:
                show_phone(contacts, args[0])
            else:
                print("Invalid command. Usage: phone [name]")
        elif command == "all":
            show_all(contacts)
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
