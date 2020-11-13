import requests
from Wappalyzer import Wappalyzer, WebPage
import re
from funct.basic_check.csp_checker import *
from funct.basic_check.page_details import *
from funct.helpers import colors
from funct.basic_check.mailchecker import *

headers=[]
def normal_check(k):
    arr=["Last-Modified","set-cookie","Date","Content-L","Content-T","ETag","Accept-Ranges","Connection","Keep-Alive"]
    for i in arr:
        if i.lower() in k.lower():
            return 0
    return 1

def check(url):
    csp_flag=1
    print("\n\t----------Server_Details-----------")
    for i in range(0,3):
        God_request =all_fun(i,url)
        y=God_request.headers
        csp=""
        for (k, v) in y.items():
            if normal_check(k):
                if 'content-security' in k.lower():
                    csp=str(v)
                    break
                if k not in headers:
                    print(colors.blue+k+":"+colors.darkgreen+v+colors.end)
                    headers.append(k)

        if csp and csp_flag:
            csp_flag=0
    csp_checker(csp)
    spf(url)
    page_scanner(all_fun(0,url).content)
    

def csp_checker(v):
    print("\t-----------CSP-------------\t")
    csp_arr=['default-src',' upgrade-insecure-requests','block-all-mixed-content','script-src','style-src','img-src','media-src','font-src','frame-src','object-src','child-src','worker-src','manifest-src']
    csp=v.replace('; ',';').replace('/http',' http')
    #print(re.findall('(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-?=%.]+', str(csp)))
    csp=csp.split(';')
    got_headers=[]
    for i in csp[:-1]:
        #print("\033[31m"+i.split(' ')[0]+":\033[32m"+(''.join(i.split(' ')[1:]))+"\033[0m")
        csper(str(i.split(' ')[0]),(''.join(i.split(' ')[1:])))
        got_headers.append(i.split(' ')[0])
    a=list(set(csp_arr)-set(got_headers))
    print("A Few CSP-Header's Not Found")
    print(*a, sep = "\033[31m ")  
    print("\033[0m")

def all_fun(i,url):
    try:
        if i ==0:
            print(colors.red+"--------GET------------"+colors.end)
            return requests.get(url)
        elif i==1:
            print(colors.red+"--------POST------------"+colors.end)
            return requests.post(url,data={})
        elif i==2:
            print(colors.red+"--------OPTIONS------------"+colors.end)
            return requests.options(url)
        else:
            print("none")
            return []
    except:
        exit("some error occured")
