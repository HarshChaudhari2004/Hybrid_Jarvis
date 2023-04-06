import webbrowser as web
import requests
from Body.Listen import MicExecution
from Body.Speak import Speak



def My_Location():

    #op = "https://www.google.com/maps/place/Delhi/@28.6472799,76.8130619,83757m/data=!3m2!1e3!4b1!4m5!3m4!1s0x390cfd5b347eb62d:0x37205b715389640!8m2!3d28.7040592!4d77.1024902"
    op = "https://goo.gl/maps/Ypw8onrihP98FqUt7"
    Speak("Checking....")

    web.open(op)

    ip_add = requests.get('https://api.ipify.org').text

    url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'

    geo_q = requests.get(url)

    geo_d = geo_q.json()

    state = geo_d['city']

    country = geo_d['country']

    Speak(f"Sir , You Are Now In {state , country} .")
