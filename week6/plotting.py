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
gs_p = cb_gwas["P"]
length = len(cb_p)
cb_10p = -(np.log10(cb_p))
gs_10p = -(np.log10(gs_p))

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




"""
fig,(ax) = plt.subplots() 
ax.set_title( "CB1980" )
ax.scatter(chromosome_lengths, cb_10p)
ax.set_xlabel("Chromosome")
ax.set_ylabel("-Log10 P-value")
plt.show()
"""

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


















