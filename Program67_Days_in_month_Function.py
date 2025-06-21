def check_leap(y):
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 ==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
def day_in_month(year, month):
    if month == 2:
        is_leap = check_leap(year)
        if is_leap:
            days = 29
        else:
            days = 28
    elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12 :
        days = 31
    else:
        days = 30
    return days

year = input("Please enter the Year: ")
month = input("Please enter the month as numeric: ")

if year.isdigit() and month.isdigit():
    if 3000 > int(year) > 1800 and 1 <= int(month) <= 12:
         total_days= day_in_month(int(year), int(month))
         print(f"Total number of days are: {total_days}")
    else:
        print("Year should be within range of 1800 to 3000 and Month numeric value should also between 1-12")
else:
    print("Invalid year or month")