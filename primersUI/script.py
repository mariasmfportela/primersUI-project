# Basic script to find primer candidates
# Hits are 20bp in length, with 50-55% GC content, GC clamps in the 3' end, and no more than 3xGC at the clamp

# Function that receives a gene string (only C, G, T or A characters) and outputs an array of primer hits
# Looks for a GC clamp reading from start to end of the string
def find_hit_in_sequence(gene):
    hits = []
    for i in range(len(gene) - 20):
        if gene[i] == 'C' or gene[i] == 'G':
            if gene[i + 1] == 'C' or gene[i + 1] == 'G':
                if gene[i + 2] != 'C' and gene[i + 2] != 'G':
                    cg_count = 0
                    for base in gene[i:i + 20]:
                        if base == 'C' or base == 'G':
                            cg_count += 1

                    if cg_count == 10 or cg_count == 11:
                        hits.append(gene[i:i + 20])
    return hits


def hits_from_exons(exon1, exon2):
    # Reverse exon 1 as GC clamp should be at the end of the primer
    exon1 = exon1[::-1]
    hits_exon1 = []
    for elem in find_hit_in_sequence(exon1):
        hits_exon1.append(elem[::-1])

    hits_exon2 = find_hit_in_sequence(exon2)

    return {
        "forward": hits_exon1,
        "reverse": hits_exon2,
    }
