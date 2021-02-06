from lexicals import lexical_regs, lexical_extractors
import spacy
from spacy.matcher import Matcher


def spacy_test():
    nlp = spacy.load("en_core_web_sm")
    matcher = Matcher(nlp.vocab)
    num = 2

    extractors = lexical_extractors()
    regex = lexical_regs()
    matcher.add("test", None, extractors[num])

    # doc = nlp("He's parents, Doge Fake Bob and John Doe Kobe. Smith and Gogo, will go home.")
    # doc = nlp("He was born Dominick DeLuise on August 1, 1933, in Brooklyn, New York,")
    doc = nlp("As they say, behind every clown's smile, one can find a few tears.He was born Dominick DeLuise on August 1, 1933, in Brooklyn, New York, to parents John, a sanitation engineer, and Vicenza (DeStefano) DeLuise, both Italian immigrants.")

    spans = [doc[start:end] for match_id, start, end in matcher(doc)]
    spans = spacy.util.filter_spans(spans)
    # print(spans)
    for span in spans:
        match = regex[num].findall(span.text)
        # match = span.text
        # match = list(map(str.strip, match))
        # print(match)
        print(match)

    # for match_id, start, end in matches:
    #     # string_id = nlp.vocab.strings[match_id]  # Get string representation
    #     span = doc[start:end]  # The matched span
    #
    #     print(match_id, string_id, start, end, span.text)
