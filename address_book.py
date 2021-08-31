from collections import UserDict
from datetime import timedelta, date, datetime
import re
import time


class Name:
    def __init__(self, name):
        self.__name = None
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        if name.isalpha():
            self.__name = name
        else:
            print("Incorrect name!")

    def __str__(self):
        return f"{self.__name}"


class Phone:
    def __init__(self, phone):
        self.__phone = None
        self.phone = phone

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone: str):
        if re.search("(^\+?(38)?0(67|68|96|97|98|50|66|95|99|63|73|93|89|94)\d{7}$)", re.sub(r'\D', "", phone)):
            if len(re.sub(r'\D', "", phone)) == 12:
                self.__phone = '+' + re.sub(r'\D', "", phone)
            else:
                self.__phone = '+38' + re.sub(r'\D', "", phone)

        else:
            print("Incorrect phone!")

    def __str__(self):
        return f"{self.__phone}"


class Email:
    def __init__(self, email):
        self.__email = None
        self.email = email

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        if re.search("^[\w\.-]+@[\w\.-]+(\.[\w]+)+", email):
            self.__email = email
        else:
            print("Incorrect email!")

    def __str__(self):
        return f"{self.__email}"


class Birthday:
    def __init__(self, birthday):
        self.__birthday = None
        self.birthday = birthday

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, birthday):
        try:
            if time.strptime(birthday, '%d/%m/%Y'):
                self.__birthday = birthday
        except ValueError:
            print('Incorrect date!\nTry to enter like the example: DD/MM/YYYY"')

    def __str__(self):
        return f"{self.__birthday}"


class Address:
    def __init__(self, address):
        self.address = address
        self.__address = address

    def __str__(self):
        return f"{' '.join(self.__address).title()}"


class Record:
    def __init__(self, name, phone, email, birthday, address):
        self.name = Name(name)
        self.phone = Phone(phone)
        self.email = Email(email)
        self.birthday = Birthday(birthday)
        self.address = Address(address)

    def __str__(self):
        return f"{self.phone},{self.email},{self.birthday},{self.address}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.__str__()] = record

    def find_contact(self, name):
        for key, value in self.data.items():
            if str(name) == str(key):
                print(f"{key}: {value}")

    def del_contact(self, name):
        self.data.pop(name)

    def days_to_birthday(self, number_days):
        EndDate = date.today() + timedelta(days=number_days)
        list = []
        try:
            for key, val in self.data.items():
                result = re.search(r"\d{1,2}\/\d{1,2}\/\d{4}", str(val)).group()
                if datetime.strptime(result, "%d/%m/%Y").month == EndDate.month\
                        and datetime.strptime(result, "%d/%m/%Y").day == EndDate.day:
                    list.append({str(key): str(val)})
        except AttributeError:
            pass
        return list

    def __str__(self):
        for key, val in self.data.items():
            print(f'{str(key)}:{str(val)}')
        print(f'Total contacts: {len(self.data)}')

