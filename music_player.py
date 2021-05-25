import os
import time
import random
import pyttsx3

w=pyttsx3.init()

while True:
    
    try:
        music_dir = 'C:\\Users\\User\\music'
        songs = os.listdir(music_dir)
        print(songs)

        n=int(input('enter index of your song: '))
        if n == 'q':
            input('press enter to exit')
            break
        os.startfile(os.path.join(music_dir, songs[n]))
        input()

    except IndexError:
        print('your music list is not up to', n)
        w.say('sorry , your music list is not up to', n)
        w.runAndWait()
        print('refreshing....')
        w.say('refreshing......')
        w.runAndWait()
        time.sleep(3)
    except ValueError:
        print('only enter the number of the song as it falls in the list')
        print('refreshing....')
        w.say('refreshing......')
        w.runAndWait()
        time.sleep(3)
  
    

