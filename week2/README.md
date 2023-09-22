1.1 1 Mbp * 3x coverage = 3Mbp total; 3 million bp/100 bp = 30,000 reads
1.3.1 50,641 bases have 0 coverage or 5.0641% of the genome has zer coverage.
1.3.2 This fits the poisson expectations which suggest that the area with zero coverage should be about 50,000 and the Poisson distribution fit the curve well. The normal distrbution fits the simulationa bit worse than the Poisson becasue the normal distribution fits less well for smaller means (ie smaller coverage). If we increase the coverage than we should see that the fit of normal distribution would improve. 
1.4.1 There are 52 bases with zero coverage or 0.0052% of the genome
1.4.2 The Poisson distribution fits the curve well, better than the 3x coverage. Similarly, the normal distrbution fits the simulation slightly worse than the Poisson becasue the normal distribution fits less well for smaller means (ie smaller coverage). But the normal distribution fits the simulation much better than for 3x coverage.
1.5.1 There are 9 bases with zero coverage or 0.0009% of the genome.
1.5.2 Both the normal distribution and the Poisson distribution fit the simulation very well. This is becasue the increased coverage leads to increased means and lamda which contributes to the distributions fitting very well to the simualtion. 
2.4 dot -Tpng edges.dot -o ex2_digraph.png