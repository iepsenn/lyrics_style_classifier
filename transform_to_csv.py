import os 
import pandas as pd

styles_folders = ['axe', 'sertanejo', 'gospelreligioso', 'bossa-nova', 'forro', 'mpb', 'samba']


file = os.listdir('axe')[0]
file = 'axe/' + file


def get_content(folder):
    path = folder + "/"
    lyrics = os.listdir(folder)
    
    txt = []
    label = []
    
    for l in lyrics:
        file = path + l
        
        with open(file, 'r') as lyric:
            content = lyric.read().replace('\n', '')
        lyric.close()

        txt.append(content)
        label.append(folder)
    
    return txt, label


def to_csv():
    d = {'lyric' : [], 'label': []}
    df = pd.DataFrame(data=d)
    
    for style in styles_folders:
        lyrics, labels = get_content(style)
        
        to_add = {'lyric' : lyrics, 'label': labels}
        df_to_append = pd.DataFrame(data=to_add)
        
        df = df.append(df_to_append, ignore_index=True)
    
    return df


#dataset = to_csv()
#dataset.to_csv('lyrics.csv', index=False)

