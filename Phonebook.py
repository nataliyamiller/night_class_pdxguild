# New Phonebook
new_phonebook = ('Find Any Phone Number!')
print new_phonebook
first = raw_input ('First name ')
last = raw_input ('Last name ')
phone = raw_input ('Phone number ')
question = raw_input ("Are you trying to locate %s, %s, %s? " %(last, first, phone))

dictionary = {'holly': {'first_name': 'Holly', 'last_name': 'Oldin', 'phone': "503-277-9710"},
			'sam': {'first_name': 'Sam', 'last_name': 'Davis', 'phone': "503-971-6757"}}


def add():
	first_name = raw_input ('What\'s the first name? ').lower()
	last_name = raw_input ('what\'s the last name? ').lower()
	phone = raw_input ('What\'s the phone number? ')
	dictionary [first_name.lower()] = {'first_name': first_name, 'last_name': last_name, 'phone': phone}
	print 'Person successfully added:'
	print 'First_name: ' + dictionary [first_name.lower()]['first_name']
	print 'Last_name: ' + dictionary [first_name.lower()]['last_name']
	print 'Phone number: ' + dictionary [first_name.lower()]['phone']

def search():
	try:
		srch = raw_input ('What\'s the first name? ').lower()
		print 'First_name:' + dictionary [srch]['first_name']
		print 'last_name:'+ dictionary [srch]['last_name']
		print 'Phone:' + dictionary [srch]['phone']
	except:
		print 'This person does not exist. Would you like to add this person?: '

def help():
	show_help == raw_input ('Cannot find the person you are looking for?: ')
	if show_help == 'yes' or show

prompt = ('command (add/search/help)? ')
while True:
	command = raw_input (prompt)
	if command == 'search':
		search()

	if command == 'add':
		add ()

	if command == 'help'


else:
	print 	'Help options'	

