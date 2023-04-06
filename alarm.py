import datetime   
from playsound import playsound
from Body.Speak import Speak

def clock():

    Speak("Enter the time:")
Time = input("Enter the time of alarm to be set -> HH:MM:SS\n")

while True:
    Time_Ac = datetime.datetime.now()
    now = Time_Ac.strftime("%H:%M:%S")

    if now == Time:
        Speak("Time to wakeup sir!")
        playsound('No Love.mp3')

    elif now>Time:
        break
