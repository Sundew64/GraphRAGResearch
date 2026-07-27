import spacy

triples_list = []

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

sentence = list(doc.sents)[3]

for sentence in list(doc.sents):
    print(sentence.text)

    subject = None
    verb = None
    obj = None

    for token in sentence:
        if token.dep_ == "nsubj":
            subject = token.text

            for child in token.lefts:
                if child.dep_ == "compound":
                    subject = child.text + " " + subject

        elif token.dep_ == "ROOT":
            verb = token.text

        elif token.dep_ in ("dobj", "obj"):
            obj = token.text
            for child in token.lefts:
                if child.dep_ == "compound":
                    subject = child.text + " " + subject
    
    print("Subject:", subject)
    print("Verb:", verb)
    print("Object:", obj)

    if subject and verb and obj:
        triple = (subject, verb, obj)
        print(triple)
        triples_list.append(triple)



print(triples_list)