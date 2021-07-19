import json
import os
import argparse
from funct.basic_check.Bcheck import *
from funct.helpers import colors
from funct.basic_check.cms_detector import *

a=colors.yellow+'''
 \t  _____       _____   _____   ________     ________ 
 \t / ____|     |  __ \ / ____| |  ____\ \   / /  ____|
 \t| |  __  ___ | |  | | (___   | |__   \ \_/ /| |__   
 \t| | |_ |/ _ \| |  | |\___ \  |  __|   \   / |  __|  
 \t| |__| | (_) | |__| |____) | | |____   | |  | |____ 
 \t \_____|\___/|_____/|_____/  |______|  |_|  |______|
                                                     
                                                     
'''+colors.end
os.system('clear')
print(a)
parser = argparse.ArgumentParser('')
parser.add_argument('-u',help="Enter An Valid URL")
args=parser.parse_args()

if not args.u:
    exit("No Url Parameter Found")
if not args.u.startswith('http'):
    exit("Invalid Url did you mean https://"+args.u)

url =str(args.u)
check(url)
#scan(url)

