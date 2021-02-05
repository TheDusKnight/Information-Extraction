import spacy
import en_core_web_sm
import csv
from spacy.matcher import Matcher

''' Entity tag
geo = Geographical Entity
org = Organization
per = Person
gpe = Geopolitical Entity
tim = Time indicator
art = Artifact
eve = Event
nat = Natural Phenomenon
'''

''' regex look behind and lookup
(?<=BookTitle:).*?(?=\s)
BookTitle:HarryPotter JK Rowling
'''

nlp = en_core_web_sm.load()
lexical_matcher = Matcher(nlp.vocab)
syntactic_matcher = Matcher(nlp.vocab)

# pattern = [
#     {"IS_DIGIT": True},
#     {"LOWER": "fifa"},
#     {"LOWER": "world"},
#     {"LOWER": "cup"},BookTitle:HarryPotter JK Rowling
#     {"IS_PUNCT": True}
# ]

# pattern = [
#     {"LEMMA": "love", "POS": "VERB"},
#     {"POS": "NOUN"}
# ]

# test_pattern = [
#     # {'ORTH': {'REGEX': '(?<=/).*(?=/poo)'}},
#     # {'ORTH': {'REGEX': '.*(/poo)'}},
#     {'ORTH': {'REGEX': '.*(?=poo)'}}
# ]

birthplace_lexical = [
    {'ORTH': 'in'},
    # {'IS_STOP': False},
    # {'ORTH': {'REGEX': '(?<=in)'}},
    {'ORTH': {'REGEX': '[a-zA-Z]+'}},
    {'IS_PUNCT': True},
    {'ORTH': {'REGEX': '[a-zA-Z]+'}},
    {'IS_PUNCT': True},
    # {'OP': '+'},
    # {'LOWER': 'belgium'},
    # {'TEXT': {'REGEX': '(in) [a-zA-Z\s]+(\,)? [a-zA-Z]+(\,)?(\.)?'}},
    # {'ORTH': {'REGEX': '[a-zA-Z\s]+(\,)? [a-zA-Z]+(\,)?(\.)?'}},

]

education_lexical = [
    # {'IS_STOP': True},
    {'ORTH': {'REGEX': '([A-Z][a-z]+)'}, 'OP': '*'},
    # {'ORTH': {'REGEX': '([A-Z][a-z]+)', 'OP': '?'}},
    {'ORTH': {'REGEX': '(College|University|Institute|School|Academy)'}},
    {'ORTH': 'of', 'OP': '?'},
    # {'OP': '*'},
    # {'ORTH': 'Dramatic', 'OP': '?'},
    # {'ORTH': {'REGEX': '(^[A-Z][a-z]+$)', 'OP': '?'}},
    # {'ORTH': {'REGEX': '([A-Z][a-z]+)', 'OP': '*'}},
    {'ORTH': {'REGEX': '([A-Z][a-z]+)'}, 'OP': '*'},
    # {'ORTH': {'REGEX': '(College|University|Institute|Law School|School|School of|Academy of|University of)'}},


    # {'IS_SPACE': True},
    # {'ORTH': {'REGEX': '([A-Z][a-z]+ )*(College|University|Institute|Law School|School|School of|Academy of|University of)( [A-Z][a-z]+)*'}},
    # {'ORTH': {'REGEX': '([A-Z][^\s,.]+[.]?\s[(]?)*'}},
    # {'ORTH': {'REGEX': '(College|University|Institute|Law School|School of|Academy)[^,\d]*(?=,|\d)'}},
    # {'OP': '+'},
    # {'ORTH': {'REGEX': '^(Academy|academy|)$'}},
]

# parents_lexical = [
#     {'LOWER': 'born'},
#     {'OP': '*'},
#     {'LOWER': 'to'},
#     {'TEXT': {'REGEX': '\s*'}, 'OP': '*'},
#     {'IS_PUNCT': True, 'OP': '*'},
#     {'TEXT': {'REGEX': '\s*'}, 'OP': '+'},
#     {'IS_PUNCT': True, 'OP': '*'},
#     {'LOWER': 'and', 'OP': '?'},
#     {'TEXT': {'REGEX': '\s*'}, 'OP': '*'},
#     {'IS_PUNCT': True, 'OP': '*'},
#     {'TEXT': {'REGEX': '\s*'}, 'OP': '+'},
#     {'IS_PUNCT': True, 'OP': '*'},
# ]

