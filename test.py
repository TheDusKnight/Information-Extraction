from lexicals import lexical_regs, lexical_extractors
from syntactics import syntactic_extractors, syntactic_regs
import spacy
import re
from spacy.matcher import Matcher
from spacy import displacy
options = {"distance": 120}


def spacy_test():
    nlp = spacy.load("en_core_web_sm")
    matcher = Matcher(nlp.vocab)
    num = 3

    extractors = syntactic_extractors()
    regex = syntactic_regs()
    # extractors = lexical_extractors()
    # regex = lexical_regs()
    matcher.add("test", None, extractors[num])

    # doc = nlp("He's parents, Doge Fake Bob and John Doe Kobe. Smith and Gogo, will go home.")
    # doc = nlp("He was born Dominick DeLuise on August 1, 1933, in Brooklyn, New York,")
    # doc = nlp("As they say, behind every clown's smile, one can find a few tears.He was born Dominick DeLuise on August 1, 1933, in Brooklyn, New York, to parents John, a sanitation engineer, and Vicenza (DeStefano) DeLuise, both Italian immigrants.")
    # doc = nlp("""In addition to his film and tel. Academy Award for Best Foreign Language Fileevision work, Kiser has acted on stage in the Broadway plays "God's Favorite" (Terry received a Tony Award nomination for his performance in this Neil Simon comedy), "Shelter", "The Castro Complex", and "Paris Is Out!". Terry won both an Obie and a Theater World Award for his exemplary acting in the dramatic play "Fortune and Men's Eyes".""")
    doc = nlp("Terry received a Tony Award nomination for his performance in this Neil Simon comedy), Terry won both an Obie and a Theater World Award for his exemplary acting.")
    # doc = nlp("Samuel Alexander Mendes was born on August 1, 1965 in Reading, England, UK to his parents James Peter Mendes, a retired University lecturer, and Valerie (Helene) Mendes, an author who writes children's books.")


    spans = [doc[start:end] for match_id, start, end in matcher(doc)]
    spans = spacy.util.filter_spans(spans)
    # print(spans)
    for span in spans:
        print(span)
        r = regex[num]
        # r = re.compile(r'(?<= in ).*')
        match = r.findall(span.text)
        # match = span.text
        print(match)

    # for match_id, start, end in matches:
    #     # string_id = nlp.vocab.strings[match_id]  # Get string representation
    #     span = doc[start:end]  # The matched span
    #
    #     print(match_id, string_id, start, end, span.text)


def spacy_syntacitc_test():
    nlp = spacy.load("en_core_web_sm")
    mysent = """Samuel Alexander Mendes was born Vicenza (DeStefano) DeLuise on August 1, 1965 in Reading, England, UK to parents Lengend On The Moon, James Peter Mendes, a retired university lecturer Game of Thrones (2011) Tony Award from University of Southern California, and Valerie (Helene) Mendes, an author. He later attended New York's High School of Performing Arts who writes children's books."""
    matcher = Matcher(nlp.vocab)
    doc = nlp(mysent)
    for w in doc:
        print(f'{w.text:12s} [{w.lemma_:10s} | {w.tag_:5s} | {w.pos_:6s} | {w.dep_:9s} | {spacy.explain(w.tag_)}]')
    for ent in doc.ents:
        # print(type(str(ent)))
        print(ent, ent.label_)
        # print(f'{ent:15s} [{ent.label_:10s}]')
