def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def get_month_days(year, month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28
    else:
        return 30

def print_calendar(year, month):
    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
                   'August', 'September', 'October', 'November', 'December']

    print(month_names[month-1], year)
    print('Sun  Mon  Tue  Wed  Thu  Fri  Sat')
    
    starting_day = sum([get_month_days(year, m) for m in range(1, month)]) % 7
    print('     ' * starting_day, end='')
    
    for day in range(1, get_month_days(year, month) + 1):
        print(f'{day:2d}   ', end='')
        
        if (day + starting_day) % 7 == 0:
            print()
    
    print()

year = int(input("Enter the year: "))
month = int(input("Enter the month number(0-12): "))

print_calendar(year, month)

