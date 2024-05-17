import cloudscraper
import contextlib
import datetime
import hashlib
import os
import os.path
import pytz
import random
import requests
import sys
import time
import tldextract
import webbrowser
import re
import certifi
from bs4 import BeautifulSoup
from colorama import init, Fore, Style
from concurrent.futures import ThreadPoolExecutor, as_completed
from importlib import reload
from queue import Queue

init(autoreset=True)
reload(sys)

r = Fore.RED + Style.BRIGHT
g = Fore.GREEN + Style.BRIGHT
c = Fore.CYAN + Style.BRIGHT
y = Fore.YELLOW + Style.BRIGHT
o = Fore.RESET + Style.RESET_ALL

banner = """

    {}[!]   {} NOSPEEP ENDLIFE V3{} - {}REVERSE IP PRIV8{}
           {}CODED BY TUX-MACG1V & MR.B & N0LLb1t3{}
           {}https://t.me/I_am_a_silent_killer{}
           {}SUPPORT ME AND GIVE ME A TREAT{}
           {}TRC20-  TEd4f33f2c2AVGaB14VFCZbVLCe9hirNtK
           BTC -  1KP3ekYeQGNVpMJr8P4hwwPPQ5sFP4h2Xb{}
""".format(r, g, y, g, o, y, o, y, o, r, o, g, o)

exame = os.path.splitext(os.path.basename(__file__))[0]
folder_name = "Result"

headerys = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/91.0.4472.124 Safari/537.36'}


class useragents:
    agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36"]


def cls():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


if not os.path.exists(folder_name):
    try:
        os.mkdir('Result')
        os.getcwd()
    except OSError:
        print(f"{r}[Error creating result folder]")
cls()


def save(i):
    mylist = []
    yy = r'Result/dom.txt'
    with contextlib.suppress(Exception):
        if not i.startswith("http://") and not i.startswith("https://"):
            i = f"http://{i}"
    if not os.path.exists(yy):
        new_file = open('Result/dom.txt', 'a+', encoding="utf-8", errors="ignore")
        new_file.close()
    if len(mylist) > 1:
        mylist.clear()
        mylist.append(i)
        open(yy, "a+", encoding="utf-8",  errors="ignore").write(i + "\n")
    elif i not in mylist:
        mylist.append(i)
        open(yy, "a+", encoding="utf-8",  errors="ignore").write(i + "\n")

class tld:
    def extract(domain):
        domain = tldextract.extract(str(domain)).domain + "." + tldextract.extract(str(domain)).suffix
        return domain

class rapiddns:
    def ext_domain(ip):
        hypetime = random.uniform(0.2, 2)
        time.sleep(hypetime)
        endpoint = f"https://rapiddns.io/sameip/{ip}?full=1&t=None#result"
        User_agent = {"User-Agent": random.choice(useragents.agents)}
        try:
            req = requests.get(endpoint, headers=User_agent, timeout=2)
            if "Same IP Website" in req.text:
                soup = BeautifulSoup(req.text, "html.parser")
                table = soup.find("table", {"class": "table table-striped table-bordered"})
                tbody = table.find("tbody")
                tr = tbody.find_all("tr")
                print(f"{r}[+]{g} FROM {y} {ip}  == DOMAINS{g}[{r}{(len(tr))}{g}]")
                for i in tr:
                    td = i.find_all("td")
                    domain = (tld.extract(td[0].text))
                    save(domain)
            else:
                pass
        except:
            pass

class tntcode:
    def ext_domain(ip):
        endpoint = f"https://domains.tntcode.com/ip/{ip}"
        User_agent = {"User-Agent": random.choice(useragents.agents)}
        try:
            hype = random.uniform(1, 7)
            time.sleep(hype)
            req = cloudscraper.create_scraper()
            req = req.get(endpoint, headers=User_agent, timeout=2)
            if req.status_code == 200:
                soup = BeautifulSoup(req.text, "html.parser")
                textarea = soup.find("textarea")
                domains = textarea.text.split("\n")
                print(f"{r}[+]{g} FROM {y} {ip}  == DOMAINS{g}[{r}{(len(domains))}{g}]")
                for domain in domains:
                    save(str(domain))
            else:
                pass
        except Exception:
            pass

class spyonweb:
    def ext_domain(ip):
        try:
            hypetime = random.uniform(1, 4)
            time.sleep(hypetime)
            endpoint = f"http://ip.yqie.com/iptodomain.aspx?ip={ip}"
            user_agent = {"User-Agent": random.choice(useragents.agents)}
            req = requests.get(endpoint, headers=user_agent, timeout=2)
            if req.status_code == 200:
                soup = BeautifulSoup(req.text, "html.parser")
                table = soup.find('table', class_='table')
                data_rows = table.find_all('tr')[1:]
                domains = [row.find_all('td')[1].text.strip() for row in data_rows]
                print(f"{r}[+]{g} FROM {y} {ip}  == DOMAINS{g}[{r}{(len(domains))}{g}]")
                for domain in domains:
                    domain = (tld.extract(domain))
                    save(domain)
            else:
                pass
        except Exception:
            pass

class webscan:
    def ext_domain(ip):
        try:
            url = f"https://api.webscan.cc/?action=query&ip={ip}"
            User_agent = {"User-Agent": random.choice(useragents.agents)}
            response = requests.get(url, headers=User_agent, timeout=2).json()
            for i in range(len(response)):
                domain = response[i]["domain"]
                print(f"{r}[+]{g} FROM {y} {ip}  == DOMAINS{g}[{r}{(len(domain))}{g}]")
                domains = tld.extract(domain)
                save(domains)
        except Exception:
            pass

