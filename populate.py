import os, django, random
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FullThrottleLabs.settings')
django.setup()

from faker import Faker
from labApp.models import User, ActivityPeriod

fake = Faker()

count = 10

for _ in range(count):
    real_name = fake.name()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    def populateId():
        str = 'W'
        for i in range(8):
            char = random.choice(alpha)
            str = str + char
        #str = 'W' + str
        return str
    country = fake.country()
    city = fake.city()
    tz = country + '/' + city
    while(True):
        id = populateId()
        id = str(id)
        if User.objects.filter(id=id).exists():
            continue
        else:
            user = User(id = id, real_name = real_name, tz = tz)
            user.save()
            break

    for i in range(3):
        start_time = fake.date_time_this_year()
        end_time = fake.date_time_this_year()
        while(start_time >= end_time):
            end_time = fake.date_time_this_year()
        activityperiod = ActivityPeriod(idm = id, start_time = start_time, end_time = end_time)
        activityperiod.save()
