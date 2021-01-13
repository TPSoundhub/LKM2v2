# M2HEARlib.py
#
# M2 - Basic tonegeneration and playback functions in stereo  (two channels)
# -----------------------------------------------------------------
# Programme that generates tones from sine waves - A basic version with limited amout of code lines for generating a sound signal.
#
#
# Version 0.9 - 04 november 2020 - Knud Funch, Soundhub danmark - LYDKit til undervisningbrug - Region MidtJylland
# To be used as material for test in Physics/Math class
#
# As precondition the following libraries needs to be included in IDE - That is to be installed via TOOLS/MANAGE PACKAGES
# from within Thonny.
#
#         - numpy  - for putting sine into an array taht can easily be manipulated/worked with on high level
#         - pygame - for generating and playing sound cross platform (PC/MAC/PI) and with opportunity for playing more at same time 
#
# To show a tone can be made easily from within Thonny/Python environment, which means there is a progression path for
# 'building stuff' within the same framework as shown in Module 1.
#
# This is the key reason for making it in python/thonny - as it is acknowledged a sine wave sound can be made in easier way.
# The option for using it later as a building block is the reason for this path!
#
# Import this by "from M2HEARlib.py import *"
#

import time  
import pygame
import numpy as np

SAMPLERATE = 44100  # Sampling frequence! samples pr second. Twice the highest freq you want to reproduce as minimum (nyquist)
                    # 44100/48000 is a widely used and match with sound card and pygame sound default settings typically.  
DURATION   = 1.0    # Lenght of tone signal generated in seconds.

FOREVER = True
ONCE    = False

#
# Basic function to put a sine wave into an np array given a frequency and an amplitude as defined in parameters
# Any frequency below 1/2 the sampling rate given in SAMPLERATE can be used. 
# Amplitude as a value matching/relative to sound card 16-bit capability.
#     To avoid clipping do make sure the combined
#     max ampitude in sounds generated is 1/2*65.535 as this is the max value possible in 16-bit (signed +/- 32,767)
#     It is OK to try to get values that are higher - try and listen. Its not a pure tone anymore!
#
def generate_signal(freq,amp_max=6000):  
    # make and return a signal array with number of entries equal to DURATION*SAMPLERATE and with DURATION*freq rounds in unit circle
    # multiply with max amplitude and make sure it is within 16bit integer to match sound card capabilities 
    #
    # Laver en tabel for hhv højre og venstre med DURATION*freq antal perioder (omgange i enhedscirklen/bølgelængder)
    # og delt op i DURATION*SAMPLERATE antal datapunkter med sin(x)*amp som værdi og i 16 signed heltal.
    # sin() funktion på hele tabel på een gang. dvs alle værdier i tabel i et hug!
    # Den sidste linie kombinerer de 2 tabeller til een som kan bruges til at generere en stereo lyd
    # bruger copy funktion for at få det lagt ud i rækkefølge i memory, som er en forudsætning for at kunne bruge pygames generate sound funktion.
    t = np.linspace(0,DURATION*freq*2*np.pi,int(DURATION*SAMPLERATE),endpoint=False)
    signal_left  = (np.sin(t)*amp_max).astype(np.int16)
    signal_right = signal_left                                                           # same in both left and right channel in the stereo signal
    signal = np.array((signal_left,signal_right)).T.copy()
    return signal


def generate_freq_modulated_signal(freq,amp_max=6000,mf=3):   # carrier og modulator og husk der kan være forskellig amp på de 2 også!!
    t1 = np.linspace(0,DURATION*freq*2*np.pi,int(DURATION*SAMPLERATE),endpoint=False)
    t2 = np.linspace(0,DURATION*mf*2*np.pi,int(DURATION*SAMPLERATE),endpoint=False)
    signal_left = (np.sin(t1+np.sin(t2))*amp_max).astype(np.int16)   # mf as modulator freq 
    signal_right = signal_left                                                           # same in both left and right channel in the stereo signal
    signal = np.array((signal_left,signal_right)).T.copy()
    return signal

#
# Function to make sound from signal and play it back in one of the channels available in pygame.mixer
# Volume in left and right channel can be set in parameters. Default at max level (1). Can be muted by 0
# Default the generated sound keeps on playing in the channel until stopped. can be set to only be played once by ONCE/False in parameter.
# Channel is returned so it can be controlled later by caller.
#
def play_signal(sound,vol_l=1,vol_r=1,forever=FOREVER):
    channel = pygame.mixer.find_channel()
    channel.set_volume(vol_l,vol_r)
    if forever:
        channel.play(pygame.sndarray.make_sound(sound),-1)
    else:
        channel.play(pygame.sndarray.make_sound(sound))
        time.sleep(DURATION+0.2)                            # make sure sound plays to the end before ending this function
    return channel

# initialise pygame mixer with proper values to match sound generated
# Here sampling freq=SAMPLERATE, and 16 bit (signed) to stay within soundcards basic capability and in stereo (2 channels)
# Just so it is not needed in main programme.
#
pygame.mixer.init(SAMPLERATE, -16, 2)
