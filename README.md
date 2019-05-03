# GC2: Network Motifs, in Python

## Subgraph Counts
- Our results for the count of subgraphs up to 5 nodes are in the `./code/outfiles/` directory as `saved_graphNoutput.txt` where `N` is the network number.
    - For example `saved_graph4output.txt`is the count of all subgraphs up to 5 nodes in `graph4.net`.
- 5 node subgraph counts for each network in a reasonable amount of time was one of the assignment's requirements, and this was fulfilled.
- You can try running it for 6-8 node subgraphs, but it will probably take a few hours.
    - Run `python3 runAllNetworks.py 8` to generate output files for subgraph counts up to 8 nodes.

## Algorithm
- We implemented the Grochow-Kellis algorithm to map the subgraphs onto the larger network. Our algorithm passed all the test cases on Moodle. At the bottom of GK.py, you should be able to see the tester function as well as the tests. If you run `GK.py` with `python3 GK.py` all tests will pass. An assert statement within our code should validate this as well.

## Instructions to Run:
- **Make sure you have a version of python3 and are in a POSIX environment like Linux or Mac OSX.**
- `git clone https://github.com/jptboy/CSCI3104_GC2.git && cd CSCI3104_GC2`
- `cd code`
- To run the program for **ALL `graphN.net` FILES** in order to generate all output files:
    - make sure `k` is between 3 and 8.
    - `python3 runAllNetworks.py k`
        - example: `python3 runAllNetworks.py 8`
    - Do `python3 runAllNetworks.py k write` if you want to write all subgraph occurences to the output files.
- `chmod 777 main.py`
- Before running the next commands, select a `k` between 3 and 8, and a valid `graphN.net` file from one of these files:
    - `graph1.net`
    - `graph2.net`
    - `graph3.net`
    - `graph4.net`
- `./main.py graphN.net k`
- `./main.py graphN.net k write` if you want a list of occurences of subgraphs in the network.
- The output file(s) are in `./code/outfiles/graphNoutput.txt`.

## Examples:
- `./main.py graph3.net 5`
    - counts how many isomorphisms of graphs up to 5  nodes occur in `graph3.net`.
- `./main.py graph3.net 8 write`
    - counts how many isomorphisms of graphs up to 8  nodes occur in `graph3.net` and writes the nodes that make up these isomorphisms into the text file.
    
## Further Reference:
- For more information on the Grochow-Kellis algorithm, check out:
- [Network Motif Discovery Using Subgraph Enumeration and Symmetry-Breaking](http://www.cs.colorado.edu/~jgrochow/Grochow_Kellis_RECOMB_07_Network_Motifs.pdf)
    - The original GK algorithm.
- [Network Motifs: Simple Building Blocks of Complex Networks](https://www.cs.cmu.edu/~ckingsf/bioinfo-lectures/netmotifs.pdf)
    - Carl Kingsford's CMU Bioinformatic Lecture that provides a high-level visual overview of GK algorithm.
- [NemoMap: Improved Motif-centric Network Motif Discovery Algorithm](https://www.astesj.com/publications/ASTESJ_030523.pdf)
    - An improvement upon GK algorithm called NemoMap.
 
