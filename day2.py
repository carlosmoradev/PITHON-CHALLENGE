# 100DaysOfCode day2

"""
Rewrite the pay program (day1) using try and except so taht your program handle
non-numeric input gracefully by printing a message and exiting the program.
The following shos two execution of the program:

Enter Hours: 20
Enter Rate: nine
Error, please enter numeric input

Enter Hours: forty
Error, please enter numeric input
"""
try:
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter rate: "))
    
    
    if hours >= 40:
        status = "extra"
        rate = rate * 1.5
    else:
        status = "Normal"
    
    pay = hours * rate
    print(f"The payment is: ${pay} because you works {status} time")

except:
    print("Error, please enter numeric input")



