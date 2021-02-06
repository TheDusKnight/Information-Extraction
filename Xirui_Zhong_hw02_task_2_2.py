import spacy
import en_core_web_sm
import csv
import sys
import json
from spacy.matcher import Matcher
from lexicals import lexical_extractors, lexical_regs

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


def extractor_names():
    names = [
        "birthplace",
        "education",
        "parents",
        "awards",
        "performances",
        "colleagues",
    ]
    return names


def csv_extractor(in_csv):
    csv_rows = []
    with open(in_csv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for row in csv_reader:
            csv_rows.append((row[0], row[1]))

    return csv_rows


def json_exporter(out_dicts, out_jl):
    with open(out_jl, "w") as f:
        for out_dict in out_dicts:
            json.dump(out_dict, f)
            f.write('\n')  # TODO: remove last blank row
    # f.truncate()
    f.close()


def main(argv):
    in_csv = argv[0]
    out_jl = argv[1]
    mode = argv[2]  # 0 or 1

    nlp = en_core_web_sm.load()
    lexical_matcher = Matcher(nlp.vocab)
    syntactic_matcher = Matcher(nlp.vocab)

    names = extractor_names()
    csv_rows = csv_extractor(in_csv)
    out_put = []

    for (idx, (act, bio)) in enumerate(csv_rows):  # Find result in each bio
        # print(f'[{idx:2d}] >', act)
        out_dict = {"url": act}
        biog = bio
        doc = nlp(biog)

        # birthplace = None  # init result
        found_birthplace = False
        for idx, sent in enumerate(doc.sents):  # Split a bio to sentences
            # print(f'[{idx:2d}] >', sent)
            my_sent = str(sent)
            my_doc = nlp(my_sent)

            # for w in my_doc:
            #     print(f'{w.text:15s} [{w.tag_:5s} | {w.pos_:6s} | {spacy.explain(w.tag_)}]')
            # for w in doc:
            #     print(f'{w.text:15s} [{w.dep_}]')

            extractors = lexical_extractors()  # Get all extractors info
            regs = lexical_regs()
            for i in range(4):  # TODO: Change it back to 6
                extractor = extractors[i]
                regex = regs[i]

                if type(extractor) == tuple:  # When an extractor has more than one pattern
                    for j in range(len(extractor)):
                        lexical_matcher.add("LEXICAL_" + str(j), None, extractor[j])
                else:
                    lexical_matcher.add("LEXICAL", None, extractor)

                # lexical_matches = lexical_matcher(my_doc)
                spans = [my_doc[start:end] for match_id, start, end in lexical_matcher(my_doc)]
                spans = spacy.util.filter_spans(spans)
                # print(spans)

                if i == 0 and not found_birthplace:  # When extractor is birthplace
                    if spans:
                        match = spans[0].text
                        match = regex.findall(match)[0]
                        out_dict[names[i]] = match
                        found_birthplace = True
                        # break
                else:
                    if i == 2 and spans:
                        print("this is 2")
                    if spans:  # If a sentence is no empty, then it must contains results
                        matches = []
                        for span in spans:  # 一个句子中所有match的结果
                            tmp = span.text
                            match = regex.findall(tmp)  # TODO: Check correctness, extract mother and father?
                            for m in match:
                                matches.append(m)
                        out_dict.setdefault(names[i], []).extend(matches)

                # Remove current extractor
                if type(extractor) == tuple:
                    for j in range(len(extractor)):
                        lexical_matcher.remove("LEXICAL_" + str(j))
                else:
                    lexical_matcher.remove("LEXICAL")

        # Check if all keys exist
        for name in names:
            if name not in out_dict:
                if name == "birthplace":
                    out_dict[name] = ""
                else:
                    out_dict[name] = []

        # Add one bio result to output list
        out_put.append(out_dict)
        print(out_put)

        # birthplace = spans[0].text
        # regex = regs[i]
        # birthplace = regex.findall(birthplace)[0]
        # break

        # out_dict["birthplace"] = birthplace

        # try:
        #     # birthplace = next(s for s in spans if s)[0]
        #     if spans:
        #         birthplace = spans[0].text
        #         regex = re.compile(r'(?<= in ).*?(?=\,$)')  # 特殊匹配
        #         birthplace = regex.findall(birthplace)[0]
        # except IndexError:
        #     print("Cannot find any birthplace")
        #     # birthplace = None
        # except Exception as e:
        #     # print("Unknown error when extracting birthplace")
        #     logging.exception(e)
        #     # birthplace = None
        # finally:
        #     # out_dict["birthplace"] =
        #     print(birthplace)
        #
        #     lexical_matcher.remove("BIRTHPLACE_LEXICAL")

    # lexical_matcher.add("PARENTS_LEXICAL", None, parents_lexical)
    # lexical_matcher.add("EDUCATION_LEXICAL", None, education_lexical)
    # lexical_matcher.add("AWARDS_LEXICAL", None, awards_lexical)
    # lexical_matcher.add("PERFORMANCE_LEXICAL", None, performances_lexical)
    # lexical_matcher.add("COLLEAGUES_LEXICAL", None, colleagues_lexical_1)
    # lexical_matcher.add("COLLEAGUES_LEXICAL", None, colleagues_lexical_2)

    # doc = nlp("/foo/boo/poo")
    # lexical_matches = lexical_matcher(doc)
    # syntactic_matches = syntactic_matcher(doc)

    # spans = [doc[start:end] for match_id, start, end in lexical_matches]
    # print(spans)
    # # Only keep longest match pattern
    # print(spacy.util.filter_spans(spans))


if __name__ == "__main__":
    main(sys.argv[1:])
