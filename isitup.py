#Written in Python 3.XX
#This python script will check if an website is up if it is then will sound a beep
import requests
import winsound
import time

req = requests.get('https://www.google.com')
count = 0
while req.status_code !=200:
 count += 1
 time.sleep(10)
 
print('Website is up')
winsound.Beep(300,2000)
