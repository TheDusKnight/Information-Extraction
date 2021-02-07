import re


def syntactic_extractors():
    """
    Patterns for syntactic
    """
    # TODO: test
    birthplace_syntactic = [
        # {'IS_ALPHA': True, 'OP': '*'},
        # {'IS_PUNCT': True, 'OP': '?'},
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

    # parents_syntactic = [
    #     {'POS': 'VERB', 'ORTH': 'born'},
    #     {'OP': '*'},
    #     {'LOWER': 'to', 'POS': 'ADP'},
    #     {'POS': 'ADJ', 'OP': '*'},
    #     {'POS': 'NOUN', 'OP': '*'},
    #     {'IS_PUNCT': True, 'OP': '*'},
    #     {'ENT_TYPE': 'PERSON', 'OP': '+'},
    #     {'IS_PUNCT': True, 'OP': '*'},
    #     {'LOWER': 'and', 'POS': 'CCONJ', 'OP': '?'},
    #     {'POS': 'ADJ', 'OP': '*'},
    #     {'POS': 'NOUN', 'OP': '*'},
    #     {'IS_PUNCT': True, 'OP': '*'},
    #     {'ENT_TYPE': 'PERSON', 'OP': '+'},
    #     {'IS_PUNCT': True, 'OP': '*'},
    # ]

    parents_syntactic = [
        # {'ORTH': {'REGEX': '[f|F]ather|[m|M]other|[p|P]arent|[p|P]arents'}},
        # {'OP': '*'},
        # {'ENT_TYPE': 'PERSON', 'OP': '+'},
        # {'ORTH': 'and', 'POS': 'CCONJ', 'OP': '?'},


        # {'ORTH': {'REGEX': '[f|F]ather|[m|M]other|[p|P]arent|[p|P]arents'}},
        # {'OP': '*'},
        # {'IS_PUNCT': True, 'OP': '?'},
        # {'IS_STOP': True, 'OP': '?'},
        # {'ORTH': {'REGEX': '([A-Z][a-z]+)'}},
        # {'OP': '*'},
        # {'ORTH': 'and'},
        # {'IS_ALPHA': True, 'OP': '*'},  # TODO: remove *?
        # #  Last word before comma must be a capital word
        # {'ORTH': {'REGEX': '[,(]'}, 'OP': '*'},
        # {'ORTH': {'REGEX': '([A-Z][a-z]+)'}, 'OP': '*'},
        # {'ORTH': ')', 'OP': '*'},
        # {'ORTH': {'REGEX': '([A-Z][a-z]+)'}, 'OP': '+'},
        # {'ORTH': {'REGEX': '[.,]'}},


    ]

    awards_syntactic = [


    ]

    performances_syntactic = [

    ]

    colleagues_syntactic = [

    ]

    return birthplace_syntactic, (education_syntactic_1, education_syntactic_2), parents_syntactic, awards_syntactic, performances_syntactic, colleagues_syntactic


def syntactic_regs():
    """
    Regexes use to extract results from syntactic extractors
    """
    reg_birthplace_syntactic = re.compile(r'(?<= in ).*')
    reg_education_syntactic = re.compile(r'.*')
    reg_parents_syntactic = re.compile(r'.*')
    reg_awards_syntactic = re.compile(r'.*')
    reg_performances_syntactic = re.compile(r'.*')
    reg_colleagues_syntactic = re.compile(r".*")

    return reg_birthplace_syntactic, reg_education_syntactic, reg_parents_syntactic, reg_awards_syntactic, reg_performances_syntactic, reg_colleagues_syntactic