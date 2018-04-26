from Bio import SeqIO
import argparse
import gzip
import regex
import pickle


def main():
    parser = argparse.ArgumentParser(
        description='Extract genes from reads')
    parser.add_argument('file1', metavar="<FILE1>",
                        help='file containing first reads from PE')

    args = parser.parse_args()
    r1 = make_read_list(args.file1)

    #for i in range(len(r1)):
    print(r1[0])
        
def make_read_list(file):
    reads = []
    handle = open(file, 'rU')
    for record in SeqIO.parse(handle, "fasta"):
        reads.append(str(record.seq))
    return(reads)

if __name__ == '__main__':
    main()
