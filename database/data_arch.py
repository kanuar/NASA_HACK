'''
run these codes on google colab for faster speeds 

before running them  add a cell to colab which runs these commands below
!pip install wget
!pip install requests_html
'''
from zipfile import ZipFile
import requests
from requests_html import HTMLSession
import wget
from bs4 import BeautifulSoup

outp4={}
url_main='https://www.missionjuno.swri.edu/junocam/processing?id='
#id1=[x for x in range(624,13927)]
id1=[x for x in range(9856,13140)]
for i in id1:
    print(i)
    u1=url_main+str(i)
    html_page = requests.get(u1).text
    soup = BeautifulSoup(html_page, "lxml")
    s1=soup.find_all('title')
    if not(('PJ' in str(s1))or('Perijove' in str(s1))):
        continue
    s1=(str(s1[0]).split("'"))[1]
    print(s1)
    op=[]
    for link in soup.findAll('a'):
        k=link.get('href')
        if 'Download' in k:
            op.append(k)
    op=set(op)
    if op=={}:
        continue
    links=[]
    for j in op:
        url2='https://www.missionjuno.swri.edu'
        k=url2+j
        print(k)
        links.append(k)

    outp4[i]=links


print('completed')

f=open("file4.txt",'w')
f.write(outp1)
f.close()
'''
        wget.download(k)
        f1=str(i)+'-Data.zip'
        f2=str(i)+'-ImageSet.zip'
        with ZipFile(f1,'r') as zipobj:
            zipobj.extractall()
        with ZipFile(f2,'r') as zipobj:
            zipobj.extractall()
'''
