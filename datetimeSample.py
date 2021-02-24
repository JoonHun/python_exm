import datetime

# get current time
now = datetime.datetime.now()
print(now.year, "Year")
print(now.month, "Month")
print(now.day, "Day")
print(now.hour, "Hour")
print(now.minute, "Minute")
print(now.second, "Second")

out_a = now.strftime("%Y.%m.%d  %H.%M.%S")
print(out_a)

out_b = "{}Year {}Month {}Day  {}H {}M {}S ".format(now.year,\
  now.month, \
  now.day, \
  now.hour, \
  now.minute, \
  now.second)
print(out_b)

out_c = now.strftime("%Y{}.%m{}.%d{}  %H{}:%M{}:%S{}").format(*"YmdHMS")
print(out_c)