'''
Задание 4
Переделать скрипт из задания 3 таким образом, чтобы, при запросе параметра,
которого нет в словаре устройства, отображалось сообщение 'Такого параметра нет'.
Задание относится только к параметрам устройств, не к самим устройствам.
> Попробуйте набрать неправильное имя параметра  или несуществующий параметр,
> чтобы увидеть какой будет результат. А затем выполняйте задание.
Если выбран существующий параметр, вывести информацию о соответствующем параметре, указанного устройства.
Пример выполнения скрипта:
$ python task_5_1c.py
Введите имя устройства: r1
Введите имя параметра (ios, model, vendor, location, ip): ips
Такого параметра нет
Замечание – использование циклов и условного оператора запрещено
'''

devicesInfo = {
    "r1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.1",
    },
    "r2": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2",
    },
    "sw1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True,
    }
}
# Сохраняем в переменную значение которое ввел пользователь в кносоль
device = input("Enter device name: ")
# Сохраняем список ключей (параметрами устройства)
listOfDeviceParam = devicesInfo.get(device).keys()
# Выводим в консоль используя префикс * - чтоб убрать скобки [] и префикс dict_keys
print("Enter device parameter:", *listOfDeviceParam)
# Сохраняем в переменную значение которое ввел пользователь в консоль. И преобразовываем его в строку.
param = str(input())
# Находим значение по ключу. Если ничего не найдено - выводим сообщение.
print(devicesInfo.get(device).get(param, 'No such parameter'))