# parents_lexical = [
#     {'ORTH': {'REGEX': 'father|mother|parent|parents'}},
#     # {'OP': '*'},
#     {'ORTH': {'REGEX': '([A-Z][a-z]+)'}},
#     {'ORTH': {'REGEX': '([A-Z][a-z]+)'}, 'OP': '?'},
#     {'ORTH': {'REGEX': '([A-Z][a-z]+)'}, 'OP': '?'},
#     {'IS_PUNCT': True},
#     {'TEXT': {'REGEX': '\w*'}, 'OP': '*'},
#
#
#     # {'OP': '*'},
#     {'IS_PUNCT': True},
#     # {'ORTH': 'and', 'OP': '?'},
#     {'ORTH': 'and'},
#     # {'OP': '*'},
#     # {'ORTH': {'REGEX': '([A-Z][a-z]+)'}},
#     # # {'ORTH': {'REGEX': '([A-Z][a-z]+)'}, 'OP': '?'},
#     # # {'ORTH': {'REGEX': '([A-Z][a-z]+)'}, 'OP': '?'},
#     # {'IS_PUNCT': True},
#
# ]

# TODO: 匹配直到找到标点, shortest one
parents_lexical = [
    {'ORTH': {'REGEX': '[f|F]ather|[m|M]other|[p|P]arent|[p|P]arents'}},
    # {'OP': '*'},
    {'IS_PUNCT': True, 'OP': '?'},
    {'IS_STOP': True, 'OP': '?'},
    {'ORTH': {'REGEX': '([A-Z][a-z]+)'}},
    {'OP': '*'},
    {'ORTH': 'and'},

    {'TEXT': {'REGEX': '\w*'}, 'OP': '*'},  # TODO: remove * or replace with {'IS_ALPHA': True, 'OP': '*'}, ?
    # Last word before comma must be a capital word
    {'ORTH': {'REGEX': '([A-Z][a-z]+)'}},
    {'ORTH': {'REGEX': '[.,]'}},
    # {'IS_PUNCT': True},
]

# TODO: 提取后去掉最后一个标点
awards_lexical = [
    # {'IS_STOP': True, 'OP': '?'},
    {'ORTH': {'REGEX': '([A-Z][a-z]+)'}},
    {'ORTH': {'REGEX': 'Award|Awards'}},
    # {'OP': '*'},
    {'IS_ALPHA': True, 'OP': '*'},
    # {'ORTH': {'REGEX': '([A-Za-z]+)', 'OP': '*'}},
    {'ORTH': 'for', 'OP': '?'},
    {'ORTH': {'REGEX': '([A-Z][a-z]+)'}},
    {'ORTH': {'REGEX': '[.,]'}},
]

# TODO: sort一下，找最长的带"的所有string，去掉标点
# TODO: 每个string记录倒数第二个token，查看是否和下一个string倒数第二个token一样，如果不是则保留，提取后去掉最后一个标点
performances_lexical = [
    {'ORTH': '"', 'OP': '?'},
    {'ORTH': {'REGEX': '([A-Z][a-z]+)'}, 'OP': '+'},
    # {'ORTH': {'REGEX': '([A-Z][a-z]+)'}},
    {'ORTH': {'REGEX': '["(]'}},
    # {'LIKE_NUM': True, 'OP': '?'},
]

colleagues_lexical = [
    {'ORTH': {'REGEX': '([A-Z][a-z]+)'}, 'OP': '+'},
    {'ORTH': "'s"},
]

birthplace_syntactic = [
    {'ORTH': 'in'},
    {'ENT_TYPE': 'GPE'},
]

education_syntactic = [

]

parents_syntactic = [

]

awards_syntactic = [

]

performances_syntactic = [

]

colleagues_syntactic = [

]

# pattern = [{'ENT_TYPE': 'GPE'}]

# lexical_matcher.add("BIRTHPLACE_LEXICAL", None, birthplace_lexical)
# lexical_matcher.add("PARENTS_LEXICAL", None, parents_lexical)
# lexical_matcher.add("EDUCATION_LEXICAL", None, education_lexical)
# lexical_matcher.add("AWARDS_LEXICAL", None, awards_lexical)
# lexical_matcher.add("PERFORMANCE_LEXICAL", None, performances_lexical)
lexical_matcher.add("COLLEAGUES_LEXICAL", None, colleagues_lexical)

