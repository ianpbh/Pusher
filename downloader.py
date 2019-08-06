from requests_html import HTMLSession
import os
import urllib.request
import time
session = HTMLSession()
url = input("Digite o endereço do site: ")
r = session.get(url)
imgs = r.html.find('img')
numeroImagem = 0
for img in imgs:
    numeroImagem = numeroImagem + 1 
    os.system("wget " + img.attrs['src'] + " -O images/" + str(numeroImagem))
    time.sleep(2)
