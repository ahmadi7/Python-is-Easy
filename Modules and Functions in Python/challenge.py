import datetime
import pytz

timezones = {"1": "Africa/Algiers",
             "2": "America/Mexico_City",
             "3": "Asia/Jakarta",
             "4": "Australia/Perth",
             "5": "Europe/Athens",
             "6": "Jamaica",
             "7": "Pacific/Fiji",
             "8": "US/Pacific",
             "9": "UTC"}


for t in sorted(timezones):
    print("\t{}. {}".format(t, timezones[t]))
print("Please pick one of these timezones (or '0' to quit): ")

while True:
    choice = input()

    if choice == '0':
        break

    if choice in timezones.keys():
        tz_to_display = pytz.timezone(timezones[choice])
        world_time = datetime.datetime.now(tz=tz_to_display)
        print("The time in {} is {} {}".format(timezones[choice], world_time.strftime('%A %x %X %z'), world_time.tzname()))
        print("Localtime is {}".format(datetime.datetime.now().strftime('%A %x %X')))
        print("UTC time is {}".format(datetime.datetime.utcnow().strftime('%A %x %X')))
        print()
