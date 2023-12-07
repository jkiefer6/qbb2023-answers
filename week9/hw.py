#!/usr/bin/env python

import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.stats import multitest
from pydeseq2 import preprocessing
from pydeseq2.dds import DeseqDataSet
from pydeseq2.ds import DeseqStats


counts_df = pd.read_csv("gtex_whole_blood_counts_formatted.txt", index_col = 0)
metadata = pd.read_csv("gtex_metadata.txt", index_col = 0)

"""
counts_df_normed = preprocessing.deseq2_norm(counts_df)[0]
counts_df_normed = np.log2(counts_df_normed + 1)
full_design_df = pd.concat([counts_df_normed, metadata], axis=1)

model = smf.ols(formula = 'Q("DDX11L1") ~ SEX', data=full_design_df)
results = model.fit()

slope = results.params[1]
pval = results.pvalues[1]


full_design_dfT = full_design_df.transpose()
n = 3
full_design_dfT.drop(full_design_dfT.tail(n).index, inplace = True)
full_design_dfT = full_design_dfT.reset_index()   

all_results = pd.DataFrame(columns=['Gene', 'Slope', 'Pval'])
for line in range(len(full_design_dfT)):
    gene = full_design_dfT.at[line, "index"]
    model = smf.ols(formula = f'Q("{gene}") ~ SEX', data=full_design_df) 
    results = model.fit()
    slope = results.params[1]
    pval = results.pvalues[1]
    all_results.loc[line] = [gene, slope, pval]
all_results.to_csv('output_results.csv', index=False)


results = pd.read_csv("output_results.csv")
pvals_unclean = results["Pval"]
genes_unclean = results["Gene"]

pvals = []
genes = []
for line in range(len(pvals_unclean)):
    pvalue = pvals_unclean.iloc[line]
    gene = genes_unclean.iloc[line]
    if pd.notna(pvalue):
        pvals.append(pvalue)
        genes.append(gene)

fdr_pvals = multitest.fdrcorrection(pvals, alpha=0.10)
fdr_pvals_actual = fdr_pvals[1]
final_results = pd.DataFrame({'Gene': genes, "FDR_Pvals": fdr_pvals_actual})
final_results_sorted = final_results.sort_values(by='FDR_Pvals')
significant_results = final_results_sorted[final_results_sorted['FDR_Pvals'] < 0.1]

significant_results.to_csv('signifcant_results.txt', sep='\t', index=False)
significant_results.to_csv('signifcant_results.csv', sep='\t', index=False)
"""


dds = DeseqDataSet(
    counts=counts_df,
    metadata=metadata,
    design_factors="SEX",
    n_cpus=4,
)

dds.deseq2()
stat_res = DeseqStats(dds)
stat_res.summary()
results = stat_res.results_df
results_sorted = results.sort_values(by='padj')
significant_results = results_sorted[results_sorted['padj'] < 0.1]
significant_results = significant_results.reset_index() 
genes = significant_results["index"]
sig_pvals = significant_results["padj"]

sig_results_mod = pd.DataFrame({"Gene": genes, "Pvals": sig_pvals})
sig_results_mod.to_csv('deseq2_signifcant_results.txt', sep='\t', index=False)

deseq2_sig_results = pd.read_csv("deseq2_signifcant_results.csv")
manual_sig_results = pd.read_csv("signifcant_results.csv", delim_whitespace = True)

man_gen = manual_sig_results["Gene"]
deseq2_gen = deseq2_sig_results["Gene"]

manual_genes = set(man_gen)
deseq2_genes = set(deseq2_gen)

shared_genes = len(manual_genes.intersection(deseq2_genes))
manual_unique_genes = len(manual_genes.difference(deseq2_genes))
deseq2_unique_genes = len(deseq2_genes.difference(manual_genes))
jaccard_index = (shared_genes / (manual_unique_genes + deseq2_unique_genes + shared_genes)) * 100
print(jaccard_index)


results_reset = results.reset_index()
clean_padj = []
clean_log = []
for line in range(len(results_reset)):
    padj = results_reset.at[line, "padj"]
    logadj = results_reset.at[line, "log2FoldChange"]
    if pd.notna(padj):
        clean_padj.append(padj)
        clean_log.append(logadj)

import matplotlib.pyplot as plt


graph_pvals = -(np.log10(clean_padj))
color = []
for line in range(len(graph_pvals)):
    value = graph_pvals[line]
    item = clean_log[line]
    if value > 1 and (item < -1 or item > 1):
        color.append('r')
    else:
        color.append('k') 

fig, (ax) = plt.subplots()
ax.scatter(clean_log, graph_pvals, color = color)
ax.hlines(y = 5, xmin = -6, xmax = 4, color = 'k', linestyle = 'dotted')
ax.vlines(x = 1, ymin = 0, ymax = 250, color = 'k', linestyle = 'dotted')
ax.vlines(x = -1, ymin = 0, ymax = 250, color = 'k', linestyle = 'dotted')
ax.set_xlabel("log2FoldChange")
ax.set_ylabel("-Log10(Q Value)")
plt.tight_layout()
plt.show()
fig.savefig( "volcano.png" )
plt.close(fig)




