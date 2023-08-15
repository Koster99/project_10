from collections import UserDict

class Field:
    def __init__(self, value=None):
        self.value = value

class Name(Field):
    pass

class Phone(Field):
    pass

class Record:
    def __init__(self, name, phone):
        self.name = Name(name)
        self.phones = [Phone(phone)]

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def remove_record(self, record_name):
        if record_name in self.data:
            del self.data[record_name]

    def get_record(self, record_name):
        return self.data.get(record_name)

    def __getitem__(self, record_name):
        return self.get_record(record_name)

# Test code
if __name__ == "__main__":
    name = 'Bill'
    phone = '1234567890'
    rec = Record(name, phone)
    ab = AddressBook()
    ab.add_record(rec)
    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].phones, list)
    assert isinstance(ab['Bill'].phones[0], Phone)
    assert ab['Bill'].phones[0].value == '1234567890'
    print('All Ok')
