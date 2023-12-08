#!/usr/bin/env python

import sys

import scanpy as sc
import numpy
import matplotlib.pyplot as plt


adata = sc.read_h5ad("filtered_clustered_data.h5")
adata.uns['log1p']['base'] = None # This is needed due to a bug in scanpy 

fig, ax = plt.subplots()
sc.pl.umap(adata, color=["NKG7", "CD79A", "LYZ"], title=["NK", "B-Cells", "Myeloid"], show=False)
plt.savefig("Exercise3plot1.png")

adata.rename_categories('leiden', ["0", "Myeloid", "B-Cells", "3", "4", "5", "6", "Natural Killer"])

fig, ax = plt.subplots()
sc.pl.umap(adata, color='leiden', title='UMAP', show=False)
plt.tight_layout()
plt.savefig("Exercise3plot2.png")

