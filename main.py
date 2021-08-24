import time
import pync
import datetime
from beepy import beep


def log():
    now = datetime.datetime.now()
    start_time = now.strftime("%H:%M:%S")
    f = open("log.txt", "a")
    f.write(f"You drank water at {now} \n")
    f.close()
    time.sleep(1800)


def notify():
    pync.notify("It's time to drink water", title="Water Reminder")
    beep(sound="ready")
    log()
    return 0


def startTime(time_interval):
    while True:
        time.sleep(time_interval)
        notify()


if __name__ == '__main__':
    time_interval = 0
    startTime(time_interval)

