"""steming is used to reduce words to their root form. like 'running' to 'run'
there are two types of stemming algorithms:
porter stemmer and snowball stemmer.
snowball stemmer is an improvement over porter stemmer.
"""
from nltk.stem import PorterStemmer, SnowballStemmer,RegexpStemmer

words = ['running', 'ran', 'easily', 'fairly']

porter = PorterStemmer()
snowball = SnowballStemmer('english')

"""print("Porter Stemmer Results:")
for word in words:
    print(f"{word} -> {porter.stem(word)}")
    print("\nSnowball Stemmer Results:")
    print(f"{word} -> {snowball.stem(word)}")
    print()"""


regexp = RegexpStemmer('ing$|s$|ed$', min=4)
print("Regexp Stemmer Results:")
regexp.stem('running')
print(regexp.stem('running'))  # Output: run



