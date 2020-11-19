3# M2Sc1-hear-stereo-examples.py
# -----------------------------------------------------------------
# Programme that generates tones from sine waves - A basic version with limited amout of code lines for generating a sound.
#
# Revision 0.5 - 03 Apr 2020 - Knud Funch, Soundhub danmark - LYDKit til undervisningbrug - Region MidtJylland
# To be used as material for test in Physics/Math class
#
# To be run from within Thonny IDE on both PC,MAC and/or Raspberry PI.
#
from M2lib import *

#---------------------------------------------------------------------------------------------------------------------------
#  Build and play back sounds by simple modification of the below. Listen, measure, experiment and reflect..
#

sound_1 = generate_pure_tone(440,6000,0)           # l/r in phase
sound_2 = -sound_1
sound_3 = sound_1+sound_2
sound_4 = generate_pure_tone(443,6000,0)
sound_5 = sound_1+sound_4

play_sound(sound_5,1,1,Once)                               


# Play sound_1 in right and sound_2 in left - listen to one of then. listen to both of them either on spk or in headphones.
# Whats the difference? - why?
#play_sound(sound_1,0,1,Forever)   # 440 in right  
#play_sound(sound_4,1,0,Forever)   # 443 in left  

# gives the option to make experiments, measurements and tasks with 
# - intensity addition from one to two speakers
# - with constructive and destructive interference
#
# and same tasks/questions in the basic mono version can of cource be made with this version as well but simpler code in mono version...

            