E = '\x1b[1;31m'
G = '\x1b[1;32m'
S = '\x1b[1;33m'
Z = '\x1b[1;31m'
X = '\x1b[1;33m'
Z1 = '\x1b[2;31m'
F = '\x1b[2;32m'
A = '\x1b[2;39m'
C = '\x1b[2;35m'
B = '\x1b[2;36m'
Y = '\x1b[1;34m'
Z = '\033[1;31m' 
A = '\033[1;33m' 
Z1 = '\033[2;31m' 
F = '\033[2;32m' 
X = '\033[2;34m'
C = '\033[2;35m' 
S = '\033[2;36m' 
Y = '\033[1;34m' 
import requests
import time
def telegram_bot_sendtext(bot_message):

	print(S+""" 
  ______  _____    ____     _____ 
 |___  / |_   _|  / __ \   / ____|
    / /    | |   | |  | | | (___  
   / /     | |   | |  | |  \___ \ 
  / /__   _| |_  | |__| |  ____) |
 /_____| |_____|  \____/  |_____/ 
                                  
                                  
                                  
                                  



""")
	print(E+"Telegram Anonim Mesaj Göndrme")
	time.sleep(1.50)
	devam=input(E+"Devam Etmek İçin Enter a Basın")
	time.sleep(1.20)
	print(S+"Tool Başlatılıyor Lütfen Bekleyiniz.......")
	time.sleep(2.50)
	tok=input(F+'Token Giriniz:')
	id =input(F+'ID Giriniz:')
	
	send_text = 'https://api.telegram.org/bot' + tok + '/sendMessage?chat_id=' + id + '&parse_mode=Markdown&text=' + bot_message
	response = requests.get(send_text)
	return response.json()
	
test = telegram_bot_sendtext("SA BEN @zioscoder ")
