import re


def syntactic_extractors():
    """
    Patterns for syntactic
    """
    # TODO: test
    birthplace_syntactic = [
        {'ORTH': 'born'},
        {'OP': '*'},
        {'ORTH': 'in'},
        {'ENT_TYPE': 'GPE', 'OP': '+'},
        {'IS_PUNCT': True, 'OP': '?'},
        {'ENT_TYPE': 'GPE', 'OP': '*'},
        {'IS_PUNCT': True, 'OP': '?'},
        {'ENT_TYPE': 'GPE', 'OP': '*'},
        {'IS_PUNCT': False, 'IS_LOWER': False},
    ]

    education_syntactic_1 = [
        {'ENT_TYPE': 'GPE', 'OP': '*'},
        {'ENT_TYPE': 'ORG', 'OP': '*'},
        {'ORTH': {'REGEX': '(College|University|Institute|School|Academy)'}},
        {'IS_STOP': True},
        {'ENT_TYPE': 'ORG', 'OP': '+'},
    ]
    education_syntactic_2 = [
        {'ENT_TYPE': 'ORG', 'OP': '+'},
        {'ORTH': {'REGEX': '(College|University|Institute|School|Academy)'}},
        {'ENT_TYPE': 'ORG', 'OP': '*'},
        {'ENT_TYPE': 'GPE', 'OP': '*'},
    ]

    parents_syntactic = [  # TODO: Extract person name
        {'ORTH': {'REGEX': '[f|F]ather|[m|M]other|[p|P]arent|[p|P]arents'}},
        {'ORTH': {'REGEX': "[,()'\"]"}, 'OP': '?'},
        {'IS_ALPHA': True, 'OP': '*'},
        {'ORTH': {'REGEX': "[,()'\"]"}, 'OP': '?'},
        {'ENT_TYPE': 'PERSON', 'OP': '+'},
        {'ORTH': {'REGEX': "[,()'\"]"}, 'OP': '?'},
        {'ORTH': 'and', 'POS': 'CCONJ', 'OP': '?'},
        {'ORTH': {'REGEX': "[,()'\"]"}, 'OP': '?'},
        {'IS_ALPHA': True, 'OP': '*'},
        {'ORTH': {'REGEX': "[,()'\"]"}, 'OP': '?'},
        {'IS_ALPHA': True, 'OP': '*'},
        {'ORTH': {'REGEX': "[,()'\"]"}, 'OP': '?'},

        {'ENT_TYPE': 'PERSON', 'OP': '+'},
        {'ORTH': {'REGEX': "[,()'\"]"}, 'OP': '?'},
        {'ENT_TYPE': 'PERSON', 'OP': '*'},
        {'ORTH': {'REGEX': "[,()'\"]"}, 'OP': '?'},
        {'ENT_TYPE': 'PERSON', 'OP': '*'},
        {'ORTH': {'REGEX': "[,()'\"]"}, 'OP': '?'},
        {'ENT_TYPE': 'PERSON', 'OP': '*'},
    ]

    # Nothing need to change
    awards_syntactic_1 = [
        {'ORTH': {'REGEX': "[()'\"]"}, 'OP': '?'},
        {'POS': 'PROPN', 'OP': '+'},
        {'ORTH': {'REGEX': "[()'\"]"}, 'OP': '?'},
        {'ORTH': {'REGEX': 'Award|Awards'}},
        {'ORTH': {'REGEX': "[()'\"]"}, 'OP': '?'},
    ]

    awards_syntactic_2 = [
        {'ORTH': {'REGEX': "[()'\"]"}, 'OP': '?'},
        {'ORTH': {'REGEX': '([A-Z][a-z]+)'}, 'OP': '+'},
        {'ORTH': {'REGEX': "[()'\"]"}, 'OP': '?'},
        {'ORTH': {'REGEX': 'Award|Awards'}},
        {'ORTH': {'REGEX': "[()'\"]"}, 'OP': '?'},
        {'IS_STOP': True},
        {'ORTH': {'REGEX': "[()'\"]"}, 'OP': '?'},
        {'ORTH': {'REGEX': '([A-Z][a-z]+)'}, 'OP': '+'},
        {'ORTH': {'REGEX': "[()'\"]"}, 'OP': '?'},
    ]

    performances_syntactic = [
        {'ORTH': '"', 'OP': '?'},
        {'ORTH': {'REGEX': '([A-Z][a-z]+)'}, 'OP': '+'},
        # {'ORTH': "'s", 'OP': '?'},
        {'ORTH': {'REGEX': "'s|:"}, 'OP': '?'},
        {'IS_STOP': True, 'OP': '*'},
        {'ORTH': {'REGEX': '([A-Z][a-z]+)'}, 'OP': '*'},
        {'ORTH': "'s", 'OP': '?'},
        {'ORTH': '"', 'OP': '?'},
        {'ORTH': '('},
        {'LIKE_NUM': True},
    ]

    colleagues_syntactic_1 = [
        {'ORTH': '"', 'OP': '!'},
        {'ENT_TYPE': 'PERSON', 'OP': '+'},
        {'ORTH': "'s"},
    ]
    colleagues_syntactic_2 = [
        {'ORTH': 'with'},
        {'ENT_TYPE': 'PERSON', 'OP': '+'},
    ]

    return birthplace_syntactic, (education_syntactic_1, education_syntactic_2), parents_syntactic, (awards_syntactic_1, awards_syntactic_2), performances_syntactic, (colleagues_syntactic_1, colleagues_syntactic_2)


def syntactic_regs():
    """
    Regexes use to extract results from syntactic extractors
    """
    reg_birthplace_syntactic = re.compile(r'(?<= in ).*')
    reg_education_syntactic = re.compile(r'.*')
    reg_parents_syntactic = re.compile(r'.*')
    reg_awards_syntactic = re.compile(r'.*')
    reg_performances_syntactic = re.compile(r'.*(?=\d\d\d\d)')
    reg_colleagues_syntactic = re.compile(r"([A-Z][()A-Za-z ]+)(?='s)")

    return reg_birthplace_syntactic, reg_education_syntactic, reg_parents_syntactic, reg_awards_syntactic, reg_performances_syntactic, reg_colleagues_syntactic