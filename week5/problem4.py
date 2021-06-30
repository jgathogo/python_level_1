import os
import sys
import random


def main():
    # Random sequence string of 100 base pairs
    residues = ['A', 'C', 'G', 'T']
    pairs = random.choices(residues, k=50)
    dna = ""
    for i in pairs:
        dna += i

    print(f"Original: {dna}")

    # Transcription of DNA sequence to corresponding RNA sequence
    trans_map = {'A': 'U',
                 'C': 'g_temp',
                 'G': 'C',
                 'T': 'A'}

    for d, r in trans_map.items():
        dna = dna.replace(d, r)
    rna = dna.replace('g_temp', 'G')
    print(f"Translated: {rna}")

    # Translation
    code = {'UUU': 'Phe', 'UUC': 'Phe', 'UUA': 'Leu', 'UUG': 'Leu', 'CUU': 'Leu', 'CUC': 'Leu', 'CUA': 'Leu',
            'CUG': 'Leu', 'AUU': 'Ile', 'AUC': 'Ile', 'AUA': 'Ile', 'AUG': 'Met', 'GUU': 'Val', 'GUC': 'Val',
            'GUA': 'Val', 'GUG': 'Val', 'UCU': 'Ser', 'UCC': 'Ser', 'UCA': 'Ser', 'UCG': 'Ser', 'CCU': 'Pro',
            'CCC': 'Pro', 'CCA': 'Pro', 'CCG': 'Pro', 'ACU': 'Thr', 'ACC': 'Thr', 'ACA': 'Thr', 'ACG': 'Thr',
            'GCU': 'Ala', 'GCC': 'Ala', 'GCA': 'Ala', 'GCG': 'Ala', 'UAU': 'Tyr', 'UAC': 'Tyr', 'UAA': 'Stop',
            'UAG': 'Stop', 'CAU': 'His', 'CAC': 'His', 'CAA': 'Gln',
            'CAG': 'Gln', 'AAU': 'Asn', 'AAC': 'Asn', 'AAA': 'Lys', 'AAG': 'Lys', 'GAU': 'Asp', 'GAC': 'Asp',
            'GAA': 'Glu', 'GAG': 'Glu', 'UGU': 'Cys', 'UGC': 'Cys', 'UGA': 'Stop', 'UGG': 'Trp', 'CGU': 'Arg',
            'CGC': 'Arg', 'CGA': 'Arg', 'CGG': 'Arg', 'AGU': 'Ser', 'AGC': 'Ser', 'AGA': 'Arg', 'AGG': 'Arg',
            'GGU': 'Gly', 'GGC': 'Gly', 'GGA': 'Gly', 'GGG': 'Gly',
            }

    trans_sequence = []
    stops = 0
    for i in range(len(rna)):
        codon = rna[i:i + 3]
        # print(codon)
        if len(codon) == 3:
            # print(code[codon])
            if code[codon] == 'Stop':
                stops += 1
                continue
            trans_sequence.append(code[codon])
    print(f"Number of codons: {len(trans_sequence)}")
    print(f"Number of Stops: {stops}")
    print(f"List of translations: {trans_sequence}")

    return os.EX_OK


if __name__ == '__main__':
    sys.exit(main())
