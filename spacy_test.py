import spacy

"""
SPACY DEPENDENCY LABELS:
ROOT     -- main verb
nsubj    -- subject performing the action
dobj/obj -- direct object
compound -- part of a multi-word noun
amod     -- adjective modifier
prep     -- preposition
pobj     -- object of a preposition
"""

nlp = spacy.load("en_core_web_sm")

with open(r"C:\Users\ihita\OneDrive - Lake Washington School District\_2025-2026\Other\Research\PDFs\1.1.txt",
          "r",
          encoding="utf-8") as f:
    text = f.read()

doc = nlp(text)

sentence = list(doc.sents)[0]

print(sentence.text)

for token in sentence:
    print(
        token.text,
        token.dep_,
        token.head.text
    )