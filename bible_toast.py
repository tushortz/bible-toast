import random
import time
from configparser import ConfigParser
import os
import requests
import validators
from win10toast import ToastNotifier

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

config = ConfigParser()

config_path = os.path.join(BASE_DIR, "settings.ini")
icon_path = os.path.join(BASE_DIR, "bible.ico")

config.read(config_path)

filepath = config.get("DEFAULT", "bible_path")
duration_in_sec = config.getint("DEFAULT", "duration_in_sec")

bible = []

if validators.url(filepath):
    data = requests.get(filepath).text

else:
    with open(filepath) as f:
        data = f.read()
        
bible = data.split("\n.\n")


def get_rand_quote():
    return random.choice(bible)


def show_toast_notification():
    passage = get_rand_quote()
    passage = passage.split(" -- ")

    verse = passage[0]
    reference = passage[1].title()

    toaster = ToastNotifier()
    toaster.show_toast(reference,
                       verse,
                       icon_path=icon_path,
                       duration=duration_in_sec,
                       threaded=True,
                       )

    # Wait for threaded notification to finish
    while toaster.notification_active():
        time.sleep(0.1)


# if __name__ == "__main__":
show_toast_notification()
