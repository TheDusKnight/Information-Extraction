import re


def lexical_extractors():
    """
    Patterns for lexical
    """
    birthplace_lexical = [
        {'ORTH': 'born'},
        {'OP': '*'},
        {'ORTH': 'in'},
        {'ORTH': {'REGEX': '([A-Z][a-z]+)'}, 'OP': '+'},
        {'IS_PUNCT': True},
        {'ORTH': {'REGEX': '([A-Z][a-z]+)'}, 'OP': '+'},
        {'IS_PUNCT': True},
    ]

    # education_lexical = [
    #     {'ORTH': {'REGEX': "([A-Z][a-z']+)"}, 'OP': '*'},
    #     {'ORTH': {'REGEX': '(College|University|Institute|School|Academy)'}},
    #     {'ORTH': 'of', 'OP': '?'},
    #     {'ORTH': {'REGEX': '([A-Z][a-z]+)'}, 'OP': '*'},
    # ]
    education_lexical_1 = [
        # {'IS_STOP': False},
        {'ORTH': {'REGEX': "([A-Z][a-z']+)"}, 'OP': '+', 'IS_STOP': False},
        {'ORTH': {'REGEX': '(College|University|Institute|School|Academy)'}},
    ]
    education_lexical_2 = [
        {'ORTH': {'REGEX': '(College|University|Institute|School|Academy)'}},
        {'ORTH': 'of'},
        {'ORTH': {'REGEX': '([A-Z][a-z]+)'}, 'OP': '+', 'IS_STOP': False},
    ]

    # TODO: Parent有问题
    parents_lexical = [
        {'ORTH': {'REGEX': '[f|F]ather|[m|M]other|[p|P]arent|[p|P]arents'}},
        {'OP': '*'},
        {'IS_PUNCT': True, 'OP': '?'},
        {'IS_STOP': True, 'OP': '?'},
        {'ORTH': {'REGEX': '([A-Z][a-z]+)'}},
        {'OP': '*'},
        {'ORTH': 'and'},
        {'IS_ALPHA': True, 'OP': '*'},  # TODO: remove *?
        #  Last word before comma must be a capital word
        {'ORTH': {'REGEX': '[,(]'}, 'OP': '*'},
        {'ORTH': {'REGEX': '([A-Z][a-z]+)'}, 'OP': '*'},
        {'ORTH': ')', 'OP': '*'},
        {'ORTH': {'REGEX': '([A-Z][a-z]+)'}, 'OP': '+'},
        {'ORTH': {'REGEX': '[.,]'}},
    ]

    # awards_lexical = [
    #     {'ORTH': {'REGEX': '([A-Z][a-z]+)'}, 'OP': '+'},
    #     # # {'ORTH': {'REGEX': "([A-Z][a-z]+)"}, 'OP': '+', 'IS_STOP': False},
    #     {'ORTH': {'REGEX': 'Award|Awards'}},
    #     # {'IS_ALPHA': True, 'OP': '*'},
    #     {'ORTH': 'for', 'OP': '?'},
    #     {'ORTH': {'REGEX': '([A-Z][a-z]+)'}, 'OP': '*'},
    #     # {'ORTH': {'REGEX': '[.,]'}},
    #     # {'IS_ALPHA': True, 'OP': '*'},
    # ]

    awards_lexical_1 = [
        {'ORTH': {'REGEX': '([A-Z][a-z]+)'}, 'OP': '+'},
        {'ORTH': {'REGEX': 'Award|Awards'}},
    ]

    awards_lexical_2 = [
        {'ORTH': {'REGEX': '([A-Z][a-z]+)'}, 'OP': '+'},
        {'ORTH': {'REGEX': 'Award|Awards'}},
        {'ORTH': 'for'},
        {'ORTH': {'REGEX': '([A-Z][a-z]+)'}, 'OP': '+'},
    ]

    # performances_lexical = [
    #     {'ORTH': '"', 'OP': '?'},
    #     {'ORTH': {'REGEX': '([A-Z][a-z]+)'}, 'OP': '+'},
    #     # {'ORTH': {'REGEX': '([A-Z][a-z]+)'}},
    #     {'ORTH': {'REGEX': '["(]'}},
    #     # {'LIKE_NUM': True, 'OP': '?'},
    # ]

    performances_lexical = [
        {'ORTH': '"', 'OP': '?'},
        {'ORTH': {'REGEX': '([A-Z][a-z]+)'}, 'OP': '*'},
        {'ORTH': "'s", 'OP': '?'},
        {'ORTH': {'REGEX': '([A-Z][a-z]+)'}, 'OP': '+'},
        {'ORTH': "'s", 'OP': '?'},
        {'ORTH': '"', 'OP': '?'},
        {'ORTH': '('},
    ]

    colleagues_lexical_1 = [
        {'ORTH': '"', 'OP': '!'},
        {'ORTH': {'REGEX': '([A-Z][a-z]+)'}, 'OP': '+', 'IS_STOP': False},
        {'ORTH': "'s"},
        # {'ORTH': '(', 'OP': '!'}
    ]
    colleagues_lexical_2 = [
        {'ORTH': 'with'},
        {'ORTH': {'REGEX': '([A-Z][a-z]+)'}, 'OP': '+'},
    ]

    return birthplace_lexical, (education_lexical_1, education_lexical_2), parents_lexical, (
    awards_lexical_1, awards_lexical_2), performances_lexical, (
               colleagues_lexical_1, colleagues_lexical_2)


def lexical_regs():
    """
    Regexes use to extract results from lexical extractors
    """
    reg_birthplace_lexical = re.compile(r'(?<= in ).*?(?=\,$)')
    reg_education_lexical = re.compile(r'.*')
    # reg_parents_lexical = re.compile(r'([A-Z][a-z]+)( \(?[A-Z][a-z]+\)?)*(?=[,.]| [a-z])')
    # reg_parents_lexical = re.compile(r'([A-Z][a-z]+ )+')
    reg_parents_lexical = re.compile(r'([A-Z][()A-Za-z ]+)(?=[,.])')  # TODO: improve
    reg_awards_lexical = re.compile(r'.*')
    reg_performances_lexical = re.compile(r'.*')
    reg_colleagues_lexical = re.compile(r"([A-Z][()A-Za-z ]+)(?='s)")

    return reg_birthplace_lexical, reg_education_lexical, reg_parents_lexical, reg_awards_lexical, reg_performances_lexical, reg_colleagues_lexical

# tests = lexical_extractors()
# for test in tests:
#     if type(test) == tuple:
#         print(test[0], test[1])
