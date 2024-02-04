from datetime import datetime as dtdt, timedelta

def get_upcoming_birthdays(users):
    today = dtdt.today().date()
    upcoming_birthdays = []
    for user in users:
        birthday = dtdt.strptime(user["birthday"], "%Y.%m.%d").date().replace(year=today.year)
        if birthday < today:
            birthday = birthday.replace(year=today.year + 1)
        days_until_birthday = (birthday - today).days
        congratulation_date = birthday
        if days_until_birthday > 7:
            continue
        elif days_until_birthday == 0:
            congratulation_date = today
        elif days_until_birthday < 0:
            continue
        elif today.weekday() == 5: 
            congratulation_date += timedelta(days=2)
        elif today.weekday() == 6:
            congratulation_date += timedelta(days=1)
        upcoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date.strftime("%Y.%m.%d")})
    return upcoming_birthdays

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.28"}
]
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
