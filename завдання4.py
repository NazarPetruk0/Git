import datetime as dt
from datetime import datetime as dtdt

def get_upcoming_birthdays(users=None):
    tdate=dtdt.today().date()
    birthdays=[]
    for user in users:
        bdate=user["birthday"] 
        bdate=str(tdate.year)+bdate[4:] 
        bdate=dtdt.strptime(bdate, "%Y.%m.%d").date() 
        week_day=bdate.isoweekday() 
        days_between=(bdate-tdate).days
        if 0<=days_between<7: 
            if week_day<6: 
                birthdays.append({'name':user['name'], 'birthday':bdate.strftime("%Y.%m.%d")})
            else:
                if (bdate+dt.timedelta(days=1)).weekday()==0:
                    birthdays.append({'name':user['name'], 'birthday':(bdate+dt.timedelta(days=1)).strftime("%Y.%m.%d")})
                elif (bdate+dt.timedelta(days=2)).weekday()==0: 
                    birthdays.append({'name':user['name'], 'birthday':(bdate+dt.timedelta(days=2)).strftime("%Y.%m.%d")})
    return birthdays

users = [
   {'name': 'Jake Smith', 'birthday': '1990.03.02'},
{'name': 'John Doe', 'birthday': '1985.03.05'},
{'name': 'Ethan Williams', 'birthday': '1970.02.29'},
{'name': 'Smith Smith', 'birthday': '1990.03.06'}
]
print(get_upcoming_birthdays(users))
