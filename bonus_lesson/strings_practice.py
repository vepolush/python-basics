import constants
import templates

name = input(templates.MSG_ENTER_NAME)

# name = "Олександр"
service = "пломбування зуба"
address = "Канатна 22"
smile = "🦷"
smile = ""

# sms = name + service + address
# sms = "Шановний " + name + ", ми Вас очікуємо на послугу " + service + " за адресою " + service
sms = f"Щановний {name}, ми Вас очікуємо на послугу {service} за адресою {address}{smile}"
sms2 = templates.SMS_TEMPLATE.format(name=name, service="шиномонтаж", address=constants.ADDRESS, smile="🏎")
print(f"{sms2}")

print(sms)