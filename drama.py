import webbrowser
import colorama
import os
import time
from colorama import Fore, Back, Style

os.system('cls')
print (Fore.WHITE+Style.NORMAL+"-" * 110)
print ()
print(Fore.GREEN+'''
    M""""""'YMM                                       MM""""""""`M oo                dP                   
    M  mmmm. `M                                       MM  mmmmmmmM                   88                   
    M  MMMMM  M 88d888b. .d8888b. 88d8b.d8b. .d8888b. M'      MMMM dP 88d888b. .d888b88 .d8888b. 88d888b. 
    M  MMMMM  M 88'  `88 88'  `88 88'`88'`88 88'  `88 MM  MMMMMMMM 88 88'  `88 88'  `88 88ooood8 88'  `88 
    M  MMMM' .M 88       88.  .88 88  88  88 88.  .88 MM  MMMMMMMM 88 88    88 88.  .88 88.  ... 88       
    M       .MM dP       `88888P8 dP  dP  dP `88888P8 MM  MMMMMMMM dP dP    dP `88888P8 `88888P' dP       
    MMMMMMMMMMM                                       MMMMMMMMMMMM                                        ''')
print ()
print (Fore.WHITE+Style.NORMAL+"-" * 110)
print ()
print (Fore.MAGENTA+' (Drama Finder v6.9)')
print ()
print (Fore.RED+" (0) Thoát")
print (Fore.YELLOW+" (1) Dò tìm drama để cho bạn hóng!")
print ()
print (Fore.GREEN+" Lựa chọn: "+Fore.WHITE, end='')
x = input()
if x == ("0"):
    exit()

elif x == ("1"):
    os.system('cls')
    print(Fore.GREEN+'''
                         _____                            ______ _           _           
                        |  __ \                          |  ____(_)         | |          
                        | |  | |_ __ __ _ _ __ ___   __ _| |__   _ _ __   __| | ___ _ __ 
                        | |  | | '__/ _` | '_ ` _ \ / _` |  __| | | '_ \ / _` |/ _ \ '__|
                        | |__| | | | (_| | | | | | | (_| | |    | | | | | (_| |  __/ |   
                        |_____/|_|  \__,_|_| |_| |_|\__,_|_|    |_|_| |_|\__,_|\___|_|   ''')
    print()
    print(Fore.MAGENTA)
    a = input(" Chọn nền tảng mạng xã hội để tìm drama (Facebook, Twitter, TikTok, Youtube): ")
    if a == ("Facebook"):
        webbrowser.open('https://www.facebook.com/search/top/?q=drama', new=1)
        webbrowser.open('https://www.facebook.com/search/top?q=phốt', new=1)
        time.sleep(3)
        print(Fore.RED+' (0) Thoát')
        print()
        print(Fore.GREEN + " Lựa chọn: "+Fore.WHITE, end='')
        restart = input()
        if restart == ("0"):
            exit()

    elif a == ("Twitter"):
        xd = input(" Chọn ngôn ngữ để hóng drama (English, Vietnamese): ")
        if xd == ("Vietnamese"):
            webbrowser.open('https://twitter.com/search?q=phốt&src=typed_query&f=top&lf=on', new=1)     
        time.sleep(3)
        print(Fore.RED+' (0) Thoát')
        print()
        print(Fore.GREEN + " Lựa chọn: "+Fore.WHITE, end='')
        restart = input()
        if restart == ("0"):
            exit()  
    elif a == ("TikTok"):
        webbrowser.open('https://www.tiktok.com/search?q=phốt&t=1655526781173', new=1)
        webbrowser.open('https://www.tiktok.com/search?q=drama&t=1655526829748', new=1)
        time.sleep(3)
        print(Fore.RED+' (0) Thoát')
        print()
        print(Fore.GREEN + " Lựa chọn: "+Fore.WHITE, end='')
        restart = input()
        if restart == ("0"):
            exit()
    elif a == ("Youtube"):
        webbrowser.open('https://www.youtube.com/results?search_query=phốt', new=1)
        webbrowser.open('https://www.youtube.com/results?search_query=drama', new=1)
        time.sleep(3)
        print(Fore.RED+' (0) Thoát')
        print()
        print(Fore.GREEN + " Lựa chọn: "+Fore.WHITE, end='')
        restart = input()
        if restart == ("0"):
            exit()        