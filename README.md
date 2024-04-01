```     
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
```

__PathMon__ - программа типо __traceroute__

Поясню за PM_config.json:
```
{
    "timeout": 1, <- время ожидания
    "createMap": true, <- создать карту или нет
    "mod": 0 <- если мод 0, то результат выводиться ввиде таблицы. Если мод 1, то выводиться шаг и ip узла.
}
```
Также для программы надо установить нужные модули. Для этого запустите **`pathmon-install-needs-modules.bat`**, если вы на windows, или **`pathmon-install-needs-modules`**, если вы на linux. Будут установлены следующие модули:
- **prettytable**
- **scapy**
- **requests**
- **folium**