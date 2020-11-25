# hear-examples-2.py
# -----------------------------------------------------------------
# Programme that generates tones from sine waves - A basic version with limited amout of code lines for generating a sound.
#
# Revision 0.8 - 25 Nov 2020 - Knud Funch, Soundhub danmark - LYDKit til undervisningbrug - Region MidtJylland
# To be used as material for test in Physics/Math class
#
# To be run from within Thonny IDE on both PC,MAC and/or Raspberry PI.
#
from M2HEARlib import *

#---------------------------------------------------------------------------------------------------------------------------
#  Build and play back sounds by simple modification of the below. Listen, measure, experiment and reflect..
#

sound_1 = generate_signal(440)           # l/r
sound_2 = -sound_1
sound_3 = sound_1+sound_2
sound_4 = generate_signal(443)
sound_5 = sound_1+sound_4         

# Play sound_1 in right and sound_4 in left - listen to one of then. Use # to remove one or other .
# listen to both of them either on spk or in headphones.  The extra parameters controls wheter or not sound comes out in left/right speaker 0 = mute 1=full volume
# How does this differ from the experience of sound_5? Why? Whats the difference?
#
play_signal(sound_1,0,1)
play_signal(sound_4,1,0)


# gives the option to make experiments, measurements and tasks with 
# - intensity addition from one to two speakers
# - with constructive and destructive interference


            