

def reversed_complement(seq, material='DNA'):
    """compute reverse complement of DNA without using loops or reverse sequence funciton"""

    # make everything lowercase
    rev_comp = seq.lower()

    # in case of DNA
    if material == 'DNA':
        #replace with complement
        rev_comp = rev_comp.replace('a', 'T')
        rev_comp = rev_comp.replace('t', 'A')
        rev_comp = rev_comp.replace('g', 'C')
        rev_comp = rev_comp.replace('c', 'G')
        #reverse sequence and return
        return rev_comp [::-1]

    # in case of RNA
    elif material == 'RNA':
        rev_comp = rev_comp.replace('a', 'U')
        rev_comp = rev_comp.replace('u', 'A')
        rev_comp = rev_comp.replace('g', 'C')
        rev_comp = rev_comp.replace('c', 'G')
        #reverse the sequence and return
        return rev_comp [::-1]
