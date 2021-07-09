#! /usr/bin/python

import addressbook_pb2
import sys

def add_jane_doe(address_book):
    person = address_book.people.add()

    # Fill person's fields
    person.id = 4321
    person.name = "Jane Doe"
    person.email = "jane@example.com"

    # Add PhoneNumber's
    mobile_phone = person.phones.add()
    mobile_phone.number = "555-1234"
    mobile_phone.type = addressbook_pb2.Person.MOBILE

    work_phone = person.phones.add()
    work_phone.number = "555-3456"
    work_phone.type = addressbook_pb2.Person.WORK

def print_address_book(address_book):
    for person in address_book.people:
        print("Person ID:", person.id)
        print("  Name:", person.name)

        if person.HasField('email'):
            print("  E-mail address:", person.email)

        for phone_number in person.phones:
            if phone_number.type == addressbook_pb2.Person.PhoneType.MOBILE:
                print("  Mobile phone #:", phone_number.number)
            elif phone_number.type == addressbook_pb2.Person.PhoneType.HOME:
                print("  Home phone #:", phone_number.number)
            elif phone_number.type == addressbook_pb2.Person.PhoneType.WORK:
                print("  Work phone #:", phone_number.number)


if len(sys.argv) != 2:
    print("Usage:", sys.argv[0], "ADDRESS_BOOK_FILE")
    sys.exit(-1)

# Create an AddressBook and add a Person to it
address_book = addressbook_pb2.AddressBook()
person = address_book.people.add()

# Fill person's fields
person.id = 1234
person.name = "John Doe"
person.email = "jdoe@example.com"

# Add a PhoneNumber
phone = person.phones.add()
phone.number = "555-4321"
phone.type = addressbook_pb2.Person.HOME

print("\nInitial address book:\n")
print_address_book(address_book)

# Write the address to disk
f = open(sys.argv[1], "wb")
f.write(address_book.SerializeToString())
f.close()

# Read the existing address book from disk
f = open(sys.argv[1], "rb")
address_book.ParseFromString(f.read())
f.close()

# Add a second person to the address book
add_jane_doe(address_book)

print("\nModified Address book:\n")
print_address_book(address_book)

# Write the address to disk
f = open(sys.argv[1], "wb")
f.write(address_book.SerializeToString())
f.close()