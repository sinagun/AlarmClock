import datetime

alarmHour = int(input("enter the time "))
alarmMinute= int(input("enter the time "))
amPm =str(input("am or pm"))
if (amPm== "pm"):
    alarmHour=alarmHour + 12
while (1==1):
    if (alarmHour==datetime.datetime.now().hour and alarmMinute == datetime.datetime.now().minute):
        print("wake up")
        break
print("exited")