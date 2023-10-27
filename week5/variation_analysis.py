#!/usr/bin/env python


import matplotlib.pyplot as plt

depths = []
allele_freq = []
parsing_list = []
annotations = []
geno_q = []
for line in open("sample_ann_yeast_var.vcf"):
    if line.startswith('#'):
        continue
    fields = line.rstrip('\n').split('\t')
    formats = fields[9:]
    for value in formats:
        parsing1 = value.split(",")
        #print(parsing1)
        for item in parsing1:
            parsing2 = item
            par3 = parsing2.split(":")
            #print(par3)
            if len(par3) > 1:
                depths.append(par3[1])
            if len(par3) > 2:
                geno_q.append(par3[2]) # this is AD not GQ bc I don't see GQ in my practice set
    infos = fields[7]
    parsed = infos.split(";")
    #print(parsed)
    annotations.append(parsed[40])
    allele_freq.append(parsed[3])


ann_set = set(annotations)
ann_counts = len(ann_set)

fig, (ax) = plt.subplots(2,2)
ax[1,1].hist(allele_freq)
ax[1,1].set_xlabel("Allele Frequency")
ax[1,1].set_ylabel("Count")
#ax[1,1].set_xticks(allele_freq, rotation = 40)
ax[0,0].hist(depths)
ax[0,0].set_xlabel("Read Depth")
ax[0,0].set_ylabel("Count")
#ax[0,0].set_xticks(depths, rotation = 40)
ax[0,1].hist(geno_q)
ax[0,1].set_xlabel("Genotype Quality")
ax[0,1].set_ylabel("Count")
#ax[0,1].set_xticks(geno_q, rotation = 40)
ax[1,0].bar(annotations, ann_counts)
ax[1,0].set_xlabel("Variant Effect")
ax[1,0].set_ylabel("Count")
#ax[1,0].set_xticks(annotarotation = 40)

plt.tight_layout()

plt.show()
fig.savefig("var_calls_try1.png")
plt.close(fig)


