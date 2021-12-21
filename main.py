from classes.Zamowienie import Order
from classes.Dieta import Diet
from classes.Pacjent import Patient


patient_1 = Patient('David', 'Smith', '9th Street 13 Paris', 35)
diet_1 = Diet('Low carb', 2400, 'Regular', 37)
diet_2 = Diet('Standard', 2100, 'Vegan', 25)

order_1 = Order()
order_1.order_id = '1000'
order_1.diets = [diet_1, diet_2]
order_1.patient = patient_1
order_1.status = 'In progress'

print(order_1)
