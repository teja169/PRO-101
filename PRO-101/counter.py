import time

timer = int(input("enter the time in seconds : "))

def countdown_timer( seconds ):
    
    while seconds>0 :
        minute = int(seconds/60)
        second = int(seconds%60)
    
        time1 = f'{minute}:{second}'
        time.sleep(1)
    
        print(time1)
        seconds -= 1
        
    

countdown_timer(timer)  