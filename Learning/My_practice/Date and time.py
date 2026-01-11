#Creating a program to generate the date and time
from datetime import datetime

now: datetime = datetime.now()#the variable now is inheriting from datetime class
print(f"{now:%d.%m.%y (%H:%M:%S)}")#we use the %d-day , %m-month, %y-year and the 24 hour format %H-Hour ,%M-minute, %S- second
#to print the local time we use %c
print(f"{now: %c}")#The format: Thu Jul 25 09:29:03 2024-
#for the am and pm format we use %I%p
print(f"{now:%I%p}")



















