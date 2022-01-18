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


$ for l in 1 2 3 4 5 6 7 8 9; do echo $l; time lzop -$l < file.fastq > file.cl$l.lzop; done
1

real    0m1.432s
user    0m0.852s
sys     0m0.572s
2

real    0m1.405s
user    0m0.825s
sys     0m0.580s
3

real    0m1.394s
user    0m0.881s
sys     0m0.513s
4

real    0m1.508s
user    0m0.908s
sys     0m0.496s
5

real    0m1.429s
user    0m0.897s
sys     0m0.531s
6

real    0m1.417s
user    0m0.888s
sys     0m0.529s
7

real    1m19.086s
user    1m18.176s
sys     0m0.572s
8

real    2m46.511s
user    2m44.730s
sys     0m0.608s
9

real    3m58.234s
user    3m56.906s
sys     0m0.808s


$ for l in 1 2 3 4 5 6 7 8 9; do echo $l; time lz4 -$l < file.fastq > file.cl$l.lz4; done
1

real    0m2.260s
user    0m0.896s
sys     0m1.086s
2

real    0m1.512s
user    0m0.977s
sys     0m0.531s
3

real    0m6.677s
user    0m6.137s
sys     0m0.513s
4

real    0m8.951s
user    0m8.421s
sys     0m0.503s
5

real    0m14.061s
user    0m13.461s
sys     0m0.492s
6

real    0m20.752s
user    0m20.332s
sys     0m0.393s
7

real    0m32.706s
user    0m32.260s
sys     0m0.388s
8

real    0m47.403s
user    0m46.922s
sys     0m0.360s
9

real    1m24.715s
user    1m23.029s
sys     0m0.492s


$ for l in 1 2 3 4 5 6 7 8 9; do echo $l; time gzip -$l < file.fastq > file.cl$l.gz; done
1

real    0m4.854s
user    0m4.606s
sys     0m0.241s
2

real    0m5.084s
user    0m4.814s
sys     0m0.268s
3

real    0m6.949s
user    0m6.680s
sys     0m0.268s
4

real    0m6.115s
user    0m5.779s
sys     0m0.329s
5

real    0m9.842s
user    0m9.604s
sys     0m0.236s
6

real    0m23.096s
user    0m22.801s
sys     0m0.280s
7

real    0m39.374s
user    0m39.064s
sys     0m0.276s
8

real    1m5.513s
user    1m4.640s
sys     0m0.424s
9

real    1m31.852s
user    1m31.086s
sys     0m0.512s



