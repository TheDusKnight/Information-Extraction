import sys
import test
from spacy import displacy
from Xirui_Zhong_hw02_task_2_2 import main


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('From main function\n')
    test.spacy_test()
    # test.spacy_syntacitc_test()
    # test.spacy_visual()

    # main(sys.argv[1:])

