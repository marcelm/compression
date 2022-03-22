# Datasets

- very short reads (35 bp)
- 100 bp
- 150 bp
- 250 bp
- 300 bp (MiSeq)
- interleaved
- PacBio
- Nanopore
- with and without quality binning
- with and without second header


* SRR020285
* ERR1760498



fastq-dump --split-3 --defline-qual '+' --defline-seq '@$sn' SRR020285
fastq-dump --split-3 --defline-qual '+' --defline-seq '@$sn' ERR1760498






fastq-dump --defline-qual '+' --defline-seq '@$ac.$si' SRR2174302


