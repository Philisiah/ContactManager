import re

# text = 'abbaaabbbbaaaaa'

# pattern = 'ab'

# for match in re.findall(pattern, text):
#     print('Found {}'.format(match))
stri = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'

emails = re.findall(r'[\w\.-]+@[\w\.-]+', stri)
for email in emails:
	print (email)
