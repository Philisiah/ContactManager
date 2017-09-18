class Contact():

    def __init__(self, name, phonenumber, gender, email, postal_address):
        self.name = name
        self.phonenumber = phonenumber
        self.gender = gender
        self.email = email
        self.postal_address = postal_address

    def __repr__(self):
        return "New Contact added Name:{} PhoneNumber:{} Gender: {} Email: {} Postal Address {}"\
            .format(name, phonenumber, gender, email, postal_address)


def get_input():

    print('Enter contact details')
    print('Enter name:')
    name = input()
    print('Enter phonenumber')
    phonenumber = input()
    print('Enter gender')
    gender = input()
    print('Enter email')
    email = input()
    print('postal_address')
    postal_address = input()

    NewUser = Contact(name, phonenumber, gender, email, postal_address)