syntactic_matcher.add("BIRTHPLACE_SYNTACTIC", None, birthplace_syntactic)

# doc = nlp("He was born Dominick DeLuise on August 1, 1933, in Brooklyn, New York, to parents John Smith, a sanitation "
#           "engineer, and her mom Vicenza (Cat) DeLuise Bob Go, both Italian immigrants. A natural class clown, it helped Dom "
#           "fit in at school, and he started drawing belly laughs fairly young on stage. His very first school play "
#           "had him portraying an inert copper penny! He later attended New York's High School of Performing Arts, "
#           "but when it came to college, he decided to major in biology at Tufts University near Boston. He never got "
#           "the idea of being a comedian out of his head, however, and the obsession eventually won out.")

# doc = nlp("Matthias Schoenaerts was born on December 8, 1977 in Antwerp, Belgium. His Mother, Dominique Wiche, "
#           "was a costume designer, translator and French teacher, and his father was actor Julien Schoenaerts.")

# doc = nlp("""Samuel Alexander Mendes was born on August 1, 1965 in Reading, England, UK to parents James Peter
# Mendes, a retired university lecturer, and Valerie Helene Mendes, an author who writes children's books. Their
# marriage didn't last long, James divorced Sam's mother in 1970 when Sam was just 5-years-old. Sam was educated at
# Cambridge University and joined the Chichester Festival Theatre following his graduation in 1987. Afterwards,
# he directed Judi Dench in "The Cherry Orchard", for which he won a Critics Circle Award for Best Newcomer. He then
# joined the Royal Shakespeare Company, where he directed such productions as "Troilus and Cressida" with Ralph Fiennes
# and "Richard III". In 1992, he became artistic director of the reopened Donmar Warehouse in London, where he directed
# such productions as "The Glass Menagerie" and the revival of the musical "Cabaret", which earned four Tony Awards
# including one for Best Revival of a Musical. He also directed "The Blue Room" starring Nicole Kidman. In 1999,
# he got the chance to direct his first feature film, American Beauty (1999). The movie earned 5 Academy Awards
# including Best Picture and Best Director for Mendes, which is a rare feat for a first-time film director.""")

# doc = nlp("""In 1992, he became artistic director of the reopened Donmar Warehouse in London, where he directed such productions as "The Glass Menagerie" and the revival of the musical "Cabaret", which earned four Tony Awards including one for Best Revival of a Musical. He also directed "The Blue Room" starring Nicole Kidman.""")

# doc = nlp("""He went on to make two more films that year, both of which were conveniently set in Minnesota, the acclaimed Beautiful Girls (1996) and Feeling Minnesota (1996).""")

# doc = nlp("""In 1999, he got the chance to direct his first feature film, American Beauty (1999). The movie earned 5 Academy Awards including Best Picture and Best Director for Mendes, which is a rare feat for a first-time film director.""")

doc = nlp("""With his role in Tom Barman's Any Way the Wind Blows (2003), he proved he was Flanders' young actor to watch. In 2004, Schoenaerts produced and starred in the short film A Message from Outer Space (2004).""")

# doc = nlp("His mother is English, and worked at British Midland, and his father was Irish (from County Kerry), "
#           "and worked on the railways for Bombardier.")

# doc = nlp("John Carroll Lynch was born August 1, 1963 in Boulder, Colorado, and was raised in Denver. He attended "
#           "Academy of Dramatic Show and Saint Benedict Catholic School last year.")
# Find all matches
# doc = nlp("/foo/boo/poo")
lexical_matches = lexical_matcher(doc)
syntactic_matches = syntactic_matcher(doc)

# Iterate over the matches
for match_id, start, end in lexical_matches:
    # Get the matched span
    # matched_span = doc[start+1:end-1] # TODO: birthplace add this
    matched_span = doc[start:end]

    # print(matched_span.text)
    print(matched_span.text)

# print("Lexical Matches:", [doc[start:end].text for match_id, start, end in lexical_matches])
# print("Syntactic Matches:", [doc[start:end].text for match_id, start, end in syntactic_matches])
