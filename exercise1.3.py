
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

def reversed_complement(seq, material='DNA'):
    """compute reverse complement of DNA without using reversed sequence"""

    #initialize an empty string
    rev_comp = ''

    #find complement
    for base in seq:
        rev_comp += complement_base(base, material=material)
    #reverse sequence and return
    return rev_comp [::-1]
