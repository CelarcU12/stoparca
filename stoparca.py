import time
import winsound

frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second


def stoparca():
                sec = int(input("koliko sec?"))
                st =0
                while st < sec:
                                if sec-st <6:
                                                print("Pozor, pripravi se. Še :  "+str(sec-st)+" sekund")
                                                winsound.Beep(frequency*3, 10)
                                else:
                                                winsound.Beep(frequency, 7)
                                                print("            "+str(sec-st))
                                time.sleep(1)
                                st+=1
                winsound.Beep(1000, duration)
                ponovno = input("Še enkrat? ")
                if ponovno !="n" :
                                  stoparca()      
                                        
stoparca()	


def stoparca2():
                for i in range(5):
                                for j in range(3):
                                                for k in range(20):
                                                                print("            "+str(k))
                                                                time.sleep(1)
                                                                winsound.Beep(frequency, 10)
                                                winsound.Beep(1000, duration)
                                print("Pavza")
                                time.sleep(55)
                                for i in range(5):
                                                print("Še : "+str(5-i))
                                                time.sleep(1)
                                                winsound.Beep(440, 10)
                print("Bravo bravo, ti pa si dec!!! =)")
#stoparca2()

def stoparca3(sec):
                st =0
                while st < sec:
                                if sec-st <6:
                                                print("Pozor, pripravi se. Še :  "+str(sec-st)+" sekund")
                                                winsound.Beep(frequency*3, 10)
                                else:
                                                winsound.Beep(frequency, 7)
                                                print("            "+str(sec-st))
                                time.sleep(1)
                                st+=1
for serija in range(10):
                print("Serija : "+str(serija))
                sez= [20,10,20,10,60]
                for el in sez:
                                stoparca3(el)
#stoparca3(3)
