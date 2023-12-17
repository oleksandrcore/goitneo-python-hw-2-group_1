from collections import UserDict


class Field:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def is_valid(self):
        return isinstance(self.value, str) and len(self.value) == 10


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, value):
        phone = Phone(value)

        if phone.is_valid():
            self.phones.append(phone)

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if old_phone == phone.value:
                phone._value = new_phone

    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone_number == phone.value:
                return phone

    def remove_phone(self, phone_number):
        for phone in self.phones:
            if phone_number == phone.value:
                self.phones.remove(phone)

    def __str__(self):
        joined_phones = '; '.join(p.value for p in self.phones)
        return f"Contact name: {self.name.value}, phones: {joined_phones}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, None)

    def delete(self, name):
        return self.data.pop(name, None)
