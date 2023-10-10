#!/usr/bin/env python

import sys

from model_peaks import load_bedgraph, bin_array
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt


def main():
    # Load file names and fragment width
    forward_fname, reverse_fname, out_fname, frag_width, fwd_control, rev_control = sys.argv[1:]


    # Define what genomic region we want to analyze
    chrom = "chr2R"
    chromstart = 10000000
    chromend =  12000000
    chromlen = chromend - chromstart
    frag_width = int(frag_width)
    # Load the sample bedgraph data, reusing the function we already wrote

    forward = load_bedgraph(forward_fname, chrom, chromstart, chromend)
    reverse = load_bedgraph(reverse_fname, chrom, chromstart, chromend)
    print()
    # Combine tag densities, shifting by our previously found fragment width
    
    combined = np.zeros(chromlen)
    combined[frag_width//2:] += forward[frag_width//2:]  
    combined[:-frag_width//2] += reverse[:-frag_width//2]
    #print(sum(combined))


    # Load the control bedgraph data, reusing the function we already wrote
    
    cont_f = load_bedgraph(fwd_control, chrom, chromstart, chromend)
    cont_r = load_bedgraph(rev_control, chrom, chromstart, chromend)

    # Combine tag densities

    control_combined = cont_f + cont_r
    #print(sum(control_combined))
    # Adjust the control to have the same coverage as our sample

    control_combined = control_combined * (sum(combined)/sum(control_combined))
    #combined = combined * (sum(combined)/sum(control_combined))
    #print(sum(control_combined))

    # Create a background mean using our previous binning function and a 1K window
    # Make sure to adjust to be the mean expected per base

    background = bin_array(control_combined, 1000)/1000


    # Find the mean tags/bp and make each background position the higher of the
    # the binned score and global background score

    mod_control = np.maximum(background, np.mean(control_combined))
    
    # Score the sample using a binsize that is twice our fragment size
    # We can reuse the binning function we already wrote

    scored_sample = bin_array(combined, 2 *frag_width)

    # Find the p-value for each position (you can pass a whole array of values
    # and and array of means). Use scipy.stats.poisson for the distribution.
    # Remeber that we're looking for the probability of seeing a value this large
    # or larger
    # Also, don't forget that your background is per base, while your sample is
    # per 2 * width bases. You'll need to adjust your background

    new_stats = 1-scipy.stats.poisson.cdf(scored_sample, mu = mod_control*frag_width*2)
    #print(new_stats)

    # Transform the p-values into -log10
    # You will also need to set a minimum pvalue so you doen't get a divide by
    # zero error. I suggest using 1e-250

    for i in np.arange(np.size(new_stats)):
        if new_stats[i] <= 0:
            new_stats[i] = 1e-250
   
    
    #for value in np.nditer(new_stats):
        #if value <= 0:
            #new_stats[value] = 1e-250

    log_pval = -1*(np.log10(new_stats))
    #print(log_pval)


    # Write p-values to a wiggle file
    # The file should start with the line
    # "fixedStep chrom=CHROM start=CHROMSTART step=1 span=1" where CHROM and
    # CHROMSTART are filled in from your target genomic region. Then you have
    # one value per line (in this case, representing a value for each basepair).
    # Note that wiggle files start coordinates at 1, not zero, so add 1 to your
    # chromstart. Also, the file should end in the suffix ".wig"
    modified_chrom_start = chromstart + 1
    write_wiggle(log_pval, chrom, modified_chrom_start, "sample1_pval_peaks.wig")
    # Write bed file with non-overlapping peaks defined by high-scoring regions 
    write_bed(log_pval, chrom, chromstart, chromend, frag_width, "sample1_peaks.bed")
    #are the scores my scored sample or my modified pvalues?
def write_wiggle(pvalues, chrom, chromstart, fname):
    output = open(fname, 'w')
    print(f"fixedStep chrom={chrom} start={chromstart + 1} step=1 span=1",
          file=output)
    for i in pvalues:
        print(i, file=output)
    output.close()

def write_bed(scores, chrom, chromstart, chromend, width, fname):
    chromlen = chromend - chromstart
    output = open(fname, 'w')
    while np.amax(scores) >= 10:
        pos = np.argmax(scores)
        start = pos
        while start > 0 and scores[start - 1] >= 10:
            start -= 1
        end = pos
        while end < chromlen - 1 and scores[end + 1] >= 10:
            end += 1
        end = min(chromlen, end + width - 1)
        print(f"{chrom}\t{start + chromstart}\t{end + chromstart}", file=output)
        scores[start:end] = 0
    output.close()




if __name__ == "__main__":
    main()