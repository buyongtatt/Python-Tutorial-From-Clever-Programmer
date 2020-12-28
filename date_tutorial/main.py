import datetime
import pytz

today = datetime.date.today()
print(today)

birthday = datetime.date(1998, 12, 13)
print(birthday)

# find days since birth
days_since_birth = (today - birthday).days
print(days_since_birth)

# adding 10 days to current day
tdelta = datetime.timedelta(days=10)
print(today - tdelta)

print(today.weekday())

print(datetime.time(7, 2, 20, 15))
# datetime.date (Y, M, D)
# datetime.time (h, m, s)
# datetime.datetime (Y, M, D, h, m, s, ms)

hour_delta = datetime.timedelta(hours=10)
print(datetime.datetime.now() + hour_delta)

datetime_today = datetime.datetime.now(tz=pytz.UTC)
datetime_pacific = datetime_today.astimezone(pytz.timezone('Asia/Kuala_Lumpur'))
print(datetime_pacific)
for tz in pytz.all_timezones:
    print(tz)

# string formatting with dates
# 2020-12-27 -> December 27, 2020
# strftime (f = formatting)

print(datetime_pacific.strftime('%B %d, %Y'))

# December 27, 2020 -> datetime(2020,12,27)
# strptime (p = parsing)
print(datetime.datetime.strptime('December 27, 2020', '%B %d, %Y'))

# github refer to maya