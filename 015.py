from datetime import date
for year in range(1006,1996,10):
    if date(year,1,26).isoweekday()==1:
        if year % 4 == 0:
            print(year)
