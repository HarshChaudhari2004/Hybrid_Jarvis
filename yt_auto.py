#Youtube Automation
from keyboard import press
from keyboard import press_and_release
from Body.Speak import Speak

def YouTubeAuto(command):

    query = str(command)

    if 'pause' in query:

        press('space bar')

    elif 'resume' in query:

        press('space bar')

    elif 'full screen' in query:

        press('f')

    elif 'Theater mode' in query:

        press('t')

    elif 'skip' in query:

        press('l')

    elif 'back' in query:

        press('j')

    elif 'increase speed' in query:

        press_and_release('SHIFT + .')

    elif 'decrease speed' in query:

        press_and_release('SHIFT + ,')

    elif 'previous' in query:

        press_and_release('SHIFT + p')

    elif 'next' in query:

        press_and_release('SHIFT + n')

    elif 'mute' in query:

        press('m')

    elif 'unmute' in query:

        press('m')

    else:
        Speak("No Command Found!")
