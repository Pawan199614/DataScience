import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize, wordpunct_tokenize
#from nltk.tokenize import sent_tokenize, word_tokenize,wordpunct_tokenize


try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')
#nltk.download('punkt_tab')
Corpus = """Hello Welcome's, to pawan rajpurohit NLP Learning. Please Learn entier course! to become expert in NLP.""" 
documents = sent_tokenize(Corpus)
words = word_tokenize(Corpus)
# this function used to split into words and also punct example pawan's like ' and s split into two words
wordpunc = wordpunct_tokenize(Corpus)
print("wordpucnt tokenize :",wordpunc)
#print("words tokenize :",words)