import datetime
year = int(input("What year were you born in? "))
month = int(input("What month were you born in? "))
day = int(input("What day were you born on? "))

if datetime.date(year,month,day).weekday() == 0:
    print("Monday")
elif datetime.date(year,month,day).weekday() == 1:
    print("Tuesday")
elif datetime.date(year,month,day).weekday() == 2:
    print("Wednesday")
elif datetime.date(year,month,day).weekday() == 3:
    print("Thursday")
elif datetime.date(year,month,day).weekday() == 4:
    print("Friday")
elif datetime.date(year,month,day).weekday() == 5:
    print("Saturday")
else:
    print("Sunday")