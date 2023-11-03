plink --vcf genotypes.vcf --recode --out ped_map_myfile

plink --file ped_map_myfile --pca 10 --out varaints

plink --vcf genotypes.vcf --freq

plink --vcf genotypes.vcf --linear --pheno CB1908_IC50.txt --covar varaints.eigenvec --allow-no-sex --out cb_gwas

plink --vcf genotypes.vcf --linear --pheno GS451_IC50.txt --covar varaints.eigenvec --allow-no-sex --out gs_gwas

CB data: The gene DIP2B was the closest associated with the top loci hit from my GWAS analysis. This gene encodes the disco interacting protein 2 homolog B which so
far has been speculated to be invovled in DNA methylation since it has a biding site for DNA methyltrasnferase and AMP binding sites. If this gene is mutated, it could
lead to abberrant DNA methylation which represses transcription of genes nearby the methylation site and recruits chromatin remodelers. Therefore, the mutant phenotype that we see os most likely due to a mutation whic inhbits DIP2B's ability to promote the methylation of DNA, therefore genes that are suppsoed to be turned off remain on causing
the observed mutant phenotype. Interestingly, this specific gene is noted in NCBI as being sensitive to folate, which could also alter the expression of DIP2B (citation: https://www.ncbi.nlm.nih.gov/gene/57609). 

GS data: The gene ZNF826 was the closes associated with the top loci from my GWAS analysis. This gene encodes the zinc finger protein 826. Zinc finger proteins are significant because zinc finger domains often indicate that a protein binds to DNA- say for example like a transcription factor. These proteins commonly consits of two beta sheets with an alpha helix in the middle and the alpha helix gives the protein specificty to bind to a specific region of DNA while the zinc ion stabilizes this shape. This particular protein has been thought to be involved in regulationn of transcription (citation: https://www.ncbi.nlm.nih.gov/gene/?term=ZNF826). Therefore, any mutation in this protein could impact the transcription of a variety of other genes as well and lead to a very signficant phenotype. 


