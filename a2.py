def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return dna1 > dna2


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    count = 0

    for nuc in dna:
        if nuc in nucleotide:
            count += 1
    return count


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return dna2 in dna1

def is_valid_sequence(dna):
    """ str -> bool
    Return True if and only if the DNA sequence is valid
    (that is, it contains no characters other than 
    'A', 'T', ’C’ and ’G’). 

    >>> is_valid_sequence('ATCCGG')
    True
    >>> is_valid_sequence('ATTcCGG')
    False
    """
    is_valid = True
    for seq in dna:
        if seq not in 'ATCG':
            is_valid = False
    return is_valid

def insert_sequence(dna1, dna2, ind):
    """ (str, str, int) -> str
    Return the DNA sequence obtained by inserting the second DNA sequence
    into the first DNA sequence at the given index.
    >>> insert_sequence("CCGG", "AT", 2)
    ’CCATGG’
    """
    new_dna = dna1[:ind] + dna2 + dna1[ind:]
    return new_dna

def get_complement(dna):
    """(str) -> str
    adenine and thymine, guanine and cytosine.
    In DNA, adenine correctly pairs with thymine and guanine correctly pairs
    with cytosine.

    'A' -> 'T'
    'T' -> 'A'
    'G' -> 'C'
    'C' -> 'G'

    >>> get_complement('A')
    'T'
    >>> get_complement('C')
    'G'
    >>> get_complement('a')
    False
    """

    if dna == 'A':
        return 'T'
    elif dna == 'T':
        return 'A'
    elif dna == 'G':
        return 'C'
    elif dna == 'C':
        return 'G'
    else:
        return False
    
    
def get_complementary_sequence(dna):
    """(str) -> str
    Return the DNA sequence that is complementary to the given DNA sequence
    >>> get_complementary_sequence('AT')
    'TA'
    >>> get_complementary_sequence('CG')
    'GC'
    """
    complement = ""
    for n in dna:
        complement = complement + get_complement(n)
    return complement
    
    
