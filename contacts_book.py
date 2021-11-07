import os


ADD = 1
SHOW = 2
SEARCH = 3
DELETE = 4
CLEAR = 5
EXIT = 6
separator = '~'*10

def menu():
    print('''
{separator} Choose a option {separator}
{ADD} - Add contact
{SHOW} - Show my contacts
{SEARCH} - Search contact
{DELETE} - Delete Contact
{CLEAR} - Clear Contact Book
{EXIT} - Exit
''')

def add_contact(contact_book):
    os.system('cls')
    print(separator,'Add Contact', separator)
    val = 0
    while val == 0:
        name = input('Enter the contact name: ').capitalize()
        if name in contact_book:
            print('Contact already exist')
        else:
            val = 1
    phone = 0
    while phone == 0:
        try:
            phone = int(input('Enter a phone number: '))
        except:
            print('Invalid data, enter only numbers')
    email = 0
    while email == 0:
        try:
            email = input('Enter a E-mail: ')
            if '@' in email and '.' in email:
                break
        except:
            print('Invalid Email, try again')
    contact_book[name] = (phone, email)
    print('Contact added successfully')

def show_contact(contact_book):
    os.system('cls')
    print(separator, 'My Contacts', separator)
    if len(contact_book) > 0:
        for contact, data in contact_book.items():
            print(f'''
            Name: {contact}
            Phone: {data[0]}
            E-mail: {data[1]}
            {separator*3}
            ''')
    else:
        print('Empty Contact Book')

def search_contact(contact_book):
    os.system('cls')
    print(separator, 'Search contact', separator)
    if len(contact_book) > 0:
        name = 0
        while name == 0:
            try:
                name = input('Enter the name of the contact you want to find: ')
            except:
                print('Invalid data')
        cont = 0
        for contact, data in contact_book.items():
            if name in contact:
                print(f'''
            Name: {contact}
            Phone: {data[0]}
            E-mail: {data[1]}
            {separator*3}
            ''')
            cont +=1
        if cont == 0:
            print('No found contacts')
        else:
            print(f'{cont} contacts found')
    else:
        print('Empty Contact Book')

def delete_contact(contact_book):
    os.system('cls')
    print(separator, 'Delete Contact', separator):
    if len(contact_book) > 0:
        name = 0
        while name == 0:
            try:
                name = input('Enter the name of the contact you want to delete: ')
            except:
                print('Invalid data')
        if name in contact_book:
            del contact_book[name]
            print(separator, 'Contact deleted', separator)
        else:
            print('No found contacts')

def clear_contact(contact_book):
    os.system('cls')
    print(separator, 'Clear my Contact Book', separator)
    option = 0
    while option == 0:
        try:
            option = input('Do you really want to clear the Contact Book? yes/no: ')
        except:
            print('Invalid option')
    if option == 'yes' or option == 'y':
        contact_book = {}
    else:
        print('Aborting the process...')

def main():
    contact_book = {}
    process = True
    while process:
        os.system('cls')
        menu()
        option = 0
        while option == 0:
            try:
                option = int(input('Choose de option: '))
            except:
                print('Invalid Option, please enter a number')
        if option == ADD:
            add_contact(contact_book)
        elif option == SHOW:
            show_contact(contact_book)
        elif option == SEARCH:
            search_contact(contact_book)
        elif option == DELETE:
            delete_contact(contact_book)
        elif option == CLEAR:
            clear_contact(contact_book)
        elif option == EXIT:
            process = 0
        else:
            print('Invalid Option')







