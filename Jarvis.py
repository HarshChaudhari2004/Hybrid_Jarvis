from Brain.AIBrain import ReplyBrain
# from Brain.Qna import QuestionsAnswer
from Body.Listen import MicExecution
print(">> Starting The Jarvis : Wait For Some Seconds.")
from Body.Speak import Speak
from Features.Clap import Tester
print(">> Started The Jarvis : Wait For Few Seconds More")
from Main import MainTaskExecution
from keyboard import press
from keyboard import press_and_release

def MainExecution():
    Speak("Hello Sir")
    Speak("I'm Jarvis, I'm Ready To Assist You Sir.")

    while True:

        Data = MicExecution()
        Data = str(Data).replace(".","")

        ValueReturn = MainTaskExecution(Data)
        if ValueReturn==True:
            pass

        elif len(Data)<3:
            pass

        elif "whatsapp message" in Data:
            pass

        # Specific Command
        elif "turn on the tv" in Data:
            Speak("Ok..Turning On The Android TV")

        elif 'youtube search' in Data:
            Query = Data.replace("jarvis","")
            query = Data.replace("youtube search","")
            from yt import YouTubeSearch
            YouTubeSearch(Data)

        elif 'my location' in Data:
            from my_location import My_Location
            My_Location()

        elif 'where is' in Data:
            from maps import GoogleMaps
            Place = Data.replace("where is ","")
            Place = Place.replace("jarvis" , "")
            GoogleMaps(Place)

        elif 'set alarm' in Data:
            from alarm import clock
            clock()

        elif 'Browser auto' in Data:
            from chrome_auto import ChromeAuto
            ChromeAuto()

        # elif 'youtube auto' in Data:
        #     from yt_auto import YouTubeAuto
        #     YouTubeAuto()

        elif 'write a note' in Data:
            from Automations import Notepad
            Notepad()

        elif 'dismiss' in Data:
            from Automations import CloseNotepad
            CloseNotepad()            

        # elif "what is" in Data or "where is" in Data or "question" in Data or "answer" in Data:
        #     Reply = QuestionsAnswer(Data)

#Youtube Automation

        elif 'pause' in Data:

            press('space bar')

        elif 'play video' in Data:

            press('space bar')

        elif 'full screen' in Data:

            press('f')

        elif 'Theater mode' in Data:

            press('t')

        elif 'skip' in Data:

            press('l')

        elif 'back' in Data:

            press('j')

        elif 'increase speed' in Data:

            press_and_release('SHIFT + .')

        elif 'decrease speed' in Data:

            press_and_release('SHIFT + ,')

        elif 'previous' in Data:

            press_and_release('SHIFT + p')

        elif 'next' in Data:

            press_and_release('SHIFT + n')

        elif 'mute' in Data:

            press('m')

        elif 'unmute' in Data:

            press('m')

        else:

            if 'bye' in Data:
                Speak("Bye sir")
                break

            elif 'exit' in Data:
                Speak("Bye Sir!!, Thank you")
                break

            Reply = ReplyBrain(Data)
            Speak(Reply)

def ClapDetect():

    query = Tester()
    if "True-Mic" in query:
        print("")
        MainExecution()
    else:
        pass

ClapDetect()
