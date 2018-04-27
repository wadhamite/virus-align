# Extract genes from multi-sequence file
> Charlotte Houldcroft & Krishna Kumar

# Code to extract open reading frames (ORFs) from a multiple sequence alignment
# It works by taking an MSA and removing all - from the reference sequence (must be top of file)
# It then matches the refseq to the refseq CDS for a given ORF and extracts that region from all the sequences in the MSA, thus producing a gene-by-gene 'chunked' MSA

## Installation instructions

```
pip3 install virtualenv
virtualenv env
source env/bin/activate
pip3 install -r requirements.txt
```


## Run Python code to extract genes

```
python3 extract-orf.py multialigned_sequence.fasta genes.fasta 
```
