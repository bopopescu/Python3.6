#!/usr/bin/python

week=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

endings=['st','nd','rd']+17*['th']+['st','nd','rd']+7*['th']+['st']

months=['yiyue','eryue','sanyue','siyue','wuyue','liuyue','qiyue','bayue','jiuyue','shiyue','shiyiyue','shieryue']

years=input('Year:')
month=input('Months(1-12):')
days=input('Day(1-31):')
weeks=input('week(1-7):')

month_number=int(month)
days_number=int(days)
week_number=int(weeks)

year_name=years+'Years'
month_name=months[month_number-1]
day_name=days+endings[days_number-1]
week_name=week[week_number-1]
print ('\n')
print ("{0}/{1}/{2}/{3}".format(year_name,month_name,day_name,week_name))
print ('\n')
input('Press <enter>:')



