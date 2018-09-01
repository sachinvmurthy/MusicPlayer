import simplegui

# load some sounds
music = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/Epoq-Lepidoptera.ogg")
laugh_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/Evillaugh.ogg")

# define event handlers
def play():
    """
    Play some music, starts at last paused spot
    """
    music.play()

def pause():
    """
    Pause the music
    """
    music.pause()

def rewind():
    """
    Rewind the music to the beginning
    """
    music.rewind()

def laugh():
    """
    Play the laugh
    """
    laugh_sound.play()

def vol_down():
    """
    Turn the current volume down
    """
    global vol
    if vol > 0:
        vol = vol - 1
    music.set_volume(vol / 10.0)
    volume_button.set_text("Volume = " + str(vol))

def vol_up():
    """
    Turn the current volume up
    """
    global vol
    if vol < 10:
        vol = vol + 1
    music.set_volume(vol / 10.0)
    volume_button.set_text("Volume = " + str(vol))



frame = simplegui.create_frame("Music demo", 250, 250, 100)


frame.add_button("play", play, 100)
frame.add_button("pause", pause, 100)
frame.add_button("rewind", rewind, 100)
frame.add_button("laugh", laugh, 100)
frame.add_button("Vol down", vol_down, 100)
frame.add_button("Vol up", vol_up, 100)

vol = 7
volume_button = frame.add_label("Volume = " + str(vol))
laugh_sound.set_volume(.1)


frame.start()
