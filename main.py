import difflib
import json
import pickle

from address_book import AddressBook, Record
from notes import NoteRecord
from sort_folder import sort_folder_command


def main():
    print(f"COMMAND LINE INTERFACE\nYour Personal Assistant\n" + "=" * 23)
    print("If you wont to read reference to Personal Assistant,\nEnter <<help>> or <<reference>>")
    try:
        with open('data.json', 'r') as json_file:
            note_list = json.load(json_file)
            last_id = note_list[-1]['id']
            NoteRecord.counter = last_id
    except FileNotFoundError:
        note_list = []
    try:
        with open('data_test.bin', 'rb') as f:
            address_book = pickle.load(f)
    except FileNotFoundError:
        address_book = AddressBook()
    while True:
        try:
            command = input("Enter your command\n>>").lower()
            sep_command = command.split(" ")
            if sep_command[0] == "add" and sep_command[1] == "contact": # and len(sep_command) > 2:
                address_book.add_record(Record(sep_command[2].title(), sep_command[3], sep_command[4],
                                               sep_command[5], sep_command[6:]))
            elif sep_command[0] == "add" and sep_command[1] == "note" and len(sep_command[2:]) != 0:
                tag_index = sep_command.index('-tag') if '-tag' in sep_command else len(sep_command)
                title_index = sep_command.index('-title') if '-title' in sep_command else None
                NoteRecord.counter += 1
                main_note = NoteRecord(' '.join(sep_command[2:tag_index]),
                                       sep_command[tag_index + 1:title_index] if tag_index != len(sep_command) else None,
                                       sep_command[title_index + 1].title() if title_index else None)
                note_list.append(main_note.record)
            elif sep_command[0] == "add" and sep_command[1] == "note" and len(sep_command[2:]) == 0:
                print("You entered empty note!")
            elif sep_command[0] == "add" and sep_command[1] == "tag":
                title_index = sep_command.index('-title') if '-title' in sep_command else None
                for note in note_list:
                    if note['title'] == sep_command[title_index + 1]:
                        note['tag'] += (sep_command[2:title_index])
            elif sep_command[0] == "show" and sep_command[1] == "contact":
                address_book.find_contact(sep_command[2].title())
            elif sep_command[0] == "show" and sep_command[1] == "birthday":
                print(address_book.days_to_birthday(int(sep_command[2])))
            elif sep_command[0] == "show" and sep_command[1] == "all":
                address_book.__str__()
            elif sep_command[0] == "show" and sep_command[1] == "note":
                print(note_list)
            elif sep_command[0] == "edit" and sep_command[1] == "contact":
                address_book.edit_contact(sep_command[2].title())
            elif sep_command[0] == "edit" and sep_command[1] == "note":
                for note in note_list:
                    if note['title'] == sep_command[2]:
                        change_index = sep_command.index('-change') if '-change' in sep_command else None
                        if change_index:
                            note['note'] = ' '.join(sep_command[change_index + 1:])
                        else:
                            print('You didn`t print text to change!\nTry again!')
            elif sep_command[0] == "search" and sep_command[1] == "tags":
                NoteRecord.tag_search(sep_command[2])
            elif sep_command[0] == "sort" and sep_command[1] == "folders":
                sort_folder_command(sep_command[2:])
                print("Your folder just has been sorted!")
            elif sep_command[0] == "delete" and sep_command[1] == "contact":
                address_book.del_contact(sep_command[2].title())
            elif sep_command[0] == "delete" and sep_command[1] == "note":
                for note in note_list:
                    if note['title'] == sep_command[2]:
                        note_index = note_list.index(note)
                        note_list.pop(note_index)
            elif command == "help" or command == "reference":
                help_command()
            elif command in ["good bye", "close", "exit", "."]:
                with open('data_test.bin', 'wb') as f:
                    pickle.dump(address_book, f)
                print("Good bye!\nHope see you soon!")
                if note_list:
                    NoteRecord().note_serialize(note_list)
                break
            else:
                command_dict = {1: "add contact", 2: "add notes", 3: "add tag", 4: "show contact",
                                5: "show birthday", 6: "show all", 7: "show note", 8: "edit contact",
                                9: "edit note", 10: "search tags", 11: "sort folders", 12: "delete contact",
                                13: "delete note", 14: "help", 15: "reference", 16: "close",
                                17: "exit", 18: "good bye"}
                for value in command_dict.values():
                    ratio = int(difflib.SequenceMatcher(None, command, value).ratio() * 100)
                    if ratio > 50:
                        fixed_string = value[0] + value[1:]
                        print(f"You entered unknown command <<{command}>>. Maybe it`s <<{fixed_string}>>? Try again.")
                    elif ratio < 50:
                        continue
        except IndexError:
            print("Wrong input! Entered information is not enough for operation!")
        except KeyError:
            print("Wrong input! Check entered information!")


def help_command():
    """
    =====================================================
                 CLI - Command Line Interface
                       Personal Assistant
    =====================================================

    Personal Assistant works with Address book, write,
    save Notes and sort files in folders.

    Personal Assistant has a commands:
    1. "add contact" - for add name, address, contact
    information (phone, e-mail) and birthday to Address
    book write "add" then all details and enter it;

    2. "add notes" - for add notes write "add notes" then
    your note and enter it;

    3. "add tag" - for add tag to notes write "add tag"
    then some few words from note and enter it;

    4. "show contact" - for get all contact information
    write "show contact" then name and enter it;

    5. "show birthday" - for show a list of contacts who
    have a birthday after a specified number of days from
    the current date write "show birthday" then number of
    days and enter it;

    6. "show all" - for show all contacts in Address book
    write "show all" and enter command;

    7. "show note" - for search note write "show note"
    then title or tag and enter it;

    8. "edit contact" - for edit contact information write
    "edit contact" then name and enter it;

    9. "edit notes" - for edit notes write "edit notes"
    then title and enter it;

    10. "search tags" - for search and sort notes by tags
    write "search tags" then tag and enter it;

    11. "sort folders" - for sort files in folders write
    "sort folders" then path to folder and enter it;

    12. "delete contact" - for delete name and contact
    information in Address book write "delete contact" then
    name and enter it;

    13. "delete note" - for delete note write "delete note"
    then title and enter it;

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

