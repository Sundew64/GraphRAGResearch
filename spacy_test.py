import spacy

triples_list = []
sentence_triples_list = []

"""
SPACY DEPENDENCY LABELS:
ROOT     -- main verb
nsubj    -- subject performing the action
nsubjpass -- passive subject
dobj/obj -- direct object
compound -- part of a multi-word noun
amod     -- adjective modifier
prep     -- preposition
pobj     -- object of a preposition
conj     -- word/verb joined to another word/verb
relcl    -- relative clause
"""

nlp = spacy.load("en_core_web_sm")

"""
              Wikipedia text
                    ↓
              clean citations
                    ↓
                  spaCy
                    ↓
             dependency tree
                    ↓
          ┌─────────┴─────────┐
          ↓                   ↓
     get_verbs()         noun phrase
          ↓              get_phrase()
          ↓
   ┌──────┴───────┐
   ↓              ↓
get_subjects()  get_objects()
   ↓              ↓
   └──────┬───────┘
          ↓
       triples
"""


def get_phrase(token):
    phrase = [token]

    for child in token.children:
        if child.dep_ in ("det", "amod", "compound", "poss", "nummod"):
            phrase.append(child)

    phrase = sorted(phrase, key=lambda x: x.i)

    return " ".join(word.text for word in phrase)


def get_verbs(sentence):
    verbs = []

    for token in sentence:
        if token.pos_ == "VERB":
            if token.dep_ in ("ROOT", "conj", "relcl"):
                verbs.append(token)

    return verbs


def get_subjects(verb):
    subjects = []

    # Find explicit subjects
    for child in verb.children:
        if child.dep_ in ("nsubj", "nsubjpass"):
            subjects.append(child)

            # Find subjects joined with "and"
            for conjunct in child.conjuncts:
                subjects.append(conjunct)

    # A conjoined verb can inherit its parent's subject
    if not subjects and verb.dep_ == "conj":
        subjects = get_subjects(verb.head)

    # A relative-clause verb can inherit its governing noun
    if not subjects and verb.dep_ == "relcl":
        subjects.append(verb.head)

    return subjects

def get_objects(verb):
    objects = []

    for child in verb.children:

        # Direct objects
        if child.dep_ in ("obj", "dobj"):
            objects.append(child)

            # Objects joined with "and"
            for conjunct in child.conjuncts:
                objects.append(conjunct)

    return objects

for pg in range(1, 11):

    filepath = fr"C:\Users\ihita\OneDrive - Lake Washington School District\_2025-2026\Other\Research\PDFs\{pg}.1.txt"

    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    paragraphs = text.split("\n\n")

    for para, paragraph in enumerate(paragraphs, start=1):

        doc = nlp(paragraph)

        for sent, sentence in enumerate(doc.sents, start=1):

            verbs = get_verbs(sentence)

            for verb in verbs:
                subjects = get_subjects(verb)
                objects = get_objects(verb)

                for subject in subjects:
                    for obj in objects:

                        triple = (
                            get_phrase(subject),
                            verb.lemma_,
                            get_phrase(obj)
                        )
                        triples_list.append(triple)

                        triple = (
                            pg,
                            para,
                            sent,
                            get_phrase(subject),
                            verb.lemma_,
                            get_phrase(obj)
                            )

                        sentence_triples_list.append(triple)

#for triple in sentence_triples_list:
    #print(triple)