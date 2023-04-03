### Imports ###

import pandas as pd
import os
import random
import numpy as np
import json
from keras_preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer

text_file = open("C:/Users/ghilas.aissou/OneDrive - North Dakota University System/Desktop/Kaggle Competition/Data/sample.txt", 'r')
result = text_file.read()
text_file.close()
tokenizer = Tokenizer()
