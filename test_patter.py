import spacy
import re

nlp = spacy.load("en_core_web_sm")
# doc = nlp("The United States of America (USA) are commonly known as the United States (U.S. or US) or America.")
doc = nlp("/foo/boo/poo")
# expression = r"[Uu](nited|\.?) ?[Ss](tates|\.?)"
expression = r"(?<=/).*(?=/poo)"
# expression = r"(poo)"

for match in re.finditer(expression, doc.text):
    start, end = match.span()
    span = doc.char_span(start, end)
    # This is a Span object or None if match doesn't map to valid token sequence
    if span is not None:
        print("Found match:", span.text)
