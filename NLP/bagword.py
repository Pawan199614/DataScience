from sklearn.feature_extraction.text import CountVectorizer
# Multiple documents
text = ["It was the best of times", "it was the worst of times", "it was the age of wisdom", "it was the age of foolishness"] 
# create the transform
vectorizer = CountVectorizer(lowercase=True, stop_words='english', max_features=10)
# tokenize and build vocab
vectorizer.fit(text)
# encode documents
vector = vectorizer.transform(text)
# summarize
print(sorted(vectorizer.vocabulary_))
print(vector.shape)
print(vector.toarray())