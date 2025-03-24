from functools import wraps


def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ValueError, TypeError, IndexError):
            match func.__name__:
                case "parse_input":
                    print("Command can not be blank")
                case "add_contact":
                    print("Usage: add NAME PHONE_NUMBER")
                case "change_contact":
                    print("Usage: change NAME PHONE_NUMBER")
                case "show_phone":
                    print("Usage: phone NAME")
                case _:
                    print(f"error in {func.__name__}")

    return inner


@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


# TODO:Додати пізніше перевірку на кількість аргументів та анотаціі
@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    name, phone = args
    if not contacts.get(name):
        return "Contact does not exist."
    contacts[name] = phone
    return "Contact updated."


@input_error
def show_phone(args, contacts):
    name = args[0]
    phone_number = contacts.get(name)
    return f"Phone number: {phone_number}" if phone_number else "Contact not found"


def show_all(contacts):
    if not contacts:
        return "Contacts not found."
    return "\n".join(
        f"Name: {name}, Phone number: {phone}" for name, phone in contacts.items()
    )


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        if not (parsed_user_input := parse_input(user_input)):
            continue
        command, *args = parsed_user_input

        match command:
            case "close" | "exit":
                print("Good bye!")
                break
            case "hello":
                print("How can I help you?")
            case "add":
                if message := add_contact(args, contacts):
                    print(message)
            case "all":
                print(show_all(contacts))
            case "change":
                if message := change_contact(args, contacts):
                    print(message)
            case "phone":
                if message := show_phone(args, contacts):
                    print(message)
            case _:
                print("Invalid command.")


if __name__ == "__main__":
    main()
