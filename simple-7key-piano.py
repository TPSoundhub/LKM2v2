# Tones on KB.py
#
# Programme that generates tones from sine waves for frequencies corresponding to 7 tones A4 to G5.
# Tones are then mapped to Keyboard keys A,S,D,F,G,H,J so it can be used as a very simple 'piano'.
#
# Revision 0.2 - 25 Nov 2020 - Knud Funch, Soundhub danmark - LYDKit til undevisningbrug - Region MidtJylland
#
# To be run from within Thonny IDE on both PC and PI.
# As precondition the following libraries needs to be included in IDE - That is to be installed via TOOLS/MANAGE PACKAGES
# from within Thonny.
#
#         - numpy
#         - matplotlib
#         - pygame 
#
#
# To generate sound (sine waves) and map them to Keyboard keys and play them pygame and numpy libraries are imported
#
# You must have focus in the small 'black' window to get keys into this program.
#  
# To shut down program and get window cleared you must either press ESC or the X in upper right corner.

from M2HEARlib import *


frequency = [     # node and index/position in table/array
440,           # A4 - pos 0
494,           # B4 - pos 1
523,           # C5 - pos 2
587,           # D5 - pos 3
659,           # E5 - pos 4
698,           # F5 - pos 5
784,           # G5 - pos 6
]

def make_tones(freq):
    x = generate_signal(freq)
    # Modify this function to make the sound of the piano different - eg by adding overtones to signal.  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    return x

#
# Leave the rest unchanged!
#

range_of_tones = range(0, len(frequency))
sound_table = [make_tones(frequency[i]) for i in range_of_tones]
generated_sounds = map(pygame.sndarray.make_sound, sound_table)

# Window needed for getting keyboard input to the program. (ESC stops and close window)
screen = pygame.display.set_mode((150, 150))

keys=['a', 's', 'd', 'f', 'g', 'h', 'j']

sounds = map(pygame.sndarray.make_sound, generated_sounds)

# Map keys and sounds together in dictionaty for easy and fast look up
key_sound = dict(zip(keys, sounds))
# is playing table for checking sound playing pr key - and initialise all to False (not playing)
is_playing = {k: False for k in keys}


# Take KB input events and play coresponising tone - you have a 'keyboard piano now so play along ;-)
run = True
while run:
    event = pygame.event.wait()

    if event.type == pygame.QUIT: run = False  # X'ed in window
    else:
        if event.type in (pygame.KEYDOWN, pygame.KEYUP):
            key = pygame.key.name(event.key)
            print(key)
            if event.key == pygame.K_ESCAPE: run = False
            if (event.type == pygame.KEYDOWN) and (key in key_sound.keys()) and (not is_playing[key]):
                key_sound[key].play(-1)  # -1 means plays until stopped. ticks because not aligned start/stop values! Need trimming!!
                is_playing[key] = True
            elif event.type == pygame.KEYUP and key in key_sound.keys():
                key_sound[key].stop()
                is_playing[key] = False

# When running is stopped
pygame.quit()  # clean up - removes the window for focus/KB input
            