#!/usr/bin/env python3
import GK
import sys
import os
import json
from os.path import isfile
'''
This is the driver file, the algorithm(s) are in GK.py
all this file does is read from the text files and put data into memory,
call the Grochow-Kellis function and write data to text files.

Look at the GK.py file mainly.
'''
def getSubGraphs(subgraph_files):
    '''
    This method reads data from the subgraph files and generates a list of graphs
    which are adjacency lists and it returns the list of graphs.
    '''
    subgraphs = []
    for file in subgraph_files:
        with open(file,"r") as f:
            # read the file
            contents = f.read()
            contents = contents.split("\n")
            listOfEdgeLists = []
            for line in contents:
                if len(line) == 0:
                    continue
                # change the list which is a string in the file to a
                # real list with json.loads on it
                listOfEdgeLists.append(json.loads(line))
            listofgraphs = []
            for idx,edgelist in enumerate(listOfEdgeLists):
                # we convert the edge list format to a adjacency list with this method
                g = GK.convertElToDictGraph(edgelist)
                # we include some information about the subgraph along with it
                # such as how many vertices it has and its index in the text file
                listofgraphs.append((int(file[-5]),idx,g))
        subgraphs.append(listofgraphs)
    return subgraphs
def getNetwork(netfile):
    '''
    This reads data from the network.net file
    and converts it into a graph that is a adjacency list.
    '''
    network = None
    el = []
    with open(netfile,"r") as f:
        # we use the same algorithm as above for the subgraphs
        # to generate the big network graph
        # look in GK.py's adjListFromEdgeList function
        contents = f.read()
        contents = contents.split("\n")
        for line in contents:
            if "*" in line or len(line) == 0:
                continue
            tup = []
            nodes = line.split(' ')
            tup.append(int(nodes[0]))
            tup.append(int(nodes[1]))
            el.append(tup)
    network = GK.convertElToDictGraph(el)
    return network
def readData(netfile):
    '''
    Reads data from the text files and passes it into
    the other functions to generates graphs
    '''
    sortFunc = lambda x: int(x[-5])
    network = None
    subgraphs = None
    cwd = os.getcwd()
    raw = os.listdir(cwd+"/infiles")
    raw = ["./infiles/" + x for x in raw]
    files = [x for x in raw if isfile(x)]
    
    subgraph_files = [x for x in files if "allgraphs" in x]
    # sort the subgraph_files so that they are like allgraphs1.txt allgraphs2.txt and so on
    subgraph_files.sort(key = sortFunc)
    netfile = [x for x in files if netfile in x][0]
    
    subgraphs = getSubGraphs(subgraph_files)
    network = getNetwork(netfile)
    
    return network,subgraphs
def writeData(data, k,networkfile, writeOccs = False):
    '''
    This function writes data to the text files.
    '''
    networkfile = networkfile.split(".")
    networkfile = networkfile[0]
    outfile = "./outfiles/" + networkfile + "output.txt"
    with open(outfile,"w") as f:
        for i in range(k):
            knode = data[i]
            for thing in knode:
                nodeC = thing[0]
                idx = thing[1]
                occs = thing[2]
                fstr = "%d %d %d\n" % (nodeC, idx, occs)
                f.write(fstr)
                if writeOccs:
                    for nodeset in thing[3]:
                        strNodeSet = str(nodeset)
                        strNodeSet = strNodeSet + "\n"
                        f.write(strNodeSet)
    return 0
def main():
    """
    This function checks the command line arguments
    and calls functions to read data from the text file
    and it calls the main computation function and keeps track of the
    occurences of each subgraph in a list and then writes all of this to
    the output text files.
    """
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print("Error usage is: ./main.py netfile.net k",file = sys.stderr)
        exit(1)
    network_file = sys.argv[1]
    writeoccs = False
    if len(sys.argv) == 4 and sys.argv[3] == "write": 
        writeoccs = True
    
    k = int(sys.argv[2]) - 2
    if k < 1 or k > 6:
        print("Error k must be between 3 and 8 inclusive")
        exit(1)
    network, subgraphs = readData(network_file)

    # outlist is where we store all the information about the occurences
    outlist = []
    for _ in range(6): outlist.append([])
    for idx,sublist in enumerate(subgraphs):
        for i in range(len(sublist)):
            temp = [idx+3,sublist[i][1],0,[]]
            outlist[idx].append(temp)

    for i in range(k):
        knode = subgraphs[i]
        for tup in knode:
            Hnodes = tup[0] - 3
            idxH = tup[1]
            H = tup[2]
            # where the main work takes place
            # this is the most important function
            N,mappings = GK.subGraphOccurences(network,H)
            outlist[Hnodes][idxH][2] = N
            mapvals = []
            if writeoccs:
                for mapping in mappings:
                    temp = [mapping[k] for k in mapping]
                    mapvals.append(temp)
                outlist[Hnodes][idxH][3] = mapvals
    # write the data to the text files at the end
    writeData(outlist,k,network_file,writeOccs=writeoccs)


if __name__ == '__main__':
    main()