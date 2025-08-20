"""" The stop word removal like extra word like "the", "is", "at" etc.
This code uses NLTK library to process text, tokenize sentences, and remove stop words."""

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize, wordpunct_tokenize
from nltk.stem import PorterStemmer, SnowballStemmer, RegexpStemmer,WordNetLemmatizer

nltk.download('stopwords')

corps = """
Natural Language Processing (NLP) is a branch of artificial intelligence that helps computers understand, interpret, and generate human language. 
It combines computational linguistics with machine learning and deep learning models. 
NLP is used in many real-world applications such as chatbots, language translation, sentiment analysis, and speech recognition. 
With the growth of digital data, NLP has become increasingly important for extracting insights from large volumes of text. 
Researchers and engineers continue to develop new algorithms to improve the accuracy and efficiency of NLP systems. 
Learning NLP opens up exciting opportunities in data science, allowing professionals to build smarter applications that can interact with users in a more natural way."""

tokenzing = sent_tokenize(corps)
stemer = WordNetLemmatizer()

for word in range(len(tokenzing)):
    words = word_tokenize(tokenzing[word])
    words = [stemer.lemmatize(word,pos="n") for word in words if word not in set(stopwords.words('english'))]  # Remove punctuation and convert to lowercase
    tokenzing[word] = ' '.join(words)

print("Tokenized and Stemmed Corpus:",tokenzing)


