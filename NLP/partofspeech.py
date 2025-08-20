""" Post tag module to use part of speech tag like noun, verb, adjective etc. """
import nltk

# Download required resources (only first time)
nltk.download("averaged_perceptron_tagger_eng")

# Input sentence
sentence = "The cat is sleeping on the mat"

# Tokenize the sentence into words
words = nltk.word_tokenize(sentence)

print("Tokenized Words:", words)

# POS tagging
pos_tags = nltk.pos_tag(words)

print(pos_tags)
