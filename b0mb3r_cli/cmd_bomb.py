import json
import requests
import subprocess
import re
import time

# 27.08.2020

print("This script is written exclusively for b0mb3r. Developer Koval Yaroslav. (github.com/koval01)")
print("If you are using Linux on a server (VPS / VDS) then you may have problems with Cyrillic. It is necessary to Russify the system.")
lang = input("Select lang (EN, UA, RU): ")

def spam_start(phone, cycles, lang, time_while, port):
	phone = re.sub(r'[^0-9.]+', r'', phone)
	cycles = re.sub(r'[^0-9.]+', r'', cycles)
	time_while = re.sub(r'[^0-9.]+', r'', time_while)
	port = re.sub(r'[^0-9.]+', r'', port)
	if port == '':
		port = str('8080')
	if lang == "EN":
		print('b0mb3r starting...')
	elif lang == "UA":
		print('Запуск b0mb3r...')
	elif lang == "RU":
		print('Запуск b0mb3r...')
	if port == '8080' or port == '':
		bomb_start = subprocess.Popen("b0mb3r --only-api")
	elif port != '8080':
		bomb_start = subprocess.Popen("b0mb3r --only-api --port " + str(port))
	time.sleep(10)
	try:
		spam_request = requests.post("http://127.0.0.1:{}/attack/start".format(str(port)), json={
			"number_of_cycles": int(cycles),
			"phone": int(phone)
			})
	except requests.exceptions.RequestException as e:
		print('Request (Start spam) error: {}'.format(str(e)))
	json_data = json.loads(spam_request.text)
	resp_status = str(json_data["success"])
	resp_id = str(json_data["id"])
	link_check_status = "http://127.0.0.1:{}/attack/".format(str(port)) + resp_id + "/status"
	if resp_status:
		spam_work = True
		temp_int_stat = 0
		if lang == "EN":
			print("The script has started. Cycle time - {}s, number of cycles - {}.".format(str(time_while), str(cycles)))
		elif lang == "UA":
			print("Сценарій розпочав роботу. Час циклу - {} секунд, кількість цилків - {}.".format(str(time_while), str(cycles)))
		elif lang == "RU":
			print("Сценарий начал работу. Время цикла - {} секунд, количество циклов - {}.".format(str(time_while), str(cycles)))
		while spam_work:
			try:
				status_check_request = requests.get(str(link_check_status))
			except requests.exceptions.RequestException as e:
				print('Request (Status check) error: {}'.format(str(e)))
			json_data_status = json.loads(status_check_request.text)
			resp_check_status_one = str(json_data_status["currently_at"])
			resp_check_status_two = str(json_data_status["end_at"])
			if int(temp_int_stat) < int(resp_check_status_one):
				print("Progress - {}/{}".format(resp_check_status_one, resp_check_status_two))
			temp_int_stat = int(resp_check_status_one)
			if int(resp_check_status_one) == int(resp_check_status_two):
				if lang == "EN":
					print("Spam finish!")
				elif lang == "UA":
					print('Спам завершено!')
				elif lang == "RU":
					print("Спам завершен!")
				spam_work = False
			time.sleep(int(time_while))
	if lang == "EN":
		exit("b0bm3r cli completed the work, so it was closed.")
	elif lang == "UA":
		exit("b0bm3r cli завершив роботу, тому був закритий.")
	elif lang == "RU":
		exit("b0bm3r cli завершил работу, поэтому был закрыт.")

if lang == "EN":
	print("What port you want use?")
	port = input("Work port: ")
	print("Example of entering a phone number for Ukraine - +380985577999 or 380985577999")
	phone = input("Phone number: ")
	print("Do not enter too large a value, 50-100 is recommended")
	cycles = input("Cycles count: ")
	print("For example, if you want to run this script on the server at night, it is desirable to put 30 seconds or more.\nIf you run the script on phones or PCs, you can put 2 seconds or for example 0.5")
	time_while = input("Time while: ")
	spam_start(phone, cycles, lang, time_while, port)
elif lang == "UA":
	print("Який порт ви хочете використовувати?")
	port = input("Робочий порт: ")
	print("Приклад вводу номера телефону для України - +380985577999 або 380985577999")
	phone = input("Номер телефону: ")
	print("Не вводьте занад-то велике значення, рекомендовано 50-100")
	cycles = input("Кількість циклів: ")
	print("Наприклад, якщо ви хочете запустити цей скрипт на сервері на ніч, то бажано ставити 30 секунд, чи більше.\nЯкщо ви запускаєте скрипт на телефони чи ПК то можете поставити 2 секунди чи наприклад 0.5")
	time_while = input("Час циклу: ")
	spam_start(phone, cycles, lang, time_while, port)
elif lang == "RU":
	print("Какой порт вы хотите использовать?")
	port = input("Рабочий порт: ")
	print("Пример ввода номера телефона для Украины - +380985577999 или 380985577999")
	phone = input("Номер телефона: ")
	print("Не вводите слишком большое значение, рекомендуется 50-100")
	cycles = input("Количество циклов: ")
	print("Например, если вы хотите запустить этот скрипт на сервере на ночь, то желательно ставить 30 секунд, или больше.\nЕсли вы запускаете скрипт на телефоны или ПК то можете поставить 2 секунды или, например 0.5")
	time_while = input("Время цикла: ")
	spam_start(phone, cycles, lang, time_while, port)
else:
	print("Lang error!")
