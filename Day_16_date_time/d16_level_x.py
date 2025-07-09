# from datetime import datetime
# # current date and time
# now = datetime.now()
# t = now.strftime("%H:%M:%S")
# print("time:", t)
# time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# # mm/dd/YY H:M:S format
# print("time one:", time_one)
# time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
# # dd/mm/YY H:M:S format
# print("time two:", time_two)
# time_three = now.strftime("%A %d-%B-%Y, %I:%M:%S %p, %z")
# print("time three:", time_three)

# Get the current day, month, year, hour, minute and timestamp from datetime module
# ================================================================================================================
from datetime import datetime

date_time_now = datetime.now()
print("Full date and Time details:: ", date_time_now)
print("Current day::", date_time_now.day)
print("Current month::", date_time_now.month)
print("Current year::", date_time_now.year)
print("Current hour::", date_time_now.hour)
print("Current minute::", date_time_now.minute)
print("Current timestamp::", date_time_now.timestamp())


# Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
# ================================================================================================================
print("formatted date_time::", date_time_now.strftime("%m/%d/%Y, %H:%M:%S"))
print("formatted date_time::", date_time_now.strftime("%d-%b-%y, %I:%M:%S %p"))

# Today is 5 December, 2019. Change this time string to time.
date_string = "5 December, 2019"
date_time_obj = datetime.strptime(date_string, "%d %B, %Y")
print("date string to Time::", date_time_obj)
print("date string to Time::", date_time_obj.timestamp())

# Calculate the time difference between now and new year.
# ================================================================================================================

## With Date
from datetime import date
date_today = date.today()
date_new_year = date(day=2,month=1,year=2026)

## With datetime
# date_today = datetime.now()
# date_new_year = datetime.strptime("1-Jan-2026", "%d-%b-%Y")
print("Time diff to new year::", date_new_year-date_today)

# Calculate the time difference between 1 January 1970 and now.
# ================================================================================================================
date_today = date.today()
date_old = date(day=1,month=1,year=1970)

print("Time diff from an old date::", date_today-date_old)

from datetime import timedelta
delta_1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
print("delta :: ", delta_1)
# Think, what can you use the datetime module for? Examples:
# Time series analysis
# To get a timestamp of any activities in an application
# Adding posts on a blog

