import os
import random
import requests
from bs4 import BeautifulSoup
from time import sleep

styles = [
    'axe',
    'sertanejo',
    'gospelreligioso',
    'bossa-nova',
    'forro',
    'mpb',
    'samba'
]
link = "https://www.letras.mus.br/"

print("Scrapping from {}\n".format(link))


def get_lyrics_link(lyrics_number, style):

    lyric_style = "mais-acessadas/" + str(style)
    to_request = link + lyric_style

    req = requests.get(to_request)
    if req.status_code != 200:
        raise Exception(
            f"(HTTP code status: {req.status_code}) Requisição falhou!!!"
        )

    content = req.content
    soup = BeautifulSoup(content, 'html.parser')
    lyrics_redirection = soup.findAll(
        'ol', {"class": "top-list_mus cnt-list--col1-3"})

    lyrics_list = lyrics_redirection

    links = []
    for a in lyrics_list:
        anchors = a.findAll('a', href=True)
        for href in anchors:
            lyrics_link = link + href['href']
            links.append(lyrics_link)

    return random.sample(links, lyrics_number)


def get_lyrics(links, style):

    print("Scrapping {} lyrics".format(style))
    os.makedirs(os.path.join("dataset", style))

    n_samples = len(links)
    c_sample = 0

    for to_request in links:
        req = requests.get(to_request)
        if req.status_code != 200:
            raise Exception(
                f"(HTTP code status: {req.status_code}) Requisição falhou!!!"
            )

        content = req.content
        soup = BeautifulSoup(content, 'html.parser')
        lyrics_redirection = soup.findAll('article')
        title = soup.findAll('div', {'class': 'cnt-head_title'})

        song = (
            str([t.findAll('h1')for t in title][0])
            .split('<h1>')[-1]
        ).split('</h1>')[0]
        artist = str([t.findAll('h2')for t in title][0]).split('/')[1]

        c_sample += 1
        print('getting sample: {}/{}'.format(c_sample, n_samples))

        lyrics_content = lyrics_redirection

        lyrics_letter = ""
        for a in lyrics_content:
            texts = a.findAll('p')

            for text in texts:
                letter = str(text)[3:-4]  # to remove <p></p>

                letter = letter.split('<br>')
                letter_ = ""
                for text in letter:
                    letter_ += text + " "

                letter = letter_

                letter = letter.split('</br>')
                letter_ = ""
                for text in letter:
                    letter_ += text + " "

                letter = letter_

                letter = letter.split('<br/>')
                letter_ = ""
                for text in letter:
                    letter_ += text + " "

                letter = letter_

                lyrics_letter += letter + " "

        filename = str(song) + "(" + str(artist) + ").lyric"

        try:
            with open(filename, "w") as lyric:
                lyric.write(lyrics_letter)

            lyric.close()
            sleep(1)

        except Exception:
            pass

    os.system(("mv *lyric %s") % (style))

    print("{} lyrics scrapped successful".format(style))


def scrapper(number_of_samples):
    for style in styles:
        links = get_lyrics_link(number_of_samples, style)
        get_lyrics(links, style)
