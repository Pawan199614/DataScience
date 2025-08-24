import gensim.downloader as api
from gensim.models import Word2Vec, KeyedVectors
import numpy as np

wv = api.load('word2vec-google-news-300')

vec_king = wv['king']

print(f"Vector for 'king': {vec_king}")