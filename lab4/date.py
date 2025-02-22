from datetime import datetime, timedelta

#Task1
current_date = datetime.now()
new_date = current_date - timedelta(days=5)

print(f"Current date: {current_date.strftime('%Y-%m-%d')}")
print(f"Date five days ago: {new_date.strftime('%Y-%m-%d')}")

#Task2
current_date = datetime.now()
yesterday = current_date - timedelta(days=1)
tomorrow = current_date + timedelta(days=1)

print(f"Yesterday: {yesterday.strftime('%Y-%m-%d')}")
print(f"Today: {current_date.strftime('%Y-%m-%d')}")
print(f"Tomorrow: {tomorrow.strftime('%Y-%m-%d')}")

#Task3 
curr_date = datetime.now()
curr_without_microsec = curr_date.replace(microsecond=0)

print(f"Current datetime: {curr_date}")
print(f"Datetime without microseconds: {curr_without_microsec}")

#Task4
from datetime import datetime

date1_str = input("Enter the first date (YYYY-MM-DD HH:MM:SS): ")
date2_str = input("Enter the second date (YYYY-MM-DD HH:MM:SS): ")

date1 = datetime.strptime(date1_str, "%Y-%m-%d %H:%M:%S")
date2 = datetime.strptime(date2_str, "%Y-%m-%d %H:%M:%S")

difference_in_seconds = abs((date2 - date1).total_seconds())
print(f"The difference between the two dates is: {difference_in_seconds} seconds")
