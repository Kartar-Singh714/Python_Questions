# This program is related to find the days left if the person age is for example lasts to 90 years.

age = int(input("Enter your age: "))
days, weeks, months, last_age= 365, 52, 12, 90
days_left= last_age*days - age*days
week_left = last_age*weeks - age*weeks
month_left = last_age*months - age*months
years_left = last_age - age
print(f"You have {days_left} days, {week_left} weeks, {month_left} months left, {years_left} years left ")


#######  Approach2  #######
y_left = last_age - age
d_left = y_left*days
m_left = y_left*months
w_left = y_left*weeks
print(f" NEW !! You have {d_left} days, {w_left} weeks, {m_left} months left, {y_left} years left ")