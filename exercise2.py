

#Exercise 2.2
"""Looking at FASTA file and saving without spaces"""

#rstrip() function only strips last space/etc; so, want to load your FASTA sequence
#as individual lines, then do an iteration of rstrip on each individual line; index!

with open('salmonella_spi1_region.fna', 'r') as f:
    # Get all the lines in a list
    f_lines = f.readlines()

    # Make an empty string
    no_spaces = ""

    # Make a for loop to strip spaces but not first line thing
    for line in f_lines:
        # Strip the spaces of sequence lines and reiterate
        if line[0] in 'ATCG':
            #This next thing is same thing as no_spaces += line.rstrip()
            no_spaces = no_spaces + line.rstrip()


# Exercise 2.3a
def gc_blocks(seq, block_size):
"""
Divides a sequence into blocks and gives their GC content.
"""
    # Divide sequence into blocks based on block_size.

    #make an empty string for blocks
    block_list = ''
    for base in seq:
        i = 0
        block_list = block_list += seq[i: i+(block_size - 1)], i += blocksize
