import datetime
print("todays date:",datetime.date.today())
Date=datetime.date.today()
print(Date.year)
print(Date.day)
print(Date.month)
print(Date.strftime('%A'))
Day1=datetime.date(2017,5,3)
Day2=datetime.date(2015,3,28)
day_difference=Day2-Day1
print(day_difference)

#creating the time delta
print(datetime.timedelta(days=3))
if Day1==Day2:
   print("equal")
elif Day1>Day2:
	print("not equal")
else:
	print("success")


  