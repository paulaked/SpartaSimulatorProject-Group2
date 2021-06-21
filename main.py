import time

def time_counter(t):

    while t != 0:
        years, months = divmod(t, 12)
        timer = '{:02d}:{:02d}'.format(years, months)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print("The time simulation is over")

t = input("Enter the time in months for the programme to run: ")

time_counter(int(t))
