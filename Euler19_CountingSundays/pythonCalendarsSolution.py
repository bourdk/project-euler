import calendar as cal

tcal = cal.TextCalendar(6)
sundays = 0

for i in range(1901, 2001):
    strcal = tcal.formatyear(i, 2, 1, 0, 1)
    for line in strcal.split(sep='\n'):
        try:
            n = int(line[:2])
            if n == 1:
                sundays += 1
        except ValueError:
            continue

print(sundays)