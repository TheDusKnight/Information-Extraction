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
    # doc = nlp("As they say, behind every clown's smile, one can find a few tears.He was born Dominick DeLuise on August 1, 1933, in Brooklyn, New York, to parents John, a sanitation engineer, and Vicenza (DeStefano) DeLuise, both Italian immigrants.")
    # doc = nlp("""In addition to his film and tel. Academy Award for Best Foreign Language Fileevision work, Kiser has acted on stage in the Broadway plays "God's Favorite" (Terry received a Tony Award nomination for his performance in this Neil Simon comedy), "Shelter", "The Castro Complex", and "Paris Is Out!". Terry won both an Obie and a Theater World Award for his exemplary acting in the dramatic play "Fortune and Men's Eyes".""")
    # doc = nlp("Terry received a Tony Award nomination for his performance in this Neil Simon comedy), Terry won both an Obie and a Theater World Award for his exemplary acting.")
    doc = nlp("Samuel Alexander Mendes was born on August 1, 1965 in Reading, England, UK to parents James Peter Mendes, a retired university lecturer, and Valerie Helene Mendes, an author who writes children's books.")

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
