import argparse

contacts = []

def create_contact(first_name, last_name, email):
    contact = {
        'first_name': first_name, 
        'last_name': last_name, 
        'email': email, 
    }
    contacts.append(contact)
    print(f'Contact created!')

def list_contacts():
    if len(contacts) == 0:
        print("Contact list empty")
    else: 
        for contact in contacts: 
            print(f"First Name: {contact['first_name']}\nLast Name: {contact['last_name']}\nEmail: {contact['email']}\n")

def find_contacts(first_name): 
    found_contacts = []
    for contact in contacts:
        if contact['first_name'].lower() == first_name.lower():
            found_contacts.append(contact)
    if len(found_contacts) == 0:
        print(f"No contacts found with the first name: {first_name}")
    else: 
        print(f"Found {len(found_contacts)} contact(s) with the first name: {first_name}")
        for contact in found_contacts:
            print(f"First Name: {contact['first_name']}\nLast Name: {contact['last_name']}\nEmail: {contact['email']}\n")

def main():
    parser = argparse.ArgumentParser(description="Contact List")

    subparsers = parser.add_subparsers(dest='command', help='Available commands')

# create contact command 
create_parser = subparsers.add_parser('create', help='Create a new contact')
create_parser.add_argument('first_name', help='First name of contact')
create_parser.add_argument('last_name', help='Last name of contact')
create_parser.add_argument('email', help='Email of contact')

# List contacts command 
subparsers.add_parse('list', help='List all contacts')

# Find contact command 
find_parser = subparsers.add_parser('find', help='Find a contact by first name')
find_parser.add_argument('first_name', help='First name of the contact to find')

args = parser.parse_args()

if args.command == 'create':
        create_contact(args.first_name, args.last_name, args.email)
elif args.command == 'list':
        list_contacts()
elif args.command == 'find':
        find_contact(args.first_name)
else:
        print("Invalid command")

if __name__ == '__main__':
    main()