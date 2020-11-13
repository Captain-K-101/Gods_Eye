import requests
from funct.helpers import colors

def spf(url):
    if url[:4]=='http':
        url=url.split('//')[1]
    if len(url.split('/'))>1:
        url=url.split('/')[0]
    if len(url.split('.'))>2:
        url=url.split('.')
        url[0]=''
        url='.'.join(url)
        url=url[1:]
    data={'serial':'fred12','domain':url}
    print("The domain: "+url)
    a=requests.post('https://www.kitterman.com/spf/getspf3.py',data=data).text
    spf=a.split('<body>')[1].split('<form method="get')[0].replace('<br>','').replace('<p>','').replace('</p>','')
    if '-all' not in spf:
        print("The domain "+url+" is "+colors.green+"VULNEARBLE"+colors.end+" to spf spoofing")
    else:
        print("The domain "+url+" is "+colors.red+"NOT VULNEARBLE"+colors.end+" to spf spoofing")
    