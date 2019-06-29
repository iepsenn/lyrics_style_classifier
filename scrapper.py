import pandas as pd
import requests
from bs4 import BeautifulSoup
from time import sleep

styles = ['axe', 'sertanejo', 'gospelreligioso', 'bossa-nova', 'forro', 'mpb', 'samba']

link = "https://www.letras.mus.br/"

print("Scrapping from {}\n".format(link))

#estilo = "mais-acessadas/samba"
#to_request = link + estilo
#print(to_request)

import random

def get_lyrics_link(lyrics_number, style):
    
    lyric_style = "mais-acessadas/" + str(style)
    to_request = link + lyric_style
    
    try:
        req = requests.get(to_request)
    except:
        if req.status_code != 200:
           	print("Requisição falhou!!!")
            content = req.content
            exit(1)
    else:
        if req.status_code == 200:
            print('Requisição ok!!!')
            content = req.content

    soup = BeautifulSoup(content, 'html.parser')
    lyrics_redirection = soup.findAll('ol', {"class": "top-list_mus cnt-list--col1-3"})

    lyrics_list = lyrics_redirection
    
    links = []
    for a in lyrics_list:
        anchors = a.findAll('a', href=True)
        #print(anchors)
        for href in anchors:
            #print(link['href'])
            lyrics_link = link + href['href']
            #print(lyrics_link)
            links.append(lyrics_link)

    return random.sample(links, lyrics_number)

get_lyrics_link(5, "samba")

import random
import os
from time import sleep 

def get_lyrics(links, style):
    
    print("Scrapping {} lyrics".format(style))
    
    os.system(("mkdir %s")%(style))
    
    for to_request in links:        
        try:
            req = requests.get(to_request)
        except:
            if req.status_code != 200:
                print('Requisição falhou!!!')
                content = req.content
                exit(1)
        else:
            if req.status_code == 200:
                #print('Requisição ok!!!')
                content = req.content

        soup = BeautifulSoup(content, 'html.parser')
        lyrics_redirection = soup.findAll('article')
        title = soup.findAll('div', {'class': 'cnt-head_title'})

        song = (str([t.findAll('h1')for t in title][0]).split('<h1>')[-1]).split('</h1>')[0]
        artist = str([t.findAll('h2')for t in title][0]).split('/')[1]
        
             
        lyrics_content = lyrics_redirection

        lyrics_letter = ""
        for a in lyrics_content:
            texts = a.findAll('p')
            
            for text in texts:
                letter = str(text)[3:-4] #to remove <p></p>

                letter = letter.split('<br>')
                letter_ = ""
                for l in letter:
                    letter_ += l + " "

                letter = letter_

                letter = letter.split('</br>')
                letter_ = ""
                for l in letter:
                    letter_ += l + " "

                letter = letter_

                letter = letter.split('<br/>')
                letter_ = ""
                for l in letter:
                    letter_ += l + " "

                letter = letter_

                lyrics_letter += letter + " "

        filename = str(song) + "(" + str(artist) + ").lyric"

        with open(filename, "w") as lyric:
            lyric.write(lyrics_letter)

        lyric.close()
        
        sleep(2)
     
    os.system(("mv *lyric %s") % (style))
    
    print("{} lyrics scrapped suscefull".format(style))

links = get_lyrics_link(5, "samba")
get_lyrics(links, "samba")

def scrapper(number_of_samples):
    for style in styles:
        links = get_lyrics_link(number_of_samples, style)
        get_lyrics(links, style)

import sys
scrapper(1)