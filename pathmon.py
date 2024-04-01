LOGO = '''
                                               _____     ______ 
                                               |   |     | \/ | 
   ________   ________  __________  __    __   ¯¯|¯¯\___ ¯¯¯¯¯¯  ___        ___  ______  ___   ___
   |   _   \ /  ____  \ |___   ___| | |   | |   ¯¯¯     \ P      |  \      /  | /  __  \ |  \  |  |
   |  |_|  | | |____| |     | |     | |___| |    _______/        |   \    /   | | |  | | |   \ |  |
   |   ____/ |  ____  |     | |     | _____ |   /   P            |    \  /    | | |  | | |    \|  |
   |  |      | |    | |     | |     | |   | |   \______ _____    |  |\ \/ /|  | | |  | | |  |\    |
   |  |      | |    | |     | |     | |   | |           |   |    |  | \  / |  | | |__| | |  | \   |
   |__|      |_|    |_|     |_|     |_|   |_|           ¯¯|¯¯    |__|  \/  |__| \______/ |__|  \__|
                                                         ¯¯¯ 
   
'''

HELP_COMMAND = '''
Содержимое файла конфигурации PM_config.json (пример):
{
    "timeout": 1,       <- Время ожидания ответа от сервера
    "createMap": true,  <- Создание карты (когда пункт "mod" = 0). Принимаются значения true (создавать) или false (не создавать)
    "mod": 0            <- Режим мониторинга. 0 - выводить: IP, город, страну, провайдера, организацию. 1 - выводить только IP
}

Когда пункт "mod" = 0, программа подаёт API запрос на сайт http://ip-api.com. Пример запроса программы: http://ip-api.com/json/8.8.8.8
'''

from prettytable import PrettyTable
from threading import Thread
import scapy.all as scapy
import requests
import folium
import json
import time
import sys
import os

flag = False
table = PrettyTable()

try:
    with open('PM_config.json','r') as configFile:
        configFile = json.load(configFile)
except FileNotFoundError:
    data = {
      "timeout": 1,
      "createMap": True,
      "mod": 1
   }
    with open('PM_config.json','w') as writeConfigFile:
        json.dump(data, writeConfigFile, indent=4)
    input('[-] Файл конфигурации не был найден, поэтому он был создан')
    exit()

def __clearTerminal():
   if sys.platform == 'win32': os.system('cls')
   else: os.system('clear')

def __animation():
   sl = 0.1
   while flag is not True:
      if flag is False:
         __clearTerminal()
         print('''        
            ИДЁТ МОНИТОРИНГ МАРШРУТА        
   [                                          ]''')
         time.sleep(sl)
      else: break
      if flag is False:
         __clearTerminal()
         print('''        
            ИДЁТ МОНИТОРИНГ МАРШРУТА        
   [##                                        ]''')
         time.sleep(sl)
      else: break
      if flag is False:
         __clearTerminal()
         print('''        
            ИДЁТ МОНИТОРИНГ МАРШРУТА        
   [####                                      ]''')
         time.sleep(sl)
      else: break
      if flag is False:
         __clearTerminal()
         print('''        
            ИДЁТ МОНИТОРИНГ МАРШРУТА        
   [  ####                                    ]''')
         time.sleep(sl)
      else: break
      if flag is False:
         __clearTerminal()
         print('''        
            ИДЁТ МОНИТОРИНГ МАРШРУТА        
   [    ####                                  ]''')
         time.sleep(sl)
      else: break
      if flag is False:
         __clearTerminal()
         print('''        
            ИДЁТ МОНИТОРИНГ МАРШРУТА        
   [      ####                                ]''')
         time.sleep(sl)
      else: break
      if flag is False:
         __clearTerminal()
         print('''        
            ИДЁТ МОНИТОРИНГ МАРШРУТА        
   [        ####                              ]''')
         time.sleep(sl)
      else: break
      if flag is False:
         __clearTerminal()
         print('''        
            ИДЁТ МОНИТОРИНГ МАРШРУТА        
   [          ####                            ]''')
         time.sleep(sl)
      else: break
      if flag is False:
         __clearTerminal()
         print('''        
            ИДЁТ МОНИТОРИНГ МАРШРУТА        
   [            ####                          ]''')
         time.sleep(sl)
      else: break
      if flag is False:
         __clearTerminal()
         print('''        
            ИДЁТ МОНИТОРИНГ МАРШРУТА        
   [              ####                        ]''')
         time.sleep(sl)
      else: break
      if flag is False:
         __clearTerminal()
         print('''        
            ИДЁТ МОНИТОРИНГ МАРШРУТА        
   [                ####                      ]''')
         time.sleep(sl)
      else: break
      if flag is False:
         __clearTerminal()
         print('''        
            ИДЁТ МОНИТОРИНГ МАРШРУТА        
   [                  ####                    ]''')
         time.sleep(sl)
      else: break
      if flag is False:
         __clearTerminal()
         print('''        
            ИДЁТ МОНИТОРИНГ МАРШРУТА        
   [                    ####                  ]''')
         time.sleep(sl)
      else: break
      if flag is False:
         __clearTerminal()
         print('''        
            ИДЁТ МОНИТОРИНГ МАРШРУТА        
   [                      ####                ]''')
         time.sleep(sl)
      else: break
      if flag is False:
         __clearTerminal()
         print('''        
            ИДЁТ МОНИТОРИНГ МАРШРУТА        
   [                        ####              ]''')
         time.sleep(sl)
      else: break
      if flag is False:
         __clearTerminal()
         print('''        
            ИДЁТ МОНИТОРИНГ МАРШРУТА        
   [                          ####            ]''')
         time.sleep(sl)
      else: break
      if flag is False:
         __clearTerminal()
         print('''        
            ИДЁТ МОНИТОРИНГ МАРШРУТА        
   [                            ####          ]''')
         time.sleep(sl)
      else: break
      if flag is False:
         __clearTerminal()
         print('''        
            ИДЁТ МОНИТОРИНГ МАРШРУТА        
   [                              ####        ]''')
         time.sleep(sl)
      else: break
      if flag is False:
         __clearTerminal()
         print('''        
            ИДЁТ МОНИТОРИНГ МАРШРУТА        
   [                                ####      ]''')
         time.sleep(sl)
      else: break
      if flag is False:
         __clearTerminal()
         print('''        
            ИДЁТ МОНИТОРИНГ МАРШРУТА        
   [                                  ####    ]''')
         time.sleep(sl)
      else: break
      if flag is False:
         __clearTerminal()
         print('''        
            ИДЁТ МОНИТОРИНГ МАРШРУТА        
   [                                    ####  ]''')
         time.sleep(sl)
      else: break
      if flag is False:
         __clearTerminal()
         print('''        
            ИДЁТ МОНИТОРИНГ МАРШРУТА        
   [                                      ####]''')
         time.sleep(sl)
      else: break
      if flag is False:
         __clearTerminal()
         print('''        
            ИДЁТ МОНИТОРИНГ МАРШРУТА        
   [                                        ##]''')
         time.sleep(sl)
      else: break
      if flag is False:
         __clearTerminal()
         print('''        
            ИДЁТ МОНИТОРИНГ МАРШРУТА        
   [                                          ]''')
         time.sleep(sl)
      else: break
      
