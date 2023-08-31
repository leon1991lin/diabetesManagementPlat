from datetime import date
import calendar

def getAge(born_day):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if type(born_day) == date:
        born_day = born_day.strftime("%Y-%m-%d")
    born_str_list = born_day.split("-")
    today = date.today()

    year = today.year - int(born_str_list[0])
    month = today.month - int(born_str_list[1])

    if month < 0:
        year  -= 1
        month += 12
    if calendar.isleap(today.year):
        month_days[1] = 29
    day = today.day - int(born_str_list[2])
    if day<0:
        month -= 1
        if month<0:
            year -= 1
            month+= 12
        day = month_days[month] + day
    print(f"year:{year}, month:{month}, day:{day}")
    return year

if __name__ == '__main__':
    getAge("1991-08-30")