import datetime
from credit.models import Credit, Client, Account

client = Client(name='Бердиев Н.Д.', birth_year="1994", citizenship="Кыргызстан", work_place='Codify')
client.save()

client_1 = Client(name='Темирболотов Манас', birth_year="1984", citizenship="Кыргызстан", work_place='Чанг Ан')


