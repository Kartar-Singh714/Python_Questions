#WAP to convert the Celsius temperature to Fahrenheit temp

c = input("Enter the temperature in the Celsius: ")
if c.replace(".","").isdigit():
    t=float(c)
    f_temp = (t*9/5)+32
    print(f"Temprature if farenheit is {f_temp}")
else:
  print("Invalid Number")
