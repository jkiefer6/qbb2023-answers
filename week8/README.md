Rscript runChicago.R --design-dir raw/Design --en-feat-list raw/Features/featuresGM.txt --export-format washU_text raw/PCHIC_Data/GM_rep1.chinput,raw/PCHIC_Data/GM_rep2.chinput,raw/PCHIC_Data/GM_rep3.chinput output

Active regions are enriched which is to be expected since the interactions are more likely to happen in open areas of the genome. The CTCF interactions make sense since two CTCFs that interact may be TAD boundaries and therefore these boundaries may be far apart, but through DNA looping are actually creating a section of the genome with enriched interactions. To keep this loop, the CTCFs need to be near each other and bind the insulator proteins. The H3K4me1 mark is enriched which is not suprising. It is the mark is of a enhancer regions and enhancers a frequntly have ling range interactions with the genes they activate and additionally, shadow enhancers are know to work in conjunction with other enhancers to provideredundnacy for a pathway. H3K4me3 (or a mark of promoters) is also highly enriched which makes sense since promoters and enhancers again can have longer range interactions to activate trasncription of genes. H3K27ac, also a mark of an active enhancer, is likewise enriched for the same reasons as previously stated. H3K27me3 is the mark of facultative heterochromatin and is not enriched which makes sense because these regions are deliberately held inactive and cannot interact with other areas of the gneome. H3K9me3 is slightly enriched which is surprising, but the level of interactions is not very high which makes sense since this is a mark of constitutive heterochromatin and these regions are not likely to have long range interactions with other places in the genome. 

Top 6 interactions between 2 promoters: 
Chrom Chrom_start Chrom_end col_n Score Value Ex Color  ... Source_end   Source_name Source_strand target_chrm target_start target_end  target_name target_strand
487  chr20    44562442  44565593     .  1000    34  .     0  ...   44565593         PCIF1             +       chr20     44438565   44442365        UBE2C             +
497  chr20    44596299  44607204     .   986    34  .     0  ...   44607204  FTLP1;ZNF335             +       chr20     44438565   44442365        UBE2C             +
818  chr21    26837918  26842640     .   978    34  .     0  ...   26842640        snoU13             +       chr21     26926437   26939577     MIR155HG             +
488  chr20    44562442  44565593     .   974    33  .     0  ...   44565593         PCIF1             +       chr20     44452862   44471524  SNX21;TNNC2             +
86   chr20    17946510  17951709     .   973    33  .     0  ...   17951709    MGME1;SNX5             +       chr20     17660712   17672229        RRBP1             +
133  chr20    24972345  24985047     .   973    33  .     0  ...   24985047         APMAP             +       chr20     25036380   25043735        ACSS1             +

Top 6 interactions between a promoter and enhancer:  
Chrom Chrom_start Chrom_end col_n Score Value Ex  ...         Source_name Source_strand target_chrm target_start target_end target_name target_strand
2020  chr21    26926437  26939577     .   952    33  .  ...            MIR155HG             +       chr21     26797667   26799364           .             -
1655  chr20    55957140  55973022     .   928    32  .  ...  RBM38;RP4-800J21.3             +       chr20     56067414   56074932           .             -
2016  chr21    26926437  26939577     .   838    29  .  ...            MIR155HG             +       chr21     26790966   26793953           .             -
177   chr20     5585992   5601172     .   830    28  .  ...              GPCPD1             +       chr20      5625693    5628028           .             -
2017  chr21    26926437  26939577     .   754    26  .  ...            MIR155HG             +       chr21     26793954   26795680           .             -
218   chr20     5929472   5933156     .   750    26  .  ...          MCM8;TRMT6             +       chr20      5515866    5523933           .             -
.             -


Yes, GPCPD1 makes sense to be interacting in B cells since it is expressed in the bone marrow and involved in metabolism and may be involved in regulating an immune response. 

MCM8 is a mini-chromosome maintenece protein (which is involved in replication firing) and TRMT6 which is a methyltransferase and may be invovlde in regualting viral replication. Therefore, it makes sense that these two genes may be interacting, esepcially within an immune context. 









