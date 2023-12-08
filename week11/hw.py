#!/usr/bin/env python

import sys

import scanpy as sc
import numpy
import matplotlib.pyplot as plt

# Read the 10x dataset filtered down to just the highly-variable genes
adata = sc.read_h5ad("variable_data.h5")
adata.uns['log1p']['base'] = None # This is needed due to a bug in scanpy 

#Making a neighborhood graph:
sc.pp.neighbors(adata, n_neighbors=10, n_pcs=40)

#Leiden Clustering:
sc.tl.leiden(adata)

#UMAP
sc.tl.umap(adata, maxiter=900)

#tSNE
sc.tl.tsne(adata)

#Visualization

fig, axes = plt.subplots(ncols=2)
sc.pl.umap(adata, color='leiden', ax = axes[0], title='UMAP', show=False) #i don't know if brackets are necessary here
sc.pl.tsne(adata, color='leiden', ax = axes[1], title='tSNE', show=False)
fig.tight_layout()
fig.savefig( "UMAP_tSNE.png" )
plt.close(fig)

#Exercise 2
#Wilcoxon
wilcoxon_adata = sc.tl.rank_genes_groups(adata, method ='wilcoxon', groupby='leiden', use_raw=True, copy=True)
logreg_adata = sc.tl.rank_genes_groups(adata, method = 'logreg', groupby='leiden', use_raw=True, copy=True)


# sc.pl.rank_genes_groups(wilcoxon_adata, n_genes=25, title='Wilcoxon', use_raw=True, sharey=False, show=False, ax=ax, save = "_wilcoxon.png")
# sc.pl.rank_genes_groups(logreg_adata, n_genes=25,  title='LogReg', use_raw=True, sharey=False, show=False, ax=ax, save = "_logreg.png")


#Exercise 3:
leiden = adata.obs['leiden']
umap = adata.obsm['X_umap']
tsne = adata.obsm['X_tsne']
adata = sc.read_h5ad('filtered_data.h5')
adata.obs['leiden'] = leiden
adata.obsm['X_umap'] = umap
adata.obsm['X_tsne'] = tsne

adata.write('filtered_clustered_data.h5')




