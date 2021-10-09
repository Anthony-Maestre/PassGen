import PySimpleGUI as sg
import generator

sg.theme('DarkBlue17')

layout = [[sg.Text('¿Cuáles son los requisitos de la contraseña?')],
		  [sg.Text('Nombre su contraseña:'), sg.InputText(key="nam", size=(10,))],
		  [sg.Text('Tamaño de la contraseña:'), sg.InputText(key="len", size= (2,))],
		  [sg.Checkbox('¿Necesita minúsculas?', default=False, key="low")],
		  [sg.Checkbox('¿Necesita mayúsculas?', default=False, key="upp")],
		  [sg.Checkbox('¿Necesita números?', default=False, key="num")],
		  [sg.Checkbox('¿Necesita caracteres especiales?', default=False, key="spe")],
		  [sg.Ok(), sg.Cancel()]]

window = sg.Window('Generador de contraseñas', layout)
event, values = window.read()
window.close()

generator.generate(event, values)

sg.popup(f'Su contraseña generada es: {f_pass}', button_type= 5)
