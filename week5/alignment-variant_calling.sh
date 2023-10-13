#!/bin/bash

bwa index sacCer3.fa

for sample in A01_09 A01_24 A01_35 A01_63 A01_11 A01_27 A01_39 A01_23 A01_31 A01_62
do
    echo "Aligning sample:" $sample
    bwa mem -t 4 -R "@RG\tID:${sample}\tSM:${sample}" sacCer3.fa ${sample}.fastq > ${sample}.sam 
done

for file in A01_09 A01_24 A01_35 A01_63 A01_11 A01_27 A01_39 A01_23 A01_31 A01_62
do
    echo "Sorting sample:" $file
    samtools sort ${file}.sam -o ${file}.bam 
done

for file in A01_09 A01_24 A01_35 A01_63 A01_11 A01_27 A01_39 A01_23 A01_31 A01_62
do
    echo "Indexing sample:" $file
    samtools index ${file}.bam 
done

freebayes -f sacCer3.fa A01_09.bam A01_24.bam A01_35.bam A01_63.bam A01_11.bam A01_27.bam A01_39.bam A01_23.bam A01_31.bam A01_62.bam > yeast_var.vcf

vcffilter -f "QUAL > 20" yeast_var.vcf > updated_yeast_var.vcf

vcfallelicprimitives -k -g updated_yeast_var.vcf > decomplex_yeast_var.vcf

snpEff ann R64-1-1.105 decomplex_yeast_var.vcf > ann_yeast_var.vcf

head -100 ann_yeast_var.vcf > sample_ann_yeast_var.vcf #has a bunch of junk at the top, not the first 100 lines of actual data





