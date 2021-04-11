# Basic script to find primer candidates
# Hits are 20bp in length, with 50-55% GC content, GC clamps in the 3' end, and no more than 3xGC at the clamp
from math import (floor, ceil)


# Function that receives a gene string (only C, G, T or A characters) and outputs an array of primer hits
# Looks for a GC clamp reading from start to end of the string
def find_hit_in_sequence(gene, gc_target, length):
    hits = []
    for i in range(len(gene) - length):
        if gene[i] == 'C' or gene[i] == 'G':
            if gene[i + 1] == 'C' or gene[i + 1] == 'G':
                if gene[i + 2] != 'C' and gene[i + 2] != 'G':
                    gc_count = 0
                    for base in gene[i:i + length]:
                        if base == 'C' or base == 'G':
                            gc_count += 1

                    # approximate the requested GC%
                    if gc_count == ceil(gc_target*length/100) or gc_count == ceil(gc_target*length/100)-1:
                        hits.append(gene[i:i + length])
    return hits


def hits_from_exons(exon1, exon2, gc_content, primer_length):
    # Remove white spaces or irrelevant characters
    exon1 = "".join(exon1.split())
    exon2 = "".join(exon1.split())

    # Reverse exon 1 as GC clamp should be at the end of the primer
    exon1 = exon1[::-1]
    hits_exon1 = []
    for elem in find_hit_in_sequence(exon1, gc_content, primer_length):
        hits_exon1.append(elem[::-1])

    # Find hits for exon 2
    hits_exon2 = find_hit_in_sequence(exon2, gc_content, primer_length)

    return {
        "forward": hits_exon1,
        "reverse": hits_exon2,
    }
