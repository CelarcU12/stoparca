import re
import requests
import time
import sys

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
                

                
                
