import re
from bs4 import BeautifulSoup
import requests


links = []
data = []
domains=[]

def remove_duplicates(l): # remove duplicates and unURL string
    for item in l:
        match = re.search("(?P<url>https?://[^\s]+)", item)
        if match is not None:
            links.append((match.group("url")))

def page_scanner(text):
    print("-----------PAGE-DETAILS-------------------")
    soup = BeautifulSoup(text, 'lxml')
    inputs=[]
    for x in soup.find_all('form'):
        for i in x.find_all(['input', 'button', 'text']):
            inputs.append(i.get('name'))
            print(i.name, i.get('type'),i.get('name'))
        print('---')

    for link in soup.find_all('a', href=True):
        data.append(str(link.get('href')))
    remove_duplicates(data)
    print("**Links on the page")
    for link in links:
        if str(link.split('://')[1].split('?')[0].split('/')[0]) not in domains:
            domains.append(str(link.split('://')[1].split('?')[0].split('/')[0]))
            s_c=requests.get(link).status_code
            if s_c == 200:
                print("\033[34m"+link.split('://')[1].split('?')[0]+":\033[32m"+str(s_c)+"\033[0m")
            else:
                print("\033[34m"+link.split('://')[1].split('?')[0]+":\033[31m"+str(s_c)+"\033[0m")
