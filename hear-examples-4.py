# hear-examples-4.py
# -----------------------------------------------------------------
# Programme that generates tones from sine waves - A basic version with limited amout of code lines for generating a sound.
#
# Revision 0.2 - 25 Nov 2020 - Knud Funch, Soundhub danmark - LYDKit til undervisningbrug - Region MidtJylland
# To be used as material for test in Physics/Math class
#
# To be run from within Thonny IDE on both PC,MAC and/or Raspberry PI.
#
from M2HEARlib import *
#---------------------------------------------------------------------------------------------------------------------------
#  Build and play back sounds by simple modification of the below. Listen, measure, experiment and reflect..
#
# super simpel sweep med de givne funktioner - her med lyd
# Ikke brugbar da der er ticks i lyden og lydkort/basis funktion kan ikke følge med så derfor skal weep laves på anden måde - men ellers simpelt program
# men det viser begrænsningen i det ....  Kan ikke undgå ticks når man skifter mellem lydene. Kan ikke få det smooth og heller ikke hurtigt nokm tænker jeg

for freq in range (400,4000,5):    # sidste parameter giver step størrelsen i frekvens
    print(freq)
    sound = generate_signal(freq,20000)
    play_signal(sound, forever=False)