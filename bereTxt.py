import re
import requests
import time
import sys
imeFile='farm.txt'
st=0

class Farma:
                def __init__(self,x,y):
                                self.x=x
                                self.y=y
                def __str__(self):
                                return "( "+str(self.x)+" | "+ str(self.y)+" )"
                def __repr__(self):
                                return "( "+str(self.x)+" | "+ str(self.y)+" )"
                
def shraniVSeznam(imeDat):
                seznamFarm=[]
                for vr in open(imeFile,'r'):
                                if st%2 ==0:
                                                print(vr)
                                                niz=  re.split("( | )",vr)
                                                print(niz[2].split("|"))
                                                x,y =niz[2].split("|")
                                                seznamFarm+=[Farma(int(x),int(y))]
                                st+=1
                return seznamFarm

url = 'https://tx3.travian.com/'
usr = 'Office'
psw='v.i.p.'

def login():
                with requests.Session(config = {'verbose':sys.stderr }) as r:
                                r.post(url+'login.php', data={'username':usr,'password':psw,'login':str(int(time.time())),
                                              'lowRes':0, 's1': 'Login', 'w': '1920:1080'})
                                c= r.get(url+'dorf1.php')
                print(c.status_code)

login()
                

                
                
