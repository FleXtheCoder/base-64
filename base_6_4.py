# Modules importation
import os
import base64
import time

try:
    from colorama import Fore, init
except:
    os.system("py -m pip install colorama")
    from colorama import Fore, init
init()

banner = (Fore.MAGENTA + """
                                                                                                            
                                                                                                                                                                    
________________________________   ____________ __
___  __ )__    |_  ___/__  ____/   __  ___/_  // /
__  __  |_  /| |____ \__  __/      _  __ \_  // /_
_  /_/ /_  ___ |___/ /_  /___      / /_/ //__  __/
/_____/ /_/  |_/____/ /_____/      \____/   /_/   
                                                  
                                                                                         
                                                                                                                                                                            
                                                                                                           
                                                                                      
                                                                                      """ + Fore.CYAN)
print(banner)
userid = input(" [INPUT] RAW : ")
encodedBytes = base64.b64encode(userid.encode("utf-8"))
encodedStr = str(encodedBytes, "utf-8")
print(f'\n [LOGS] BASE 64 output : {encodedStr}')
time.sleep(1.5)
print("\n")
print(Fore.LIGHTBLACK_EX +"press any button to exit...")
os.system('pause >nul')  # Pause command in Batch (press any key to exit the code)


