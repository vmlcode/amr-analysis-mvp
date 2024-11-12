import os
import numpy as np
import pandas as pd
from utils import extract_data_from_Fasta, kmers, one_hot_encode_kmer

genomic_filepath = './data/genomic/'
amr_filepath = './data/amr/'

genomic_files = os.listdir(genomic_filepath)
amr_files = os.listdir(amr_filepath)

# create dataframes
wgs_files = pd.DataFrame([extract_data_from_Fasta(file, genomic_filepath) for file in genomic_files])
# amr_files = pd.DataFrame([extract_data_from_Fasta(file, amr_filepath) for file in amr_files])


wgs_files['kmers'] = wgs_files['sequence'].apply(kmers)
# amr_files['kmers'] = amr_files['sequence'].apply(kmers)

wgs_files['encoded_kmers'] = wgs_files['kmers'].apply(lambda kmers: [one_hot_encode_kmer(kmer) for kmer in kmers])
# amr_files['encoded_kmers'] = amr_files['kmers'].apply(lambda kmers: [one_hot_encode_kmer(kmer) for kmer in kmers])
print(wgs_files[['size', 'kmers', 'encoded_kmers']])

# wgs_files.to_hdf('data.h5', key='df', mode='w')
# wgs_files.to_csv('data.csv')