#nested if condition
age=int(input("Enter your age :" ))
height= int(input("Enter your height :"))
if height>=120:
    print("You can ride")
    if age<=12 :
        print("Ticket rate is 5$")
    elif age<=18 :
        print("ticket rate is 18$")
    else :
        print("ticket rate is 19$")
else :
    print("You can't Ride")
    
