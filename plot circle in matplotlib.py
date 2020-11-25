# plot circle in matplotlib.py - version 1.0 25-nov-202
# tegn cirkel og een periode af sin/cos med matplotlib
# Til grundlæggende forklaring om signal generering
#
import numpy as np
import matplotlib.pyplot as plt

R = 1  # radius, som jo så altid er 1 i enhedscirklen
N = 30 # antal datapunkter
t = np.linspace(0,2*np.pi,N,endpoint=False)
#
# x,y værdier som cosinus hhv sinus ganget med R (radius, som er sat til 1 (enhedscirklen))
#
cosinus = R*np.cos(t)   # Cos på alle datapunkter på een gang 
sinus   = R*np.sin(t)   # Sin på alle datapunkter på een gang
#
# plot cirklen  x = cosinus, y = sinus
#
plt.subplot(211)
plt.axis("equal")
plt.grid()
plt.plot(cosinus,sinus)
plt.plot(cosinus,sinus,"+b")
#
# Plot sin og cos i forhold til vinkel i radianer (en bølgelængde) - Bemærk første/sidste værdi
#
plt.subplot(212)
plt.xlabel("x = Vinkel i radianer")
plt.ylabel("sin(x),cos(x)")
plt.grid()
plt.plot(t,sinus,"+")
plt.plot(t,cosinus,"+")
plt.show()                   
                                       
                     

