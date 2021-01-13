# see-examples-1.py
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
#  Build and plot signals by simple modification of the below. Experiment and reflect..
#

sound_1 = generate_freq_modulated_signal(880,mf=100)           

plot_signal(sound_1,time_to_plot=100)
play_signal(sound_1)

