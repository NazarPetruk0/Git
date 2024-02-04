from datetime import datetime as dtdt

def get_days_from_today(date):
    try:
        user_date = dtdt.strptime(date, '%Y-%m-%d')
        current_date = dtdt.today()
        date_difference = current_date - user_date
        return date_difference.days
    except ValueError:
        return "Неправильний формат дати. Використовуйте 'РРРР-ММ-ДД'."

print(get_days_from_today("2021-10-13"))