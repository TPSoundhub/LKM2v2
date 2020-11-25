# "sweep and plot.py"
#
# Loop eksempel med løbende plot af signal
#
# Knud - SHD - 13 nov. 2020 Version 0.1 - En første simplificering mod forløb i Skanderborg
#              19 nov. 2020 Version 0.2 - Flyttet signal generering til bibliotek og droppet forskellig amp i h/v
#                                         SAMPLERATE og DURATION også i biblioteket. Samme bib til alle øvelser...
#              20 nov. 2020 Version 0.3 - Flytet funktionalitet ud i bibliotek så hoved program kan laves simpelt - få linier
#                                         samt at bibliotek så kan bruges til at lave simple SEE udgaver af HEAR eksemplerne ....
#              25 Nov. 2020 Version 0.4 - Droppet muligheden for delta. Kun med nu for at vise hvordan biblioteker kan bruges.
#                                         og at det der blev lavet til Herning forløb kan laves enkelt med bibliotekerne..
#                                         Udskrift i shell er interesant og kan evt. kombineres ind i plot bibliotek
#                                       
#
# Ved at ændre i konstanter kan man bruge den til lidt forskelligt.
#
# Når pogram er slut skal der blot klikkes indenfor plot vinduet for at få det fjernet og ryddet op
# Pt kommer der en række fejlmeldinger hvis man klikker i 'X' i vinduet både undervejs og til slut... (
#  Brug stop stop
#
from M2HEARlib import *
from M2SEElib import *


MAX_FREQ       = 4000      # Max freq i Hz - Der vi stopper
STEP_IN_SWEEP  = 200       # i Hz - den forskel der er mellem freq i while loop i sweep

#
# Globale variable - Start frekvens i de 2 kanaler.
#
freq = 100
first_round = True


while freq < MAX_FREQ:

    signal = generate_signal(freq,15000)
    if first_round:
        first_round=False
        plot=plot_signal(signal)
    #
    # Bølge længden = hastighed/frekvens = (m/s divideret med 1/s) = meter (ganges med 100 så det er i cm) og med round(x,2) for at give 2 decimaler
    # Udskrives i shell til information. 
    #
    blv = round(SPEED_OF_SOUND*100/freq,2)
    print("Venstre og Højre: Freq: "+str(freq)+"Hz. Bølgelængden: "+"%.2f" % blv+"cm.","Svingningstid: "+"%.4f" % (1000/freq),"ms.")
    print()
    #
    # Mixer kan håndtere at afspille 8 lyde samtidigt, men her lader vi den kun spille een ad gangen i et sweep. (Med ONLY_ONE_SOUND = True)
    # Man kan gemme reference til de enkelte lyde (lyd objekter) og starte/stoppe dem individuelt... Eksperimenter med det i senere udgave
    # Man hører kun de første 8 lyde i sweep når man sætter konstanten til True ;-) Så det er ikke så fedt.... Så bør man justere de andre
    # konstanter til sådan at man kun kommer rundt i loop 8 gange...
    #
    #
    channel = play_signal(signal,forever=False)   
    # Plot
    if not first_round:
        plot.clear_curves()
        plot.update(signal)

    
    channel.stop()                    # Stop lyden inden en ny laves så de ikke blandes

    #
    # I dette eksempel lader vi frekvenserne i både højre og venstre vokse med STEP_IN_SWEEP for hver tur i while løkken.
    #
    freq+=STEP_IN_SWEEP
#
# Plot bliver stående til man klikker i X.

