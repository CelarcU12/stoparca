#glasbena lestvica

import time
import winsound


t= 500 # čas -> 100 = 0.1 sekunde 
a = 440 #frekvenca

def ton(n):
                f = 2**((n-49)/12)*a
                winsound.Beep(int(f),t)




def lestvica(z=40, sez=[2,2,1,2,2,2,1]):
                '''Dur lestvica...
                z je začetni ton.
                sez = seznam razadlj med toni -> privzeta je dur
                z= 40 je ton c1'''
                for el in sez:
                                ton(z)
                                z+=el
                ton(z)
                for el in sez[::-1]:
                                ton(z)
                                z-=el
                ton(z)
dur=[2,2,1,2,2,2,1]
mol=[2,1,2,2,1,3,1]
pentatonika = [2,3,2,2]

lestvica(40,pentatonika)
