from datetime import datetime
def printTime():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time:", current_time)

printTime()

