import difflib


def main():
    print(f"COMMAND LINE INTERFACE\nYour Personal Assistant\n" + "=" * 23)
    print("If you wont to read reference to Personal Assistant,\nEnter <<help>> or <<reference>>.")
    while True:
        command = input("Enter your command\n>>").lower()
        sep_command = command.split(" ")
        if sep_command[0] == "add" and sep_command[1] == "contact":
            pass
        if sep_command[0] == "add" and sep_command[1] == "notes":
            pass
        if sep_command[0] == "add" and sep_command[1] == "tag":
            pass
        if sep_command[0] == "show" and sep_command[1] == "contact":
            pass
        if sep_command[0] == "show" and sep_command[1] == "birthday":
            pass
        if sep_command[0] == "show" and sep_command[1] == "all":
            pass
        if sep_command[0] == "show" and sep_command[1] == "note":
            pass
        if sep_command[0] == "edit" and sep_command[1] == "contact":
            pass
        if sep_command[0] == "edit" and sep_command[1] == "note":
            pass
        if sep_command[0] == "sort" and sep_command[1] == "tags":
            pass
        if sep_command[0] == "sort" and sep_command[1] == "folders":
            pass
        if sep_command[0] == "delete" and sep_command[1] == "contact":
            pass
        if sep_command[0] == "delete" and sep_command[1] == "note":
            pass
        if command == "help" or command == "reference":
            help_command()
        elif command == "good bye" or command == "close" or command == "exit":
            print("Good bye!\nHope see you soon!")
            break
        else:
            command_dict = {1: "add contact", 2: "add notes", 3: "add tag", 4: "show contact",
                            5: "show birthday", 6: "show all", 7: "show note", 8: "edit contact",
                            9: "edit note", 10: "sort tags", 11: "sort folders", 12: "delete contact",
                            13: "delete note", 14: "help", 15: "reference", 16: "close",
                            17: "exit", 18: "good bye"}
            for value in command_dict.values():
                ratio = int(difflib.SequenceMatcher(None, command, value).ratio() * 100)
                if ratio > 50:
                    fixed_string = value[0] + value[1:]
                    print(f"You entered unknown command - {command}. Maybe it`s {fixed_string}? Try again.")
                elif ratio < 50:
                    continue


def help_command():
    """
    =====================================================
                 CLI - Command Line Interface
                       Personal Assistant
    =====================================================

    Personal Assistant works with Address book, write,
    save Notes and sort files in folders.

    Personal Assistant has a commands:
    1. "add contact" - for add name, address, contact information
    (phone, e-mail) and birthday to Address book write
    "add" then all details and enter it;

    2. "add notes" - for add notes write "add notes" then
    your note and enter it;

    3. "add tag" - for add tag to notes write "add tag"
    then some few words from note and enter it;

    4. "show contact" - for get all contact information
    write "show contact" then .........name and enter it;

    5. "show birthday" - for show a list of contacts who
    have a birthday after a specified number of days from
    the current date write "show birthday" then number of
    days and enter it;

    6. "show all" - for show all contacts in Address book
    write "show all" and enter command;

    7. "show note" - for search note write "show note"
    then few words from note or tag and enter it;

    8. "edit contact" - for edit contact information write
    "edit contact" then ....... enter it;

    9. "edit notes" - for edit notes write "edit notes"
    then ............. enter it;

    10. "sort tags" - for sort tags write "sort tags"
    ...................... enter it;

    11. "sort folders" - for sort files in folders write
    "sort folders" ................... enter it;

    12. "delete contact" - for delete name and contact
    information in Address book write "delete" then
    ............... and enter it;

    13. "delete note" - for delete note write "delete note"
    ....................enter it;

    14. "help", "reference" - for ask reference how to
    use Personal Assistant write "help" or "reference"
    and enter the command;

    15. "close", "exit", "good bye" - for finish work with
    Personal Assistant, write one of "close", "exit" or
    "good bye" and enter command then you will exit from
    Command Line Interface.

    Pleasant use!

    """
    print(help_command.__doc__)


if __name__ == "__main__":
    main()
