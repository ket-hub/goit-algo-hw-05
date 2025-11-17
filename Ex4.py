welcome_banner = '''
  ___      _       _          _    _           _   
 | _ ) ___| |_    /_\   _____(_)__| |_ ___ _ _| |_ 
 | _ \/ _ \  _|  / _ \ (_-<_-< (_-<  _/ -_) ' \  _|
 |___/\___/\__| /_/ \_\/__/__/_/__/\__\___|_||_\__|
'''
print(welcome_banner)

def parse_input(user_input):
    cmd, *args = user_input.strip().split()
    return cmd.lower(), args

def input_error(func):
    def inner(args, contacts):
        try:
            return func(args, contacts)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Give me correct name"
        except IndexError:
            return "You are trying to access an element that does not exist."
    return inner

@input_error
def add_contact(args, contacts):
    if len(args) < 2:
        return "Usage: add <name> <phone1> [phone2] ..."
    name, *phones = args
    if name in contacts:
        contacts[name].extend(phones)
        return f"Added {len(phones)} more phone(s) to '{name}'."
    else:
        contacts[name] = phones
        return f"Contact '{name}' added with {len(phones)} phone(s)."

@input_error
def change_contact(args, contacts):
    if len(args) < 2:
        return "Usage: change <name> <new_phone1> [new_phone2] ..."
    name, *phones = args
    for name in contacts:
        contacts[name] = phones
        return f"Contact '{name}' updated with {len(phones)} phone(s)."
    # else:
    #     return f"No contact found with name '{name}'."

@input_error
def show_phone(args, contacts):
    if len(args) != 1:
        return "Usage: phone <name>"

    name = args[0]

    # if name not in contacts:
    #     return f"No contact found with name '{name}'."

    phones = contacts[name]
    return ", ".join(phones)



def show_all_contacts(contacts):
    if not contacts:
        return "No contacts found."
    result = ["Contact list:"]
    for name, phones in contacts.items():
        result.append(f"- {name}: {', '.join(phones)}")
    return "\n".join(result)




def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "show" and args == ["all"]:
            print(show_all_contacts(contacts))
        
        elif command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
