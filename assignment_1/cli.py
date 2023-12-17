def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."

    return inner


def non_existing_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Give me existing name."
        except TypeError:
            return 'Provide me only one name'

    return inner


def start():
    return 'How can I help you?'


@input_error
def change_contact(args, contacts):
    name, phone = args

    if not contacts.get(name):
        return 'Invalid name'

    contacts[name] = phone
    return "Contact updated."


@non_existing_error
def show_phone(name, contacts):
    return contacts[name]


def show_all(contacts):
    return '\n'.join([f"{name} - {phone}" for name, phone in contacts.items()])


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def finish():
    return 'Good bye!'


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print(finish())
            break
        elif command == "hello":
            print(start())
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == 'phone':
            print(show_phone(*args, contacts))
        elif command == 'all':
            print(show_all(contacts))
        elif command == 'change':
            print(change_contact(args, contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
