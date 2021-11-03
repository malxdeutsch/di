from datetime import datetime, date


def date():
    now = datetime.now()
    print (f"Current date {now}")

date()

def calculate():
    now = datetime.now()
    later_date = datetime(2022, 1, 1, 0, 0, 0,)
    diff = later_date-now
    print (f"Current date {now}")
    print (f"Later date {later_date}")
    print (f"Difference is {diff}")

calculate()

def birthdate(later_date):
    now = datetime.now()
    diff = now-later_date
    seconds = diff.total_seconds()
    minute = seconds/60
    print (f"Current date {now}")
    print (f"Later date {later_date}")
    print (f"Difference is {diff}")
    print (f"I've been alive for {minute} minutes TG.")


inpt = datetime(1997, 7, 1, 0, 0, 0)
birthdate(inpt)

def holiday ():
    now = datetime.now()
    chanukah = datetime(2021, 11, 28, 0, 0, 0,)
    diff = chanukah-now
    print (f"Current date {now}")
    print (f"Chanukah starts on {chanukah}")
    print (f"Chanukah is in {diff}")

holiday()

def planets():
    seconds= 1000000000
    earth_days = 365.25  
    earth_seconds = 31557600 
    mercury = (earth_days/ 0.2408467) * earth_seconds
    venus = (earth_days/ 0.61519726) * earth_seconds
    mars = (earth_days/ 1.8808158) * earth_seconds
    jupiter = (earth_days/ 11.862615) * earth_seconds
    saturn = (earth_days/ 29.447498) * earth_seconds 
    uranus = (earth_days/ 84.016846) * earth_seconds
    neptune = (earth_days/ 164.79132)* earth_seconds 
    my_list = [mercury, venus, mars, jupiter, saturn, uranus, neptune]
    for each_planet in my_list:
        year = seconds/each_planet
        print(year)

planets()


from faker import Faker