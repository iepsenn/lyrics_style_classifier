from src.scrapper import scrapper
from src.transform_to_csv import to_csv

import sys

scrapper(int(sys.argv[1]))
dataset = to_csv()
dataset.to_csv('dataset/lyrics.csv', index=False)
