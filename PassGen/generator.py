import random
import string

low_letts = list(string.ascii_lowercase)
upp_letts = list(string.ascii_uppercase)
digits = list(string.digits)
spe_chars = list(string.punctuation)
chars = list()

def generate(event, values):
	length = int(values['len'])
	password = []
	
	if values['low'] == True:
		password.append(random.choice(low_letts))
		if not string.ascii_lowercase in chars:
			chars.extend(string.ascii_lowercase)
	if values['upp'] == True:
		password.append(random.choice(upp_letts))
		if not string.ascii_uppercase in chars:
			chars.extend(string.ascii_uppercase)
	if values['num'] == True:
		password.append(random.choice(digits))
		if not string.digits in chars:
			chars.extend(string.digits)
	if values['spe'] == True:
		password.append(random.choice(spe_chars))
		if not string.punctuation in chars:
			chars.extend(string.punctuation)

	if len(password) < length:
		random.shuffle(chars)
		for i in range(length - len(password)):
			password.append(random.choice(chars))

	random.shuffle(password)

	f_pass = "".join(password)
	pass_nam = values["nam"]

	with open('password.txt', 'w') as f:
		f.write(f'\n{f_pass} = {pass_nam}')

	return f_pass