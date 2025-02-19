#Write a Python program to drop microseconds from datetime.

from datetime import date,timedelta,datetime
time = datetime.now()
withoutmiliseconds = time.strftime("%Y-%m-%d, %H:%M:%S")
print(withoutmiliseconds)