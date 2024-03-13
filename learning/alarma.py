import os
import time
from playsound import playsound


def alarm(minutes , seconds):

    sound_path = os.path.join(os.path.dirname(__file__),"mario.mp3")

    total_second = minutes * 60 + seconds

    print(f"La alarma sonará en {minutes} minutos y {seconds} segundos")

    time.sleep(total_second)

    playsound(sound_path)

minutes = int(input("Ingresa los minutos de la alarma: "))
seconds = int(input("Ingresa los segundos de la alarma: "))

alarm(minutes,seconds)
