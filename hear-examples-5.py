# hear-examples-5.py
# -----------------------------------
# Using M2HEARlib.py to make series to emulate Obo playing A.
#
# Revision 0.5 - 25 Nov 2020 - Knud Funch, Soundhub danmark - LYDKit til undervisningbrug - Region MidtJylland
# To be used as material in module 2 test in Physics/Math class
#
# To be run from within Thonny IDE on either PC, MAC (or Raspberry PI).
#
from M2HEARlib import *
# ------------------------------------------------------------------------------------------------------------------------------
#
#         

bf = 440          # Keep bf*13 < 1/2 of sf !!   # try other fundamentals
ba = 32000        # full scale with signed 16-bit amplitude

f1  = generate_signal(bf,ba*0.1122)      # fundamental

o2  = generate_signal(2*bf,0.3890*ba)    # n'th overtone with n*fundamental freq  
o3  = generate_signal(3*bf,0.0316*ba)    # and 1/n times fundamental amplitude 
o4  = generate_signal(4*bf,0.0398*ba)
o5  = generate_signal(5*bf,0.0354*ba)
o6  = generate_signal(6*bf,0.0298*ba)
o7  = generate_signal(7*bf,0.0119*ba)

s1 = f1+o2+o3+o4+o5+o7

play_signal(s1)

# Hvad mangler der for at det lyder som en rigtig Obo?