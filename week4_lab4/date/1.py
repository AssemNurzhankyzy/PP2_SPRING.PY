#Write a Python program to subtract five days from current date.

from datetime import date,  timedelta, datetime
current = date.today() - timedelta(5)
print("Current time: ", date.today())
print("Five days ago : ",current)