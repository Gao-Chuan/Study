from getUser import user
from getTime import time

def main():
    print "{year:0>4}-{month:0>2}-{day:0>2} {hour:0>2}:{minute:0>2}:{second:0>2}"\
        .format(year = time.year, month = time.month, day = time.day, \
                hour = time.hour, minute = time.minute, second = time.second)
    if 5<time.hour<10:
        print "Good morning, {name}.".format(name = user)
    elif 9<time.hour<14:
        print "time to eat, {name}~".format(name = user)
    elif 13<time.hour<19:
        print "Good afternoon, {name}.".format(name = user)
    elif 18<time.hour<1:
        print "Good evening, {name}.".format(name = user)
    else:
        print "time to sleep, good night, {name}.".format(name = user)

if __name__ == "__main__":
    main()
    
