import time
import winsound

frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second


def stoparca( stSerij=1):
                sec = int(input("koliko sec?"))
                st =0
                print("Število serije  :  "+str(stSerij))
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
                print("Na vrsti je serija : " + str(stSerij+1))
                stoparca(stSerij+1)      
                                        
#stoparca()	


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
for serija in range(5):
                print("Serija : "+str(serija))
                sez= [20,20,20,20,20,20,120]
                for el in sez:
                                stoparca3(el)
#stoparca3(3)
