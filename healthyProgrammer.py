# Healthy Programmer

# Requirement
# Water : water.mp3 (3.5 ltr ) [9am - 5pm] <-- Drank -->log into file
# Eyes : eyes.mp3 --> Every 30 mins --> EyDone [Loop] --> log into file
# Physical activity : physical.mp3 -->Every 45 mins --> ExDone [Loop] -->log into file
#
# music until enter commit[Done]
#
# Rules
# pygame module to play audio
import datetime
import pygame


def alarm_loop(taskname, filename, alarmfile):
    pygame.mixer.music.load(alarmfile)
    # Start playing the song
    pygame.mixer.music.play()
    while True:
        print(f"{taskname} Reminder - (Enter \"Done\" to stop reminder) : ", end="")
        complete = input().capitalize()
        if ( complete == "Done"):
            file_writing(taskname,filename)
            # Pausing the music
            print("Successfully Stopped")
            break
        else:
            print("Please Complete The reminded task!")
    pygame.mixer.music.stop()

def file_writing(taskname, filename):
    with open(filename, "a") as f:
        f.write(f"{taskname} at : {datetime.datetime.now()}")




if __name__ == '__main__':
    # Starting the mixer
    pygame.mixer.init()

    # Setting the volume
    pygame.mixer.music.set_volume(1.0)

    now = datetime.datetime.now()
    # Setting the non office time range
    today9am = now.replace(hour=9, minute=0, second=0, microsecond=0)
    today5pm = now.replace(hour=17, minute=0, second=0, microsecond=0)
    while (datetime.datetime.now() < today9am or datetime.datetime.now() > today5pm):
        pass

    now =  datetime.datetime.now()
    water = datetime.datetime.now() + datetime.timedelta(minutes=40)
    eyes = datetime.datetime.now() + datetime.timedelta(minutes=30)
    physical = datetime.datetime.now() + datetime.timedelta(minutes=45)
    print("befor loop")
    print("------------------------ * The day Started * ------------------------")
    while now < today5pm:
        now = datetime.datetime.now()
        if now > eyes:
            alarm_loop("Eyes Relaxation", "eyes.txt","eyes.mp3")
            eyes = datetime.datetime.now() + datetime.timedelta(minutes=30)

        if now > water:
            alarm_loop("Take water", "water.txt", "water.mp3")
            water = datetime.datetime.now() + datetime.timedelta(minutes=40)
        if now > physical:
            alarm_loop("Physical Reminder", "physical.txt", "physical.mp3")
            physical = datetime.datetime.now() + datetime.timedelta(minutes=45)

    print("------------------------ * The day Ended * ------------------------")