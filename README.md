# GC2 Network Motifs, in Python

The output file(s) are in `./code/outfiles/graphNoutput.txt`.

Make sure you have a version of python3 and are in a Linux or Mac environment.

## Instructions to Run:
- `git clone https://github.com/jptboy/CSCI3104_GC2.git && cd CSCI3104_GC2`
- `cd code`
- To run the program for **ALL `graphN.net` FILES** in order to generate all output files
    - make sure k is between 3 and 8
    - `python3 runAllNetworks.py k`
        - example: `python3 runAllNetworks.py 8`
    - Do `python3 runAllNetworks.py k write` if you want to write all subgraph occurences to the output files
- `chmod 777 main.py`
- Before running the next commands, select a `k` between 3 and 8, and a valid `graphN.net` file from one of these files:
    - `graph1.net`
    - `graph2.net`
    - `graph3.net`
    - `graph4.net`
- `./main.py graphN.net k`
- `./main.py graphN.net k write` if you want a list of occurences of subgraphs in the network.

## Examples:
- `./main.py graph3.net 5`
    - counts how many isomorphisms of graphs up to 5  nodes occur in `graph3.net`.
- `./main.py graph3.net 8 write`
    - counts how many isomorphisms of graphs up to 8  nodes occur in `graph3.net` and writes the nodes that make up these isomorphisms into the text file.
