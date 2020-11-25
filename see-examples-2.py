# see-examples-2.py
# -----------------------------------------------------------------
# Programme that generates tones from sine waves - A basic version with limited amout of code lines for generating a sound.
#
# Revision 0.8 - 25 Nov 2020 - Knud Funch, Soundhub danmark - LYDKit til undervisningbrug - Region MidtJylland
# To be used as material for test in Physics/Math class
#
# To be run from within Thonny IDE on both PC,MAC and/or Raspberry PI.
#
from M2HEARlib import *
from M2SEElib import *

#---------------------------------------------------------------------------------------------------------------------------
#  Build and play back sounds by simple modification of the below. Listen, measure, experiment and reflect..
#

sound_1 = generate_signal(440)           
sound_2 = -sound_1
sound_3 = sound_1+sound_2
sound_4 = generate_signal(443)
sound_5 = sound_1+sound_4

plot_signal(sound_1)                        
play_signal(sound_1,forever=False)             # by adding parameter forever=False you can make sound play only once
plot_signal(sound_5,1000)                      # By adding second parameter different time in plot for l/r channel. Here 1 sec. (1000 ms)
play_signal(sound_5)           