import smtplib


adrs = ''
psw = ''


class Guest:
    guests = {}

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def save(self):
        Guest.guests[self.name] = self.email

    # def send_email(self, name):
    #     if name in Guest.guests:
    #         if len(name) % 2 != 0:
    #             print(Guest.guests[name])
    #     else:
    #         return "Thank you for coming"


def run():
    print('Welcome to MEST Guestbook')
    print('/*===============================*/')
    print('Enter c to exit')
    name = raw_input('Enter your name : ')
    email = str(raw_input('Enter your email : '))
    new_guest = Guest(name, email)
    new_guest.save()
    for name in Guest.guests.keys():
        if len(name) % 2 != 0:
            to = Guest.guests[name]
            smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
            smtpserver.ehlo()
            smtpserver.starttls()
            smtpserver.ehlo()
            smtpserver.login(adrs, psw)
            header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:MEST \n'
            print header
            msg = header + '\n Thank you for coming, However you are not invited to future events!!!\n\n'
            smtpserver.sendmail(gmail_user, to, msg)
            print 'done!'
            smtpserver.close()


if __name__ == '__main__':
    run()
    print Guest.guests
