# "M2SEElib.py"
#
# Plot funktionalitet til at lave simple (overskuelige) programmer med plot som er sammenlignelige med tilsvarende
# HEAR eksempler
#
# Version 0.1 Knud - SHD - 20 nov. 2020 - Første udgave efter erfaringer fra Herning og dialog om forløb i Skanderborg.
#                                         Ambition om at lave plot_sound som kan støtte simple eksempler på niveau med play_sound i M2HEARlib aht det pædagogiske i simple eksempler..
#
import matplotlib.pyplot as plt
import time  
import pygame
import numpy as np

#
# Globale konstanter 
#
SAMPLERATE = 44100  # Sampling frequence! samples pr second. Twice the highest freq you want to reproduce as minimum (nyquist)
                    # 44100/48000 is a widely used and match with sound card and pygame sound default settings typically.  
DURATION   = 1.0    # Lenght of tone generated in seconds.


MAX_AMP        = 30000
SPEED_OF_SOUND = 343       # m/s i luft ved 20 grader celsius

class plot_signal:     # Full means the full signal in plot eg lenght equals DURATION, If False only 10ms is shown
#
# initialiseringer med hensyn til plot og figur
#
    def __init__(self,signal,time_to_plot=10):
        plt.ion()                      # sætter plot funktionen til at tegne på skærm direkte så hvert kald får effekt med det samme
                                       # Hvis den ikke er kaldt så laver man tegning/plot i baggrunden og den bliver først vist når man kalder plt.show()
        plt.figure(figsize=[16,9])     # Laver plot vindue lidt større end default som er [6.4,4.8]
        self.left_plot = plt.subplot(311)
        plt.title("Venstre "+str(time_to_plot)+" ms udsnit\nDet der er i plot bevæger sig ca. "+str(SPEED_OF_SOUND*time_to_plot/1000)+" meter i luft ved 20 grader celsius")         
        plt.ylabel("amp")
        plt.axis([0,time_to_plot,-MAX_AMP,MAX_AMP])    # Plot 0-time_to_plot ms og sæt (amplitude) y-aksen til at gå fra - til + MAX_AMP - time_to_plot=10 ms hvis ikke angivet i kald

        self.right_plot = plt.subplot(312)
        plt.title("Højre "+str(time_to_plot)+" ms udsnit")           
        plt.ylabel("amp")
        plt.axis([0,time_to_plot,-MAX_AMP,MAX_AMP])    

        self.combined_plot = plt.subplot(313)
        plt.title("højre plus venstre - Det I hører hvis både h og venstre spiller - 1 sek udsnit")    
        plt.ylabel("amp")
    
        plt.axis([0,1000,-2*MAX_AMP,2*MAX_AMP])       
                                                    
        self.time = np.linspace(0,1000*DURATION,int(DURATION*SAMPLERATE))   # alternativ x-akse med tid i millisekunder (ms) fremfor radianer/vinkelværdier
        
        self.left_curve,     = self.left_plot.plot(self.time,signal.T[0])                
        self.right_curve,    = self.right_plot.plot(self.time,signal.T[1])                
        self.combined        = signal.T[0]+signal.T[1]
        self.combined_curve, = self.combined_plot.plot(self.time,self.combined)
        #
        # For at få tegnet plot færdigt inden der sker andet i koden skal der ventes lidt 
        #
        plt.pause(0.3)


    def update(self,signal):
        self.left_curve,     = self.left_plot.plot(self.time,signal.T[0])                
        self.right_curve,    = self.right_plot.plot(self.time,signal.T[1])                
        self.combined        = signal.T[0]+signal.T[1]
        self.combined_curve, = self.combined_plot.plot(self.time,self.combined)
        #
        # For at få tegnet plot færdigt inden der sker andet i koden skal der ventes lidt 
        #
        plt.pause(0.3)

    def clear_curves(self):
        self.left_plot.lines.remove(self.left_curve)          
        self.right_plot.lines.remove(self.right_curve)
        self.combined_plot.lines.remove(self.combined_curve)
        plt.draw() 