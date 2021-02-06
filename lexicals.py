import re


def lexical_extractors():
    """
    Patterns for lexical
    """
    # matched_span = doc[start+1:end-1] # TODO: birthplace add this
    birthplace_lexical = [
        {'ORTH': 'born'},
        {'OP': '*'},
        {'ORTH': 'in'},
        {'ORTH': {'REGEX': '([A-Z][a-z]+)'}, 'OP': '+'},
        {'IS_PUNCT': True},
        {'ORTH': {'REGEX': '([A-Z][a-z]+)'}, 'OP': '+'},
        {'IS_PUNCT': True},
    ]

    education_lexical = [
        # {'IS_STOP': True},
        {'ORTH': {'REGEX': "([A-Z][a-z']+)"}, 'OP': '*'},
        # {'ORTH': "'s", 'OP': '?'},
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

    # TODO: sort, match longest one, remove "'s"
    # TODO: 如果一句话有多个同事怎么办？
    # TODO: 考虑前缀是'"'或后缀是'（'的情况. Sort, 如果前缀有'"'或后缀有'（'则不保留
    colleagues_lexical_1 = [
        # {'ORTH': '"', 'OP': '?'},
        {'ORTH': {'REGEX': '([A-Z][a-z]+)'}, 'OP': '+'},
        {'ORTH': "'s"},
        # {'ORTH': '(', 'OP': '!'}
    ]
    # TODO: 去掉第一个token
    colleagues_lexical_2 = [
        {'ORTH': 'with'},
        {'ORTH': {'REGEX': '([A-Z][a-z]+)'}, 'OP': '+'},
    ]

    return birthplace_lexical, education_lexical, parents_lexical, awards_lexical, performances_lexical, (colleagues_lexical_1, colleagues_lexical_2)


def lexical_regs():
    """
    Regexes use to extract results from lexical extractors
    """
    reg_birthplace_lexical = re.compile(r'(?<= in ).*?(?=\,$)')
    reg_education_lexical = re.compile(r'.*')
    # reg_parents_lexical = re.compile(r'([A-Z][a-z]+)( \(?[A-Z][a-z]+\)?)*(?=[,.]| [a-z])')
    # reg_parents_lexical = re.compile(r'([A-Z][()A-Za-z ]+)(?=[,.])')  # TODO: improve
    reg_parents_lexical = re.compile(r'.*')
    reg_awards_lexical = re.compile(r'.*')
    reg_performances_lexical = re.compile(r'.*')
    reg_colleagues_lexical = re.compile(r'.*')

    return reg_birthplace_lexical, reg_education_lexical, reg_parents_lexical, reg_awards_lexical, reg_performances_lexical, reg_colleagues_lexical


# tests = lexical_extractors()
# for test in tests:
#     if type(test) == tuple:
#         print(test[0], test[1])
