import spacy

triples_list = []
sentence_triples_list = []

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

for pg in range(1, 11):
    filepath = fr"C:\Users\ihita\OneDrive - Lake Washington School District\_2025-2026\Other\Research\PDFs\{pg}.1.txt"

    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    doc = nlp(text)

    paragraphs = text.split("\n\n")

    for para, paragraph in enumerate(paragraphs, start=1):
        doc = nlp(paragraph)

        for sent, sentence in enumerate(doc.sents, start=1):

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
                            obj = child.text + " " + obj

            if subject and verb and obj:
                triple = (
                    pg,
                    para,
                    sent,
                    subject,
                    verb,
                    obj
                )
                sentence_triples_list.append(triple)


print(sentence_triples_list)