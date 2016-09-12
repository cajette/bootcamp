#call signature matches what you define in define clause aka parentheses
    #next is a string; documentation string, every function should have a doc string because it tells you what your function is doing
    #next is the output of a function

def ratio(x, y):
    """The ratio of 'x' to 'y'."""
    return x / y
#then once you run it, go ratio(#, #)

def complement_base(base, material='DNA'):

    """Return the Watson-Crick complement of a base"""
#note that a return statement shuts program down after result! This program couldn't do a sequence

    if base in 'Aa':
        if material == 'DNA':
            return 'T'
        elif material == 'RNA':
            return 'U'
        else: raise RuntimeError('Invalid Material.')
    elif base in 'TtUu':
        return 'A'
    elif base in 'Gg':
        return 'C'
    else:
        return 'G'


def reverse_complement(seq, material='DNA'):
    """Compute reverse complement of a DNA sequence."""

    # Initialize an empty string
    rev_comp = ''

    # loop through and add new rev comp bases
    for base in reversed(seq):
        rev_comp += complement_base(base, material=material)
    return rev_comp


def answer_to_the_ultimate_question_of_life_the_universe_and_everything():
    """simpler program that Deep Throught's, I bet"""
    return 42

def think_too_much():
    """Express Caesar's skepticism about Cassius"""

    print("""Yond Cassius has a lean and hungry look,
        He thinks too much; such men are dangerous""")
