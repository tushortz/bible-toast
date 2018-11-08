import random
from win10toast import ToastNotifier
import time


bible = []
with open("nasb.txt") as f:
    bible = f.read().split("\n.\n")

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
                    icon_path="bible.ico",
                    duration=20,
                    threaded=True,
                    )
                    
    # Wait for threaded notification to finish
    while toaster.notification_active(): 
        time.sleep(0.1)

# if __name__=="__main__":
show_toast_notification()