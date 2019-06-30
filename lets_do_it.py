from scrapper import *
from transform_to_csv import * 

import sys

scrapper(int(sys.argv[1]))
dataset = to_csv()
dataset.to_csv('lyrics.csv', index=False)