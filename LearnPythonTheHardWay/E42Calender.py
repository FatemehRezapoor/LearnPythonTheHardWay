# July 2020
# Calender in Python

import calendar

# ** PLAIN TEXT CALENDER **
c=calendar.TextCalendar(calendar.SUNDAY) # This means the calender is starting from sunday
st=c.formatmonth(2020,7,0,0)
print(st)
cn=calendar.TextCalendar(calendar.MONDAY)
st=cn.formatmonth(2020,7,0,0)
print(st)

# ** HTML CALENDER **
HC=calendar.HTMLCalendar(calendar.SUNDAY)
hst=HC.formatmonth(2020,7)
print(hst)

# ** ITERATE THE CALENDAR
for i in c.itermonthdates(2020,8):
    print(i)

# ** LOCAL CALENDARS : Consider the location of the user

for name in calendar.month_name:
    print(name)

for day in calendar.day_name:
    print(day)

# Challenge: You have a meeting for each first Friday of the month and you want to get a list of dates for those Fridays

print('Team meeting is on:')
for i in range(1,13):
    cal=calendar.monthcalendar(2018,i)
    print(i)
    weekone=cal[0]
    weektwo=cal[1]
    if weekone[calendar.FRIDAY]!=0:
        meetday=weekone[calendar.FRIDAY]
    else:
        meetday=weektwo[calendar.FRIDAY]
    print((calendar.month_name[m],meetday))
print(cal)



