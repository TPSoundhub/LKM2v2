# simple-piano-MicroBit-input.py
#
#
# Programme that generates tones from sine waves for frequencies corresponding to 7 tones A4 to G5.
# Tones are then mapped to input keys from Microbit - Key '1', '2','3','4','5','6','7' and stopped when '0' is received.
# Key input is received on USB as serial input.
# It can be used as a very simple 'piano'.
#
# Revision 0.4 - 26 Nov 2020 - Knud Funch, Soundhub danmark - LYDKit til undervisningbrug - Region MidtJylland
#
# To be run from within Thonny IDE on both PC and PI.
#
# Task/Challenge is to modify the "make_tones()" function so the tone/timbre of the 'piano' are changed.


from M2HEARlib import *
import serial

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
keys = [
'1',             # pos 0  - related to A4 in frequency 
'2',             # pos 1  - related to B4 in frequency
'3',             # pos 2  - related to C5 in frequency
'4',             # pos 3  - related to D5 in frequency
'5',             # pos 4  - related to E5 in frequency
'6',             # pos 5  - related to F5 in frequency
'7',             # pos 6  - related to G5 in frequency
]
#
# make the sounds to be mapped onto keys
#
range_of_tones = range(0, len(frequency))
sound_table = [make_tones(frequency[i]) for i in range_of_tones]
generated_sounds = map(pygame.sndarray.make_sound, sound_table)
# Make table of sounds from the generated signals
sounds = map(pygame.sndarray.make_sound, generated_sounds)
# Map keys and sounds together in dictionary for easy and fast look up
key_sound = dict(zip(keys, sounds))


# ON PI:
# ser = serial.Serial(baudrate = 115200, port = "/dev/ttyACM0")
# on Mac:
# ser = serial.Serial(baudrate = 115200, port = "/dev/cu.usbmodem14102")
# ON PC
ser = serial.Serial(baudrate = 115200, port = "COM5")    # Need to figure out the port name and put it in here!!!!

def receive_char():
    microbitdata = str(ser.readline())
    key=microbitdata[2]
    return key


def play_note(key,is_playing):
    if key != is_playing:
        if is_playing in keys: key_sound[is_playing].stop()  # key different from "0" then stop the last sound
        is_playing = "0"
    if key in keys:
        key_sound[key].set_volume(1.0)
        key_sound[key].play(-1)                              # play sound related to key if key different from "0"
        is_playing = key
     
    return is_playing


last_playing = '0'
#
# Main loop reading incomming keys from MicroBit and playing back coresponding note
#
while True:
   
    mb_key = receive_char()
    print(mb_key)
    last_playing = play_note(mb_key,last_playing)
           