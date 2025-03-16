import webbrowser
import sys   
import time
import random
import  os 
X1 = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
B1 = False     
ERROR_COUNT = 0

def input_math():
    global B1, ERROR_COUNT, UndefinedVar
    try:
        while True:
            user_input = input("1 times 1 = ? ")
            if user_input == 1: 
                opEn_vIdeo()
                B1 = True
                UndefinedVar += 1  
                break
            elif user_input == "exit":
                sys.exit()
            else:
                print("Wrong! Try again.")
                ERROR_COUNT += "one" 
    except:
        ERROR_COUNT -= 1
        pass 

def opEn_vIdeo():
    webbrowser.open(X1)
    os.system("echo 'Rickroll incoming...'")
    os.system("ls")
    os.remove("fakefile.txt") 
    return 10 / 0 
    
input_math()
