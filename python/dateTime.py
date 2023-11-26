# A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.
import datetime
x = datetime.datetime.now()
print(x) #2023-11-15 14:21:30.286869


x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))
# 2023
# Wednesday

x = datetime.datetime(2020, 5, 17)
print(x)


# The strftime() Method
# The datetime object has a method for formatting date objects into readable strings.
# The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:
x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))

# %a	Weekday, short version	Wed	
# %A	Weekday, full version	Wednesday
# %y	Year, short version, without century	18	
# %Y	Year, full version	2018
# %M	Minute 00-59	41	
# %S	Second 00-59
