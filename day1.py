#this is the day1 challenge

"""  
Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly
rate for hours worked above 40 hours
"""

hours = float(input("Enter Hours: "))
rate = float(input("Enter rate: "))


if hours >= 40:
    print("Extratime")
    rate = rate * 1.5
else:
    print("Normal")

pay = hours * rate


print("Pay: ", pay)
