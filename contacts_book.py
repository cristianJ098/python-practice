import os

EXIT = 0
ADD = 1
SHOW = 2
SEARCH = 3
DELETE = 4
CLEAR = 5
separator = '~'*10

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
    