def __pathMon(host: str):
   global flag

   ttl = 0
   step = 0
   locations_list = []
   getAnsweredIP = []
   showAnsweredIP = []

   while ttl < 255:
      ttl += 1
      ans = scapy.sr(scapy.IP(dst=host,ttl=ttl)/scapy.ICMP(),timeout=configFile["timeout"],verbose=False)[0]
      for getAnsIP in ans:
         getAnsweredIP.append(getAnsIP[1].src)
      for writeAnsIP in getAnsweredIP:
         if writeAnsIP not in showAnsweredIP:
            showAnsweredIP.append(writeAnsIP)

   if configFile["mod"] == 0:
      table.field_names = ['Шаг','IP','Город','Страна','Провайдер','Организация']
      if configFile["createMap"] is True: mp = folium.Map()
      for i in range(len(showAnsweredIP)):
         step += 1
         response = requests.get(f'http://ip-api.com/json/{showAnsweredIP[i]}')
         with open(f'{showAnsweredIP[i]}.json','w') as file:
            json.dump(response.json(), file, indent=4)
         with open(f'{showAnsweredIP[i]}.json','r') as file:
            res = json.load(file)
         try:
            table.add_row([f'{step}',f'{showAnsweredIP[i]}',f'{res["city"]}',f'{res["country"]}',f'{res["isp"]}',f'{res["org"]}'])
            loc = [res["lat"], res["lon"]]
            locations_list.append(loc)
            if configFile["createMap"] is True:
               folium.Marker(location=loc, popup=f'{showAnsweredIP[i]}', icon=folium.Icon(color='gray')).add_to(mp)
         except KeyError:
            table.add_row([f'{step}',f'{showAnsweredIP[i]}','-','-','-','-'])
         os.remove(f'{showAnsweredIP[i]}.json')
      if configFile["createMap"] is True:
         folium.PolyLine(
            locations=locations_list,
            color='black',
         ).add_to(mp)
         mp.save(f'PM_result_{host}.html')
      flag = True
      __clearTerminal()
      print(table)
      input('\n[i] Карта сохранена')
   elif configFile["mod"] == 1:
      flag = True
      __clearTerminal()
      for i in range(len(showAnsweredIP)):
         step += 1
         print(f'Шаг: {step}, IP: {showAnsweredIP[i]}')
      input()


__clearTerminal()

print(LOGO)
print(f'''[i] Конфигурация файла PM_config.json:
      Время ожидания: {configFile["timeout"]}, 
      Создание карты: {configFile["createMap"]}, 
      Режим мониторинга: {configFile["mod"]}
''')
getHost = str(input('Укажите хост или IP -> '))
if getHost == 'help':
   __clearTerminal()
   input(HELP_COMMAND)

threadOne = Thread(target=__animation, args=()).start()
threadTwo = Thread(target=__pathMon, args=(getHost,)).start()