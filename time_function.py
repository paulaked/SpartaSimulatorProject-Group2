import time

years, months = divmod(t, 12)
timer = '{:02d}:{:02d}'.format(years, months)
print(timer, end="\r")
time.sleep(1)

