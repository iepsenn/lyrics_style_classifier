import os
import pandas as pd

styles_folders = [
    'axe',
    'sertanejo',
    'gospelreligioso',
    'bossa-nova',
    'forro',
    'mpb',
    'samba'
]


def get_content(folder):
    path = os.path.join("dataset", folder)
    styles = os.listdir(folder)

    txt = []
    label = []

    for style in styles:
        file = os.path.join(path, style)

        with open(file, 'r') as lyric:
            content = lyric.read().replace('\n', '')
        lyric.close()

        txt.append(content)
        label.append(folder)

    return txt, label


def to_csv():
    d = {'lyric': [], 'label': []}
    df = pd.DataFrame(data=d)

    for style in styles_folders:
        lyrics, labels = get_content(style)

        to_add = {'lyric': lyrics, 'label': labels}
        df_to_append = pd.DataFrame(data=to_add)

        df = df.append(df_to_append, ignore_index=True)

    return df
