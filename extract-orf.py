from Bio import SeqIO
from Bio.Seq import Seq
import argparse
import gzip
import regex
import pickle


def main():
    # Parse arguments
    parser = argparse.ArgumentParser(
        description='Extract genes from reads')
    parser.add_argument('file1', metavar="<FILE1>",
                        help='file containing sequence reads')
    parser.add_argument('file2', metavar="<FILE1>",
                        help='file containing genes')

    args = parser.parse_args()

    # Get headers and reads from multi-sequence file
    headers, r1 = make_read_list(args.file1)
    # Get indices of missing nt
    nvec = find_occurences(r1[0], '-')
    # Create a new read with missing nuclieotides removed
    newread = extract_characters_indices(r1[0], nvec)

    # Get genes
    gheaders, genes = make_read_list(args.file2)
    # Corresponding to BWRF1
    gene = revcom(genes[0])
    
    # Pattern matching using regex
    pattern = regex.compile(r"(" + gene + r"){e<=1}", flags=regex.IGNORECASE|regex.BESTMATCH)
    result = pattern.search(newread)
    
    if result:
        # store start and end position of the gene
        print(result.start(), result.end())

    # Write to a fasta file
    file = open("bhlf1.fasta","w") 

    for i in range(len(r1)):
        # Extract - from specific locations
        newread = extract_characters_indices(r1[i], nvec)
        file.write(">" + str(headers[i]))
        file.write("\n")
        #file.write(str(newread[24828:25980]))
        file.write(str(newread[result.start():result.end()]))
        file.write("\n")
        
    file.close()

# Take reverse complement
def revcom(seq):
    rc = str(Seq(seq).reverse_complement())
    return(rc)

# Function to extract characters at particular indices from a string
def extract_characters_indices(string, vecindices):
    # Add 0 and the length to the start and the end of the string
    vecindices = [0] + vecindices + [len(string)]
    newread = ''
    for i in range(len(vecindices) - 1):

        start = vecindices[i]
        end = vecindices[i+1]
        if vecindices[i] != 0:
            start = vecindices[i] + 1;
        newread += string[start:end]
    return newread

# Find all occurences of a given character in a string
def find_occurences(string, ch):
    return [i for i, letter in enumerate(string) if letter == ch]

# Get a list of headers and reads from a fasta file
def make_read_list(file):
    reads = []
    headers = []
    handle = open(file, 'rU')
    for record in SeqIO.parse(handle, "fasta"):
        headers.append(str(record.id))
        reads.append(str(record.seq))
    return(headers, reads)

if __name__ == '__main__':
    main()
