#!/usr/bin/env python3
import GK
import sys
import os
import json
from os.path import isfile
def getSubGraphs(subgraph_files):
    subgraphs = []
    for file in subgraph_files:
        with open(file,"r") as f:
            contents = f.read()
            contents = contents.split("\n")
            listOfEdgeLists = []
            for line in contents:
                if len(line) == 0:
                    continue
                listOfEdgeLists.append(json.loads(line))
            listofgraphs = []
            for idx,edgelist in enumerate(listOfEdgeLists):
                g = GK.convertElToDictGraph(edgelist)
                listofgraphs.append((int(file[-5]),idx,g))
        subgraphs.append(listofgraphs)
    return subgraphs
def getNetwork(netfile):
    network = None
    el = []
    with open(netfile,"r") as f:
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
    sortFunc = lambda x: int(x[-5])
    network = None
    subgraphs = None
    cwd = os.getcwd()
    raw = os.listdir(cwd+"/infiles")
    raw = ["./infiles/" + x for x in raw]
    files = [x for x in raw if isfile(x)]
    
    subgraph_files = [x for x in files if "allgraphs" in x]
    subgraph_files.sort(key = sortFunc)
    netfile = [x for x in files if netfile in x][0]
    
    subgraphs = getSubGraphs(subgraph_files)
    network = getNetwork(netfile)
    
    return network,subgraphs
def writeData(data, k,writeOccs = False):
    outfile = "./outfiles/output.txt"
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
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print("Error usage is: ./main.py netfile.net k",file = sys.stderr)
        exit(1)
    args = sys.argv
    network_file = sys.argv[1]
    writeoccs = False
    if len(sys.argv) == 4 and sys.argv[3] == "write": 
        writeoccs = True
    
    k = int(sys.argv[2]) - 2
    if k < 1 or k > 6:
        print("Error k must be between 3 and 8 inclusive")
        exit(1)
    network, subgraphs = readData(network_file)

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
            N,mappings = GK.subGraphOccurences(network,H)
            outlist[Hnodes][idxH][2] = N
            mapvals = []
            if writeoccs:
                for mapping in mappings:
                    temp = [mapping[k] for k in mapping]
                    mapvals.append(temp)
                outlist[Hnodes][idxH][3] = mapvals

    writeData(outlist,k,writeOccs=writeoccs)


if __name__ == '__main__':
    main()