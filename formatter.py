import string

format_list = ["first.last", "last.first", "firstl", "lfirst", "flast", "lastf", "first", "last"]

def email_formatter(name, emailformat):

	firstname, lastname = craft_mailbox(name)

	domain = emailformat[emailformat.find('@'):]
	mailbox_scheme = emailformat[:emailformat.find('@')]

	val = craft_email(mailbox_scheme, firstname, lastname, domain)

	return val

def craft_mailbox(name):
	val = name.split()
	firstname = ""
	lastname = ""
	if len(val) > 3:
		val = val[:3]
	if len(val) == 2:
		firstname = val[0]
		lastname = val[1]
	elif len(val) == 3:
		firstname = val[0]
		if val[1].isupper():
			lastname = val[2]
		else:
			lastname = val[1]
	else:
		#name length is 1
		firstname = val[0]
		lastname = "none"

	#remove punctuation from last name
	translator = str.maketrans('', '', string.punctuation)
	lastname = lastname.translate(translator)

	return firstname.lower(),lastname.lower()

def craft_email(mailbox_scheme, firstname, lastname, domain):
	if mailbox_scheme == "first.last":
		return firstname + "." + lastname + domain
	elif mailbox_scheme == "last.first":
		return lastname + "." + firstname + domain
	elif mailbox_scheme == "firstl":
		return firstname + lastname[0] + domain
	elif mailbox_scheme == "lfirst":
		return lastname[0] + firstname + domain
	elif mailbox_scheme == "flast":
		return firstname[0] + lastname + domain
	elif mailbox_scheme == "lastf":
		return lastname + firstname[0] + domain
	elif mailbox_scheme == "first":
		return firstname + domain
	elif mailbox_scheme == "last":
		return lastname + domain


#used in main function to check if email scheme from user is valid
def get_name_mailbox(email):
	name_mailbox = email[:email.find('@')]
	return name_mailbox

#used in main function to check if csv file ends in .csv_file
def check_if_csv(filename):
	if filename[-4:] == ".csv":
		return True
	return False
