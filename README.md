# GC2 Network Motifs in python

The output file is in `./code/outfiles/output.txt`

Make sure you have a version of python3 and you are on a linux or mac environment.

- template to run:
    - `cd code`
    - `chmod 777 main.py`
    - `./main.py graphN.net k`
    - `./main.py graphN.net k write` if you want a list of occurences of subgraphs
    - Enter a k between 3 and 8, and a valid graphN.net file from these files
        - `graph1.net`
        - `graph2.net`
        - `graph3.net`
        - `graph4.net`

- examples:
    - `./main.py graph3.net 5`
        - counts how many isomorphisms of graphs up to 5  nodes occur in graph3.net
    - `./main.py graph3.net 8 write`
        - counts how many isomorphisms of graphs up to 8  nodes occur in graph3.net and writes
        - the nodes that make up these isomorphisms into the text file