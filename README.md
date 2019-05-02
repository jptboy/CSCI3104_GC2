# GC2 Network Motifs in python

The output file is in code/outfiles/output.txt

- template to run:
    - `cd code`
    - `./main.py graphN.net k`
    - `./main.py graphN.net k write` if you want a list of occurences of subgraphs

- examples:
    - `./main.py graph3.net 5`
        - counts how many isomorphisms of graphs up to 5  nodes occur in graph3.net
    - `./main.py graph3.net 8 write`
        - counts how many isomorphisms of graphs up to 8  nodes occur in graph3.net and writes
        - the nodes that make up these isomorphisms into the text file