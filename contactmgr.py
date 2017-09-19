class Contact():

    def __init__(self, name, phonenumber, gender, email, postal_address):
        self.name = name
        self.phonenumber = phonenumber
        self.gender = gender
        self.email = email
        self.postal_address = postal_address

    def __repr__(self):
        return "New Contact added Name:{} PhoneNumber: {} Gender: {} Email: {} Postal Address: {}"\
            .format(self.name, self.phonenumber, self.gender, self.email, self.postal_address)


def new_contact():
    name = input('Enter the name : ')
    phonenumber = input('Enter a phonenumber : ')
    gender = input('Enter the gender : ')
    email = input('Enter the email : ')
    postal_address = input("Enter the Postal Address :  ")
    new_contact = Contact(name, phonenumber, gender, email, postal_address)
