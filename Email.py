# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 10:49:56 2020

@author: HP
"""
import smtplib as sm
def send(senderemail,senderpass,recieveremail):
    try:
        # Session create through smtp obj
        s= sm.SMTP('smtp.gmail.com',587) #(server location, port no of gmail)
        # to make secure we do TLS(Transport Layer Security) encrypt it
        s.starttls()
        #Login with authen
        s.login(senderemail,senderpass)
        n=0
        while True:
            if n==0:
                a = input("Enter the Message : ")
            else:
                t=input()
                if t!="":
                    a+=("\n"+t)
                else:
                    break;
            n+=1
        print("...................................")    
        message=a
        #Sending email
        s.sendmail(senderemail,recieveremail,message)
        
        #Quit
        s.quit()
        print("Send Successfully.......")
    except :
        print("Something Went Wrong Try again")

if __name__=="__main__":
    rmail=input("Enter the Reciever's Mail : ")
    send("pythontestmail20@gmail.com","Python20",rmail)
    
