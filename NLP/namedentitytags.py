"Name entity used to tag the text for named entities like person, organization, location etc."
import nltk

nltk.download("maxent_ne_chunker_tab")
word = "Barack Obama was the 44th President of the United States."

# Tokenize the sentence into words
words = nltk.word_tokenize(word)
print("Tokenized Words:", words)
# POS tagging
pos_tags = nltk.pos_tag(words)
print("POS Tags:", pos_tags)    
# Named Entity Recognition
named_entities = nltk.ne_chunk(pos_tags)
print("Named Entities:", named_entities)
# Display the named entities in a readable format
for subtree in named_entities:
    if hasattr(subtree, 'label'):
        print(f"{subtree.label()}: {' '.join(word for word, pos in subtree.leaves())}")
    else:
        print(f"Word: {subtree[0]}, POS: {subtree[1]}")