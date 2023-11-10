#!/usr/bin/env python

import pandas as pd 
import matplotlib.pyplot as plt
import scipy.stats
import numpy as np 


vec_data = pd.read_csv('varaints.eigenvec', sep = ' ', header=None)
#convert to list .loc[:2] .loc[:3]

pca1 = vec_data.loc[:, 2]
pca2 = vec_data.loc[:, 3]
#print(pca1)
#print(pca2)

fig, (ax) = plt.subplots()
ax.set_title( "PCA Analysis" )
ax.scatter(pca1, pca2)
ax.set_xlabel("PCA 1")
ax.set_ylabel("PCA 2")
#plt.show()
fig.savefig( "pca2_analysis.png" )
plt.close(fig)

allel_freq = pd.read_csv('plink.frq', delim_whitespace=True)
freq = allel_freq["MAF"]



fig, (ax) = plt.subplots() 
ax.set_title( "Allele Frequency" )
ax.hist(freq, bins = 80)
ax.set_xlabel("Frequency")
ax.set_ylabel("Counts")
plt.show()
fig.savefig( "allele_freq.png" )
plt.close(fig)

cb_gwas = pd.read_csv('cb_gwas.assoc.linear', delim_whitespace=True)
gs_gwas = pd.read_csv('gs_gwas.assoc.linear', delim_whitespace=True)

cb_p = cb_gwas["P"]
gs_p = gs_gwas["P"]


cb_p_true = []
cb_test = cb_gwas["TEST"]
for line in range(len(cb_test)):
    site = cb_test[line] 
    if site == "ADD":
        cb_p_true.append(float(cb_p[line]))


gs_p_true = []
gs_test = gs_gwas["TEST"]
for line in range(len(gs_test)):
    site = gs_test[line] 
    if site == "ADD":
        gs_p_true.append(float(gs_p[line]))



length = len(cb_p_true)
cb_10p = -(np.log10(cb_p_true))
gs_10p = -(np.log10(gs_p_true))

color_cb = []
color_gs = []

for value in cb_10p:
    if value > 5:
        color_cb.append('r')
    else:
        color_cb.append('b')

for item in gs_10p:
    if item > 5:
        color_gs.append('m')
    else:
        color_gs.append('y')


def createList(r1, r2):
 if (r1 == r2):
  return "equal"
 else:
  res = []
  while(r1 < r2 ):
   res.append(r1)
   r1 += 1
  return res
  
start = 0
chromosome_lengths = (createList(start, length))


fig, (ax) = plt.subplots(2) 
ax[0].set_title( "CB1980" )
ax[0].scatter(chromosome_lengths, cb_10p, c = color_cb)
ax[0].set_xlabel("Chromosome")
ax[0].set_ylabel("-Log10 P-value")
ax[0].hlines(y = 5, xmin = start, xmax = length, color = 'r', linestyle = '-')
ax[0].margins(x=0, y=0)
ax[1].set_title( "GS451" )
ax[1].scatter(chromosome_lengths, gs_10p, c = color_gs)
ax[1].set_xlabel("Chromosome")
ax[1].set_ylabel("-Log10 P-value")
ax[1].hlines(y = 5, xmin = start, xmax = length, color = 'm', linestyle = '-')
ax[1].margins(x=0, y=0)
plt.tight_layout()
plt.show()
fig.savefig( "manhattan.png" )
plt.close(fig)

highest_snp = (min(cb_p_true))
#print(highest_snp)


index = 0
for value in cb_p_true:
    if value == 8.199e-12:
        print(index)
    index += 1
#184404
#print(cb_gwas.iloc[[2028444]])
#snp of interest is rs10876043


genotypes = pd.read_csv('genotypes.vcf', delimiter = '\t', skiprows = 27)
#print(genotypes)

#how do we specify a specific snp to sort for mutations in?
#in a for loop and then do we need to know the header for the columns? like what's 1169_1169?


SNPs = genotypes["ID"]
index = 0
for value in SNPs:
    if value == 'rs10876043':
        print(index)
    index = index + 1
#index call for genotype data is 184404

snp_interest_row = genotypes.iloc[184404]
#print(snp_interest_row)

#print(snp_interest_row.head(20)) #skip first 9 rows

mod_snp_row = snp_interest_row.iloc[9:]
#print(mod_snp_row)


phenotype_indexes = []
genotypes = []
index = 0
for row in mod_snp_row:
    if row != "./.":
        genotypes.append(row)
    else:
        phenotype_indexes.append(index)
    index += 1

phenotype_indexes_useful = []
for value in range(len(phenotype_indexes)):
    number = phenotype_indexes[value]
    mod_number = number + 1000
    phenotype_indexes_useful.append(mod_number)
#print(phenotype_indexes_useful)

big_phenotypes = pd.read_csv("CB1908_IC50.txt", delim_whitespace=True)


modified_pheno_data = big_phenotypes[~big_phenotypes["FID"].isin(phenotype_indexes_useful)]
phenotypes = modified_pheno_data["CB1908_IC50"]




wt = []
het = []
mut = []

index = 0
for value in genotypes:
    if value == "0/0":
        wt.append(phenotypes.iloc[index])
    if value == "0/1":
        het.append(phenotypes.iloc[index])
    if value == "1/1":
        mut.append(phenotypes.iloc[index])
    index = index + 1



het_mod = []
mylabels = ["Wildtype", "Heterozygous", "Homozygous Mutant"]

for i in range(len(het)):
    if str(het[i]) == 'nan':
        continue
    else:
        het_mod.append(het[i])

data = [wt, het_mod, mut]

fig,(ax) = plt.subplots() 
ax.set_title( "Effect Size" )
ax.boxplot(data, labels = mylabels)
ax.set_xlabel("Genotype")
ax.set_ylabel("IC_50")
plt.show()
fig.savefig( "effect_size.png" )
plt.close(fig)


#finding the top loci:
highest_snp = (min(cb_p_true))

index = 0
for value in cb_p_true:
    if value == 8.199e-12:
        print(index)
    index += 1
#184404
#print(cb_gwas.iloc[[184404]])
#snp of interest is rs10876043
#bp chrm 12 @ 49,190,411 (DIP2B gene)


highest_snp_gs = (min(gs_p_true))
print(highest_snp_gs)


index = 0
for value in gs_p_true:
    if value == 1.43e-07:
        print(index)
    index += 1
#2650065
#print(gs_gwas.iloc[[2650065]])
#bp chrm 19 @ 20,372,113 (ZNF826)

