import random
import string
import PySimpleGUI as sg

sg.theme('DarkBlue17')
low_letts = list(string.ascii_lowercase)
upp_letts = list(string.ascii_uppercase)
digits = list(string.digits)
spe_chars = list(string.punctuation)
chars = list()

#Obtenemos los parametros para la contraseña en esta interfaz
layout = [[sg.Text('¿Cuáles son los requisitos de la contraseña?')], 
		  [sg.Text('Nombre su contraseña:'), sg.InputText(key="nam", size=(10,))],
		  [sg.Text('Tamaño de la contraseña:'), sg.InputText(key="len", size=(2,))],
		  [sg.Checkbox('¿Necesita minúsculas?', default=False, key="low")],
		  [sg.Checkbox('¿Necesita mayúsculas?', default=False, key="upp")],
		  [sg.Checkbox('¿Necesita números?', default=False, key="num")],
		  [sg.Checkbox('¿Necesita caracteres especiales?', default=False, key="spe")],
		  [sg.Ok(), sg.Cancel()]]

window = sg.Window('Generador de contraseñas', layout)
event, values = window.read()
window.close()

#Se genera la contraseña usando los parametros ya obtenidos
def generate_random_password():
	length = int(values['len'])

	password = []
	
	if values['low'] == True:
		password.append(random.choice(low_letts))
		if not string.ascii_lowercase in chars: 
			chars.extend(string.ascii_lowercase) #Se añadira dependiendo de lo especificado
	if values['upp'] == True:
		password.append(random.choice(upp_letts))
		if not string.ascii_uppercase in chars: 
			chars.extend(string.ascii_uppercase) #Se añadira dependiendo de lo especificado
	if values['num'] == True:
		password.append(random.choice(digits))
		if not string.digits in chars: 
			chars.extend(string.digits) #Se añadira dependiendo de lo especificado
	if values['spe'] == True:
		password.append(random.choice(spe_chars))
		if not string.punctuation in chars: 
			chars.extend(string.punctuation) #Se añadira dependiendo de lo especificado

	if len(password) < length: #Aseguramos que la contraseña tenga el tamaño requerido
		random.shuffle(chars) 
		for i in range(length - len(password)):
			password.append(random.choice(chars)) #Se rellenaran los caracteres faltantes utilizando los requisitos ya especificados en la interfaz

	random.shuffle(password) #Se revuelven los caracteres en la contraseña

	f_pass = "".join(password)
	pass_nam = values["nam"]

	with open('password.txt', 'w') as f:
		f.write(f'\n{f_pass} = {pass_nam}')

	sg.popup(f'Su contraseña generada es: {f_pass}', button_type= 5)

generate_random_password()
