def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Index out of range."
    return inner

contacts = {}

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def get_phone(args, contacts):
    name = args[0]
    phone = contacts.get(name, "Contact not found.")
    return f"{name}: {phone}"

@input_error
def list_all(args, contacts):
    result = "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    return result

while True:
    command = input("Enter a command: ").strip().lower()
    if command == "add":
        arguments = input("Enter the argument for the command: ").split()
        print(add_contact(arguments, contacts))
    elif command == "phone":
        arguments = input("Enter the argument for the command: ").split()
        print(get_phone(arguments, contacts))
    elif command == "all":
        arguments = input("Enter the argument for the command: ").split()
        print(list_all(arguments, contacts))
    elif command == "exit":
        break
    else:
        print("Unknown command. Try again.")
