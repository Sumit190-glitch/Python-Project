import time 
from plyer.platforms.win.notification import WindowsNotification

while True:
    print("Please take some water")
    notifier = WindowsNotification()
    notifier.notify(title = "Reminder", message = "You need to drink some water")
    
    time.sleep(3)