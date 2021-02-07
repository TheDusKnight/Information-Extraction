import re


def lexical_extractors():
    """
    Patterns for lexical
    """
    birthplace_lexical = [
        # {'ORTH': 'born'},
        # {'OP': '*'},
        # {'ORTH': 'in'},
        # {'ORTH': {'REGEX': '([A-Z][a-z]+)'}, 'OP': '+'},
        # {'IS_PUNCT': True},
        # {'ORTH': {'REGEX': '([A-Z][a-z]+)'}, 'OP': '+'},
        # {'IS_PUNCT': True},

        # TODO: Test if better
        {'ORTH': 'born'},
        {'OP': '*'},
        {'ORTH': 'in'},
        {'ORTH': {'REGEX': '([A-Z][A-Za-z]+)'}, 'OP': '+'},
        {'IS_PUNCT': True, 'OP': '?'},
        {'ORTH': {'REGEX': '([A-Z][A-Za-z]+)'}, 'OP': '*'},
        {'IS_PUNCT': True, 'OP': '?'},
        {'ORTH': {'REGEX': '([A-Z][A-Za-z]+)'}, 'OP': '*'},
        {'IS_PUNCT': False, 'IS_LOWER': False},
    ]

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

    parents_lexical = [
        {'ORTH': {'REGEX': '[f|F]ather|[m|M]other|[p|P]arent|[p|P]arents'}},
        {'IS_ALPHA': True, 'OP': '*'},
        {'ORTH': {'REGEX': "[,()'\"]"}, 'OP': '?'},
        {'IS_ALPHA': True, 'OP': '*'},
        {'ORTH': {'REGEX': "[,()'\"]"}, 'OP': '?'},
        {'ORTH': 'and'},
        {'ORTH': {'REGEX': "[,()'\"]"}, 'OP': '?'},
        {'IS_ALPHA': True, 'OP': '*'},
        {'ORTH': {'REGEX': "[,()'\"]"}, 'OP': '?'},
        {'IS_ALPHA': True, 'OP': '*'},
        {'ORTH': {'REGEX': "[,()'\"]"}, 'OP': '?'},
        {'IS_ALPHA': True, 'OP': '*'},

        {'ORTH': {'REGEX': '([A-Z][A-Za-z]+)'}, 'OP': '+', 'IS_STOP': False},  # TODO: Check correctness
        {'ORTH': {'REGEX': "[,()'\"]"}, 'OP': '?'},
        {'IS_ALPHA': True, 'OP': '*'},
        {'ORTH': {'REGEX': "[,()'\"]"}, 'OP': '?'},
        {'IS_ALPHA': True, 'OP': '*'},
        {'ORTH': {'REGEX': "[,()'\"]"}, 'OP': '?'},
        {'IS_ALPHA': True, 'OP': '*'},
        {'ORTH': '.'},
    ]

    awards_lexical_1 = [
        {'ORTH': {'REGEX': '([A-Z][a-z]+)'}, 'OP': '+'},
        {'ORTH': {'REGEX': 'Award|Awards'}},
    ]
    awards_lexical_2 = [
        {'ORTH': {'REGEX': '([A-Z][a-z]+)'}, 'OP': '+'},
        {'ORTH': {'REGEX': 'Award|Awards'}},
        {'ORTH': 'for'},  # TODO: change to stop
        {'ORTH': {'REGEX': '([A-Z][a-z]+)'}, 'OP': '+'},
    ]

    performances_lexical = [
        {'ORTH': '"', 'OP': '?'},
        {'ORTH': {'REGEX': '([A-Z][a-z]+)'}, 'OP': '*'},
        {'ORTH': "'s", 'OP': '?'},
        {'ORTH': {'REGEX': '([A-Z][a-z]+)'}, 'OP': '+'},
        {'ORTH': "'s", 'OP': '?'},
        {'ORTH': '"', 'OP': '?'},
        {'ORTH': '('},
        {'LIKE_NUM': True},
    ]

    colleagues_lexical_1 = [
        {'ORTH': '"', 'OP': '!'},
        {'ORTH': {'REGEX': '([A-Z][a-z]+)'}, 'OP': '+', 'IS_STOP': False},
        {'ORTH': "'s"},
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
    # reg_birthplace_lexical = re.compile(r'(?<= in ).*?(?=,$)')
    reg_birthplace_lexical = re.compile(r'(?<= in ).*')
    # reg_birthplace_lexical = re.compile(r'.*')

    reg_education_lexical = re.compile(r'.*')

    # reg_parents_lexical = re.compile(r'([A-Z][a-z]+)( \(?[A-Z][a-z]+\)?)*(?=[,.]| [a-z])')
    # reg_parents_lexical = re.compile(r'([A-Z][a-z]+ )+')
    # reg_parents_lexical = re.compile(r'.*')
    reg_parents_lexical = re.compile(r'([A-Z][()A-Za-z ]+)(?=[,.])')  # TODO: improve

    reg_awards_lexical = re.compile(r'.*')
    reg_performances_lexical = re.compile(r'.*(?=\d\d\d\d)')
    reg_colleagues_lexical = re.compile(r"([A-Z][()A-Za-z ]+)(?='s)")

    return reg_birthplace_lexical, reg_education_lexical, reg_parents_lexical, reg_awards_lexical, reg_performances_lexical, reg_colleagues_lexical
