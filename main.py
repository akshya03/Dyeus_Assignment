from selenium1 import facebook_bot
import json
from time import sleep
import time

if __name__=='__main__':
    with open('config.json') as file:
        config=json.load(file)
    driver=config['driver']
    url=config['url']

    #This section can be used to use predefined userid and password
    #username=config['username']
    #password=config['password']    

    username=input("Enter your email:")
    password=input("Enter your password:")
    fb=facebook_bot(driver,url,username,password)
    sleep(4)
    print("Logged In successfully")
    print("Enter 1 to update status.\nEnter 2 to comment on random friend's recent post.\nEnter 0 to exit.")
    f=int(input("Enter your choice:"))

    while(f in [1,2]):
        if(f==1):
            msg=input("Enter your Status message:")
            fb.update_status(msg)
        elif(f==2):
            msg=input("Enter comment message:")
            fb.comment(msg)
        
        f=int(input("Enter your choice"))
    
    print("Program terminated")

