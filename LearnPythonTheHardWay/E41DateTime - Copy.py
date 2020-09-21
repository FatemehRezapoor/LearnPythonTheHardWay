# July 2020
# Date and Time
from datetime import date # From datetime module I am importing date time classes
from datetime import time
from datetime import datetime

#TODAY DATE
today=date.today() # we created an object from today class
print('Today date is:{}'.format(today))

# INDIVIDUAL COMPONENT
print(today.day,today.month,today.year)

# GET WEEKDAY NUMBER ( MON=0, SUN=6): You can use to index a list
print(today.weekday())
# Example:
days=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
print(days[today.weekday()])

# GET TIME INFORMATION
today=datetime.now()
print('Today time is:{}'.format(today))

# Get CURRENT TIME
t=datetime.time(datetime.now()) # It gets time from datetime class with now
print(t)

# FORMAT THE OUTPUT
now=datetime.now()
print(now)
# To present in the desired format use
print(now.strftime('Year is %Y'))
print(now.strftime('%a,%d %B,%y'))

# LOCAL TIME
print(now.strftime('%c, %x,%X'))
print(now.strftime('Current time: %I: %M:%S %p'))
print(now.strftime('Current time: %H %M'))

# MATH FOR DATE/TIME
from datetime import timedelta # used for time base math

# CREATE TIMEDELTA
print(timedelta(days=365, hours=5, minutes=1))
now=datetime.now()

# 1 year from now, what is the today date?
print('One year from now is :'+str(now+timedelta(365)))
# In 2 days and 3 weeks, what is the date?
print('In 2 days and 3 weeks it is:'+str(now+timedelta(days=2,weeks=3)))

# NOW CALCUALTE THE PAST
past= datetime.now() - timedelta(weeks=2)
print('Two weeks ago was: '+past.strftime('%a:%d:%y %H %M'))
print('Two weeks ago was the time was: '+t.strftime('%H %M'))

# CALCULTE DAYS LEFT TO APRIL 1ST
today=date.today()
afd=date(today.year,4,1)
# Now let's see if April fool's is passed or not
if afd<today:
    print('April Fool day is passed by {}'.format(today-afd))
    # Next April Fool day is:
    afd=afd.replace(today.year+1)
    # Calcualte days left to april fool day
    print('Next Fool day is {} in {}'.format(afd,afd-today))
else:
    print('There are {} to Fool day'.format(today-afd))




