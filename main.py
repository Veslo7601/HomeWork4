"""All function """


def decorator(func):
    """Decorator"""
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except KeyError:
            return "Enter the correct command"
        except ValueError:
            return "Please enter a valid name and phone number"
        except IndexError:
            return "Enter the correct command, name and phone number"
        except Exception as e:
            return f"{e}"
    return wrapper

contact_dict = {}

def command_hello():
    """Function Hello"""
    return "How can I help you?"

def command_add(name,phone):
    """Function add phone"""
    if name not in contact_dict:
        contact_dict[name] = phone
        return f"I add phone number {phone} to {name}"
    else:
        raise Exception("Contact already exists")

def command_change(name,phone):
    """Function change phone"""
    if name in contact_dict:
        contact_dict[name] = phone
        return f"I change phone number {phone} in {name}"
    else:
        raise Exception("Contact does not exist, enter the name of an existing contact")

def command_phone(name):
    """Function show phone number"""
    if name in contact_dict:
        return f"contact - {name} have phone number: {contact_dict[name]} "
    else:
        raise Exception("Contact does not exist, enter the name of an existing contact")

def command_show_all():
    """Function show all phone number"""
    return contact_dict

def command_good_bye():
    """Function close bot"""
    global ACTIVE_BOT
    ACTIVE_BOT = False
    return"Good Bye!"


def get_command(command):
    """Function command bot"""
    return command_list[command]

command_list = {
        "hello": command_hello,
        "add" : command_add,
        "change": command_change,
        "phone": command_phone,
        "show all": command_show_all,
        "good bye": command_good_bye,
        "close": command_good_bye,
        "exit": command_good_bye
    }

ACTIVE_BOT = False

@decorator
def command_parser(user_input):
    """Сommand parser"""
    if user_input in ["show all", "hello", "good bye", "close", "exit"]:
        return get_command(user_input)()
    else:
        user_input = user_input.split()
        if user_input[0] == "phone":
            return get_command(user_input[0])(user_input[1])
        else:
            return get_command(user_input[0])(user_input[1],int(user_input[2]))

def main():
    """Bot"""
    global ACTIVE_BOT
    ACTIVE_BOT = True
    while ACTIVE_BOT:
        user_input = input("Enter the command: ").lower().strip()
        print(command_parser(user_input))

main()
