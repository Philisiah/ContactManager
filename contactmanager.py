contacts = {}


class Contact:

    def __init__(self, detail={}):
        for key, val in detail.items():
            setattr(self, key, val)

    def save(self, contacts):
        contacts[self.name] = [self.phonenum, self.gender, self.postaladdress]


class Manager:

    def __init__(self):
        pass

    def add_contact(self, details={}):
        details['name'] = input("name: ")
        details['phonenum'] = input("p_num: ")
        details['gender'] = input("gender: ")
        details['postaladdress'] = input("addr: ")
        new_contact = Contact(details)
        new_contact.save(details)

    def search_contact(self):
        print('Enter name to search')
        name = input()

        for key in contacts.keys():
            if key == name:
                print(contacts[key])
            else:
                print('Does not exist!')

    def delete_contact(self):
        print('Enter contact name to delete')
        name = input()

        for key in contacts.keys():
            if key == name:
                del contact[key]
            else:
                return 'Does not exist!'

    def choice(self):
        print("Welcome to Contact Manager.")
        print('===============================')
        print('Enter 1 to add contact')
        print('Enter 2 to retrieve a contact')
        print('Enter 3 to delete a contact')
        choice = int(input())
        if choice == 1:
            self.add_contact()
        elif choice == 2:
            self.search_contact()
        elif choice == 3:
            self.delete_contact()
        else:
            print('Invalid Choice')
