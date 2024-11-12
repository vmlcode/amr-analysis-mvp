from Bio import SeqIO
import numpy as np

def kmers(sequence):
  """
    Generate all k-mers of a specified length from a given sequence.

    A k-mer is a substring of length `k` extracted from the input sequence. 
    This function iterates through the sequence and returns a list of all possible 
    k-mers in the order they appear.

    Parameters
    ----------
    sequence : str
        The input sequence from which to extract k-mers.
    k : int
        The length of each k-mer to be generated.

    Returns
    -------
    list
        A list of k-mers (substrings) of length `k` extracted from `sequence`.

    Raises
    ------
    ValueError
        If `k` is greater than the length of `sequence` or if `k` is less than 1.

    Examples
    --------
    >>> kmers("ATCG", 2)
    ['AT', 'TC', 'CG']

    >>> kmers("ATCG", 3)
    ['ATC', 'TCG']
    """
  kmers = []
  for i in range(len(sequence) - 21 + 1):
    kmers.append(sequence[i:i + 21])
  return kmers

def one_hot_encode_kmer(kmer):
    one_hot_map = {'A': [1, 0, 0, 0], 'T': [0, 1, 0, 0], 'C': [0, 0, 1, 0], 'G': [0, 0, 0, 1]}
    return np.array([one_hot_map[base] for base in kmer]).flatten()

def extract_data_from_Fasta(file, path):
  read = SeqIO.read(path+file, format='fasta')
  return dict(name = read.name, description = read.description ,sequence = str(read.seq), size = len(read.seq))


