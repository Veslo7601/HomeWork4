"""All function """

def input_error(default_value=None):
    """Error_decorator"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                return result
            except KeyError:
                print("Enter the correct command")
                return default_value
            except ValueError:
                print("Please enter a valid name and phone number")
                return default_value
            except IndexError:
                print("Enter the correct company, name and phone number")
                return default_value
            except Exception as e:
                print(f"{e}")
                return default_value
        return wrapper
    return decorator

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

@input_error(default_value="")
def main():
    """Function bot"""
    user_input = input("Enter the command: ").lower()
    if user_input in ["show all", "hello", "good bye", "close", "exit"]:
        print(get_command(user_input)())
    else:
        user_input = user_input.split()
        if user_input[0] == "phone":
            print(get_command(user_input[0])(user_input[1]))
        else:
            print(get_command(user_input[0])(user_input[1],int(user_input[2])))

def phone_bot():
    """Bot"""
    global ACTIVE_BOT
    ACTIVE_BOT = True

    while ACTIVE_BOT:
        main()

phone_bot()