class lol1:
    def rev3(ip):
        try:
            req1 = requests.get('https://networksdb.io/domains-on-ip/'+str(ip), timeout=5, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0'}).text
            rr = re.findall('<pre class="threecols">.*?</pre>',req1, re.DOTALL)[0]
            rr = rr.replace('<pre class="threecols">','').replace('</pre>','')
            domains = rr.split('\n')
            print(f"{r}[+]{g} FROM {y} {ip}  == DOMAINS{g}[{r}{(len(domains))}{g}]")
            for domain in domains:
                domain = (tld.extract(domain))
                save(domain)
        except:
            pass

class lol2:
    def rev4(ip):
        try:
            req1 = requests.get('https://www.chaxunle.cn/ip/'+str(ip)+'.html', timeout=5, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0'}).text
            rrr = re.findall("https://www.chaxunle.cn/ip/(.*?).html", req1)
            domains = rrr
            print(f"{r}[+]{g} FROM {y} {ip}  == DOMAINS{g}[{r}{(len(domains))}{g}]")
            for domain in domains:
                domain = (tld.extract(domain))
                save(domain)
        except:
            pass

def process_task2(line, q):
    q.put(rapiddns.ext_domain(line.strip()))
    q.put(tntcode.ext_domain(line.strip()))
    q.put(spyonweb.ext_domain(line.strip()))
    q.put(webscan.ext_domain(line.strip()))
    q.put(lol1.rev3(line.strip()))
    q.put(lol2.rev4(line.strip()))

def process_task1(line, q):
    q.put(rapiddns.ext_domain(line.strip()))
    q.put(webscan.ext_domain(line.strip()))
    q.put(lol1.rev3(line.strip()))
    q.put(lol2.rev4(line.strip()))

def worker_proc2(file, thread):
    cls()
    try:
        q = Queue()
        with ThreadPoolExecutor(max_workers=int(thread)) as executor:
            with open(file, "r") as f:
                tasks = [executor.submit(process_task2, line.strip(), q) for line in f]
                for task in as_completed(tasks):
                    try:
                        task.result()
                    except Exception:
                        os.system(f"taskkill /f /im  {exame}.exe")
                executor.shutdown(wait=True)
        os.system(f"taskkill /f /im  {exame}.exe")
        return q
    except Exception:
        print("Invalid thread")

def worker_proc1(file, thread):
    cls()
    try:
        q = Queue()
        with ThreadPoolExecutor(max_workers=int(thread)) as executor:
            with open(file, "r") as f:
                tasks = [executor.submit(process_task1, line.strip(), q) for line in f]
                for task in as_completed(tasks):
                    try:
                        task.result()
                    except Exception:
                        os.system(f"taskkill /f /im  {exame}.exe")
                executor.shutdown(wait=False)
        os.system(f"taskkill /f /im  {exame}.exe")
        return q
    except Exception:
        print("Invalid thread")

def func2():
    file = input(f"\n{r}[+]{g} GIVE ME IP LISTS: {y}")
    thread = 100
    q = worker_proc2(file, thread)
    while not q.empty():
        print(q.get())

def func1():
    file = input(f"\n{r}[+]{g} GIVE ME IP LISTS: {y}")
    thread = 100
    q = worker_proc1(file, thread)
    while not q.empty():
        print(q.get())

def tools():
    cls()
    print("""
{}[+] {}OPTION{} :{}    [1] {}CAN'T SLEEP {}-{} FAST BUT LESS DOMAIN{}{}
                [2] {}CAN SLEEP   {}-{} SLOW BUT MORE DOMAIN{}{}

                [99] {}{}Exit{}{}

""".format(r, g, r, y, g, y, g, c, y, g, y, g, c, y, g, r, r, y, o))

    press = input('{}[?] {}CHOOSE{} > {}'.format(r, g, o, r))
    if press == '1':
        func1()
    elif press == "2":
        func2()
    elif press == "99":
        print('\n[+] {}THANKS FOR USEING MY TOOL'.format(g))
        time.sleep(5)
        sys.exit()
    else:
        print('\n[+] {}THIS TOOL IS NOT FOR YOU'.format(g))
        time.sleep(5)
        sys.exit()

def main():
    global time_remining
    cls()
    print(banner)
    print(f" {r}         {g}    YOUR LICENSE VALID FOR{y} {hours_remaining:.2f} DAYS{o}")
    try:
        tools()
    except requests.exceptions.SSLError:
        print(f"\n{y}[-] {r}CHECK YOUR NETWORK CONNECTION{o}")
        time.sleep(5)
        os.system(f"taskkill /f /im  {exame}.exe")



def check_license():
    global hours_remaining
    timezone = pytz.timezone("Asia/Calcutta")
    now = datetime.datetime.now(timezone)
    expiration_date = datetime.datetime(2050, 2, 10, 0, 0, 0, tzinfo=timezone)
    if now < expiration_date:
        time_difference = expiration_date - now
        hours_remaining = time_difference.days
        main()
    else:
        print(f"\n\n{g}[!]{r} YOUR LICENSE HAS EXPIRED.....{o}")
        print(f"{y}[!] {g}CONTACT WITH TUX-MACG1V {o}")
        webbrowser.open('https://t.me/I_am_a_silent_killer', new=2)
        time.sleep(20)

if __name__ == "__main__":
    check_license()
