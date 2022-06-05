import time 
from plyer import notification

while(True):
    notification.notify(
        title = 'title',#title,
        message = 'Hello World!',#body
        app_icon = "",#icon
        timeout  = 50#acive time
    )
    time.sleep(60)#repeats after