import spacy
import en_core_web_sm
import csv
import sys
import json
import re
from spacy.matcher import Matcher
from lexicals import lexical_extractors, lexical_regs
from syntactics import syntactic_extractors, syntactic_regs

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


def json_exporter(out_puts, out_jl):
    with open(out_jl, "w") as f:
        for out_put in out_puts:
            json.dump(out_put, f)
            f.write('\n')  # TODO: remove last blank row
    # f.truncate()
    f.close()


def main(argv):
    in_csv = argv[0]
    out_jl = argv[1]
    mode = int(argv[2])  # 0 or 1
    print("Current mode is " + str(mode))

    nlp = en_core_web_sm.load()
    my_matcher = Matcher(nlp.vocab)
    # syntactic_matcher = Matcher(nlp.vocab)

    names = extractor_names()
    csv_rows = csv_extractor(in_csv)
    out_puts = []

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
            # for w in my_doc:
            #     print(f'{w.text:15s} [{w.dep_}]')

            # Get all extractors info based on mode
            if mode == 0:
                extractors = lexical_extractors()
                regs = lexical_regs()
            else:
                extractors = syntactic_extractors()
                regs = syntactic_regs()

            # Extract sentence based on 6 extractors
            for i in range(6):
                extractor = extractors[i]
                regex = regs[i]

                if type(extractor) == tuple:  # When an extractor has more than one pattern
                    for j in range(len(extractor)):
                        my_matcher.add("LEXICAL_" + str(j), None, extractor[j])
                else:
                    my_matcher.add("LEXICAL", None, extractor)

                # lexical_matches = my_matcher(my_doc)
                spans = [my_doc[start:end] for match_id, start, end in my_matcher(my_doc)]
                spans = spacy.util.filter_spans(spans)
                # print(spans)

                if i == 0:  # When extractor is birthplace
                    if spans and not found_birthplace:
                        match = spans[0].text
                        match = regex.findall(match)
                        if match:
                            match = match[0]
                        else:
                            match = ""
                        out_dict[names[i]] = match
                        found_birthplace = True
                        # break
                else:
                    # if i == 2 and spans:
                        # print('sent is ' + my_sent)
                    if spans:  # If a sentence is no empty, then it must contains results
                        matches = []
                        for span in spans:  # 一个句子中所有match的结果
                            tmp = span.text
                            match = regex.findall(tmp)  # TODO: Check correctness, extract mother and father?
                            for m in match:
                                if not m:
                                    pass
                                    # print("match is empty")
                                else:
                                    # matches.append(m)
                                    m = re.sub("[^A-Za-z0-9']+", ' ', m)  # TODO: 是否应该去掉所有标点？
                                    matches.append(m.strip())
                        # out_dict.setdefault(names[i], []).extend(matches)
                        try:  # Use set() to remove duplicates
                            out_dict.setdefault(names[i], set()).update(matches)
                        except AttributeError:
                            print(type(matches))
                            out_dict[names[i]] = set()

                # Remove current extractor
                if type(extractor) == tuple:
                    for j in range(len(extractor)):
                        my_matcher.remove("LEXICAL_" + str(j))
                else:
                    my_matcher.remove("LEXICAL")

        # Check if all keys exist, change set back to list
        for name in names:
            if name not in out_dict:
                if name == "birthplace":
                    out_dict[name] = ""
                else:
                    out_dict[name] = []
            elif name != "birthplace":
                out_dict[name] = list(out_dict[name])
            else:
                # print(out_dict[name])
                pass

        # Add each bio result to output list
        out_puts.append(out_dict)
        print(out_dict)
        # try:
        #     json.dumps(out_dict)
        #     out_puts.append(out_dict)
        # except TypeError:
        #     print("Json dumps failed")
        #     print(out_dict)

    # Write output to file
    json_exporter(out_puts, out_jl)
    print('Write success')


if __name__ == "__main__":
    main(sys.argv[1:])
