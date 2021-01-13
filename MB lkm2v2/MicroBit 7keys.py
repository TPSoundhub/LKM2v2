from microbit import *

last_key = "0"
key = "0"
display.show(key)

def read_key():
    p0 = pin0.is_touched()
    p1 = pin1.is_touched()
    p2 = pin2.is_touched()
    
    if p0 and p1 and p2:               key="7"
    elif not p0 and p1 and p2:         key="6" 
    elif p0 and not p1 and p2:         key="5" 
    elif not p0 and not p1 and p2:     key="4"
    elif p0 and p1 and not p2:         key="3"
    elif not p0 and p1 and not p2:     key="2" 
    elif p0 and not p1 and not p2:     key="1"
    else:                              key="0"
 
    return key


while True:

    key = read_key()
    sleep(50)
    key_control = read_key()
    
    if key == key_control:
        if last_key != key:
            print(key)
            display.show(key)
            last_key=key
    
    sleep(50)