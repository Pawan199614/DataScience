from nltk.stem import WordNetLemmatizer

lemin = WordNetLemmatizer()

words = ["running", "ran", "better", "best", "happily","dogs", "geese"]

for word in words:
    print(f"{word} -> {lemin.lemmatize(word, pos='v')}")