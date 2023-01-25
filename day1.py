#this is the day1 challenge

"""  
Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly
rate for hours worked above 40 hours
"""

hours = float(input("Enter Hours: "))
rate = float(input("Enter rate: "))


if hours >= 40:
    status = "extra"
    rate = rate * 1.5
else:
    status = "Normal"

pay = hours * rate


print(f"The payment is: ${pay} because you works {status} time")
