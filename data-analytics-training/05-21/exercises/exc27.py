from datetime import date 

def calculate_day(date):
    print(date.weekday()) # Precisaria fazer um if else gigante
    print(date.strftime('%A'))

today = date.today()
calculate_day(today)
