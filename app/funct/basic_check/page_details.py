import re
from bs4 import BeautifulSoup
import requests


links = []
data = []
js=[]
domains=[]

def remove_duplicates(l): # remove duplicates and unURL string
    for item in l:
        match = re.search("(?P<url>https?://[^\s]+)", item)
        if match is not None:
            links.append((match.group("url")))

def page_scanner(text):
    print("[+]-----------PAGE-DETAILS-------------------")
    soup = BeautifulSoup(text, 'lxml')
    inputs=[]
    for x in soup.find_all('form'):
        for i in x.find_all(['input', 'button', 'text']):
            inputs.append(i.get('name'))
            if  i.get('type') == "hidden":
                print(" |\033[91m[->]\033[0m"+i.name, i.get('type'),i.get('name'))
            if  i.get('type') == "submit":
                print(" |\033[92m[->]\033[0m"+i.name, i.get('type'),i.get('name'))
            else:
                print(" |\033[97m[->]\033[0m"+i.name, i.get('type'),i.get('name'))

    for link in soup.find_all('a', href=True):
        data.append(str(link.get('href')))
        
    for link in soup.find_all('script', src=True):
        js.append(str(link.get('src')))

    #for link in soup.find_all('script'):
        #js.append(str(link.get('src')) if str(link.get('src')) else continue)
    remove_duplicates(data)
    print("[+]**Links on the page")
    for link in links:
        if str(link.split('://')[1].split('?')[0].split('/')[0]) not in domains:
            domains.append(str(link.split('://')[1].split('?')[0].split('/')[0]))
            s_c=requests.get(link).status_code
            if s_c == 200:
                print(" |\033[34m"+link.split('://')[1].split('?')[0]+":\033[32m"+str(s_c)+"\033[0m")
            else:
                print(" |\033[34m"+link.split('://')[1].split('?')[0]+":\033[31m"+str(s_c)+"\033[0m")
    print("\r\n\r\n[+] JAVASCRIPT FILES")         
    for i in js:
        if 'http' not in str(i):
            print("  |\033[34m"+"FILE"+":\033[32m"+str(i)+"\033[0m")
    print("\r\n\r\n[+] JAVASCRIPT URLS")         
    for i in js:
        if 'https' not in str(i):
            print("  |\033[34m"+"FILE"+":\033[32m"+str(i)+"\033[0m")