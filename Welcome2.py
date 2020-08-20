import os
import pyttsx3 as p
import Email as em
p.speak("Welcome to RL Assistant")

print("@"*100)
print("\t\t\t\t\tWelcome to RL Assistant")
print("@"*100)


while True:
    task=""
    a = input("Enter what u want to run tell me :  ")
    a=a.lower()
#    print(a)
    if "chrome" in a or "browser" in a or "web browser" in a:
        task="chrome"
    elif "ms word" in a or "word doc" in a or "winword" in a :
        task="winword"
    elif "presentation" in a or "powerpoint" in a or "power point" in a or "ppt" in a:
        task="powerpnt"
    elif "calculator" in a or "Calculate" in a:
        task="calc"
    elif "weather" in a:
        tast="https://www.google.com/search?q=tody+weather+near+me&oq=tody+weather+near+me&aqs=chrome..69i57j0l7.6542j1j7&sourceid=chrome&ie=UTF-8"
    elif "excel" in a or "spreadsheet" in a :
        task="excel"
    elif "firefox" in a or ("browser" in a and "firefox" in a):
        task="firefox"
    elif "player" in a and "media" in a:
        task="wmplayer"
    elif "vscode" in a or "vs code" in a:
        task="code"
    elif "notepad" in a or "texteditor" in a or "text editor" in a or "editor" in a: 
        task ="notepad"
    elif ("sql" in a or "sqlplus" in a or "sql plus" in a) and "server" not in a:
        task="sqlplus"
    elif "sql" in a and "server" in a or "database homepage" in a:
        task="http://127.0.0.1:8080/apex"
    elif a=="":
        print("Sorry, Please type something")
    elif "exit" in a or "nothing" in a or "quit" in a or "stop" in a  or ("no" in a and  "task" in a)or "no" in a:
        print("Thank u for interacting see u soon")
        break;
    elif "cmd" in a or "command prompt" in a or "terminal" in a or "cli" in a:
        task=""
    elif "camera" in a or "make a video" in a:
        task="microsoft.windows.camera:"
    elif "mail" in a or "email" in a:
        sendermail=input("Enter the sender email id : ")
        passw=input("Enter your password : ")
        recv= input("Enter the mail Id of whom u want to send : ")
        em.send(sendermail,passw,recv)
    else:
        print("Sorry I don't support this")
        a=""
    if a!="":
        os.system("start "+task)
