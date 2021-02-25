#!/usr/bin/env python

import argparse
import random

def get_args():
    '''Argparse code to allow for in-line command interface.'''

    parser = argparse.ArgumentParser(description=
    """WORDS""")
    parser.add_argument('-f1','--file1',  action='store', nargs='?', type=str, 
                    required=True, help='Name of fasta file 1')
    parser.add_argument('-f2','--file2',  action='store', nargs='?', type=str, 
                    required=True, help='Name of fasta file 2')
    parser.add_argument('-f3','--file3',  action='store', nargs='?', type=str, 
                    required=True, help='Name of fasta file 3')
    parser.add_argument('-f4','--file4',  action='store', nargs='?', type=str, 
                    required=True, help='Name of fasta file 4')
    parser.add_argument('-o','--out',  action='store', nargs='?', type=str, 
                    required=True, help='Name of output file')

    return parser.parse_args()

def getSize(file1:str)->int:
    '''Returns the line count of the fasta file'''
    lc = 0

    with open(file1) as fh
        for line in fh:
            lc += 1

    return lc/2

def main(files:list, outfile:str):
    line_count = getSize(files[0]) # line count of 1 file, assumes all files input are of the same size
    ZMW_dict = dict()
    length_list = dict()
    length_counter = 0

    for fh in files:
        with open(fh, "r") as fh:
            for line in fh:  
                if line[0] == ">":
                    header = line
                    nZMW = line.split("/")[1]
                else:
                    sequence = line
                    length = len(line)
                    
                    if nZMW in ZMW_dict:
                        if length > len(ZMW_dict[nZMW][1]):
                            ZMW_dict[nZMW] = [header, sequence]
                    else:
                        ZMW_dict[nZMW] = [header, sequence]

                    if length in length_list: # store all ZMW with equal lengths
                        length_list[length].append(nZMW)
                    else: 
                        length_list[length] = [nZMW]
                    
                    if length_counter > 0.75 * 4 * line_count:
                        if len(length_list[min(length_list)]) > 1:
                            # choose a random sequence to delete
                            temp = random.choice(length_list[min(length_list)])
                            del ZMW_dict[temp]
                            length_list[min(length_list)].remove(temp)
                        else:
                            del ZMW_dict[length_list[min(length_list)]
                            del length_list[min(length_list)]
                    
                    length_counter += 1
    
    # output file
    out = open(outfile, "w")

    for nZMW in ZMW_dict:
        for line in ZMW_dict[zMW]:
            out.writelines(line)

    out.close()

if __name__ == "__main__":
    args = get_args()
    files = [args.file1, args.file2, args.file3, args.file4]
    outfile = args.out

    main(files, outfile)