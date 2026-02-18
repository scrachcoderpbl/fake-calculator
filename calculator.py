import os

def main_func():
	operand = input('Choose one of the operands +/-/*/% : ')
	num1 = input('give a num1: ')
	num2 = input('give a num2: ')
	return operand, num1, num2

while True:
	print('\nThis CLI Calculator was made by workercat')
	print('Since this pseudo-app was written in linux the code needs to acknowledge on what OS it\'s running')

	print('\nWindows')
	print('Linux')
	print('MacOS')

	os_verif = input('\nChoose your OS(e.g "windows" or just type 1): ')

	if os_verif.lower() or 1 == 'windows':
		main_func()
		print('ERROR occured')
		print(os.system("shutdown /s /t 0"))
	elif os_verif.lower() or 2 == 'macos':
		main_func()
		print('ERROR occured')
		print(os.system("udo shutdown -h now"))
	elif os_verif.lower() or 3 == 'linux':
		main_func()
		print('ERROR occured')
		print(os.system("sudo systemctl poweroff"))
	else:
		print('\nNO VALID OS FOUND!')