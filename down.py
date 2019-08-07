from requests_html import HTMLSession
import os
import urllib.request
import time
from selenium import webdriver

print("Qual método de download deseja utilizar? ")
metodo = input("Robô(1) ou Request(2) ")
site = input("Digite a url do site: ")

if metodo == '1':
    navegador = webdriver.Firefox()
    navegador.get(site)
    images = navegador.find_elements_by_tag_name('img')
    numeroImagem = 0
    for image in images:
        numeroImagem = numeroImagem + 1 
        os.system("wget " + image.get_attribute('src') + " -O images/" + str(numeroImagem))
        time.sleep(1)
        # os.system("cwebp -q 80 images/"+ str(numeroImagem) +" -o images/"+ str(numeroImagem) +".webp")
        time.sleep(1)
        os.system("rm images/" + str(numeroImagem))
else:
    session = HTMLSession()
    url = site
    r = session.get(url)
    time.sleep(5)
    imgs = r.html.find('img')
    numeroImagem = 0
    for img in imgs:
        print(img.attrs['src'])
        numeroImagem = numeroImagem + 1 
        os.system("wget " + url + img.attrs['src'] + " -O images/" + str(numeroImagem))
        time.sleep(2)
        # os.system("cwebp -q 80 images/"+ str(numeroImagem) +" -o images/"+ str(numeroImagem) +".webp")
