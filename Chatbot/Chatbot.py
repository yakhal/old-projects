import nltk
from nltk.stem.lancaster import LancasterStemmer
from tensorflow.python.compiler import tensorrt as trt

stemmer = LancasterStemmer()

import numpy
import tensorflow
import random
import json

with open("intents.json") as file:
    data = json.load(file)
    print(data)