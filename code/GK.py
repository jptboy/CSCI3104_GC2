#!/usr/bin/env python3
# Familiarize yourself with this adjacency list
# or dictionary representation of a graph
Gf = {
    0: set([1,2,3]),
    1: set([0,2]),
    2: set([0,1,3]),
    3: set([0,2])
}
 
Hf = {
    0: set([1,2]),
    1: set([0,2]),
    2: set([0,1]),
}
def validiso(f,G,H,m,u):
    '''
    This tests if f will remain a valid isomorphic function
    if the m->u pair is added to f by checking

    if two nodes in the domain of f are neighbors in H
    these nodes partners in f should also be neighbors in G.

    We only want to deal with the nodes in the domain of f
    for H and the nodes that are in the range of f for G.

    If two nodes in the domain of f are neighbors and
    they aren't neighbors in G then the isomorphism isn't
    valid and we return false.
    '''
    if len(G[u]) < len(H[m]):
        # If u can't support m f can't be a valid
        # isomorphism.
        return False
    else:
        # generate a copy of f to test things with
        copyf = {k:f[k] for k in f}
        # add m->u to the copy of f
        copyf[m] = u
        # see if u is already in the range of f,
        # and if it is return false
        setvals = set([f[k] for k in f])
        if u in setvals:
            return False
        else:
            '''
            let HV' = f_domain.intersection(H.nodes)
            let HE' = 
                (the edges between nodes in HV').
                intersection(H.edges)

            let H' = a Graph(HV',HE')

            let GV' = f_range.intersection(G.nodes)
            let GE' = 
                (the edges between nodes in GV').
                intersection(G.edges)

            let G' = a Graph(GV',GE')

            What we check is if two nodes are neighbors in
            H' they are also neighbors in G' to check
            if f will be a valid isomorphism if the m->u
            pair is added.
            '''
            el = []
            keys = set(copyf.keys())
            # keys is the domain of f
            for node in keys:
                # get the intersection of keys and
                # the vertices of H
                adjs = H[node].intersection(keys)
                # generate the HE' edgelist
                # necessary
                for adjNode in adjs:
                    el.append([node,adjNode])
            '''
            For all the edges in HE'
            the nodes in those edges are neighbors
            since HE' is a edgelist.
            Check if those nodes partners from f
            are also neighbors in G, and if they aren't
            return False.
            '''
            for tup in el:
                HNode = tup[0]
                HNeigh = tup[1]
                # f[firstnodeinedgelist]
                GNode = copyf[HNode]
                # f[secondnode in edgelist]
                GNeigh = copyf[HNeigh]
                '''
                Since HNode and HNeigh are neighbors
                check if GNeigh and GNode have a edge
                and if they don't return False.
                '''
                if not GNeigh in G[GNode]:
                    return False
            return True
def chooseNode(f,H):
    '''
    Returns the node in H that has the most neighbors
    already in the mapping 
    f: Verticles from H ->  Vertices in G.

    Don't worry about this function, just a deterministic
    way to select a node. It isn't really important.
    '''
    def sortFunc(node):
        c = 0
        for x in H[node]:
            if x in f:
                c += 1
        return c
    nodes = set(H.keys()).difference(set(f.keys()))
    nodes = list(nodes)
    nodes = sorted(nodes, key = sortFunc)
    return nodes[-1]
def extend(f,G,H):
    isos = []
    f_domain = set(f.keys())
    # If the domain of the partial map passed is
    # the same as the domain of H, we have a full mapping
    # and we can return. This is the base case
    if f_domain == set(H.keys()):
        return [{k:f[k] for k in f}]

    # Otherwise we choose some node in H that isn't
    # in the domain of f. A node not in the mappings
    # domain yet.
    m = chooseNode(f,H)
    vals = set([f[k] for k in f])

    # We find the nodes in the co-domain of the mapping
    # that arent in the range.
    notMappedTo = set(G.keys()).difference(vals)

    # For all possible m -> u that we 
    # can add to the mapping we check if that
    # would keep the mapping as a valid isomorphism
    # and if it does we add that m->u pair to the mapping
    # and recurisively call extend and try to extend
    # the current mapping with the m-> pair added to it.
    for u in notMappedTo:
        valid_isoflag = validiso(f,G,H,m,u)
        if valid_isoflag:
            f[m] = u
            call = extend(f,G,H)
            isos = isos + call
    return isos
def GK(G,H):
    occs = []
    copyG = {k:G[k] for k in G}
    '''
    For every possible mapping starting
    with  a single node in G to a single node in H, 
    we try to extend that mapping every way possible.

    g is some node in G and h is some node in H

    So for every g and h combination, we 
    try to grow that partial map everyway possible
    with the extend sub-routine and get full maps 
    that are isomorphic functions from G to H.
    '''
    # For every g in a deepcopy of G
    for g in copyG:
        # For every h in H
        for h in H:
            # If the degree of g is less than H
            # We cant have a mapping started, since
            # g cant support H.
            if(len(G[g]) < len(H[h])):
                continue
            else:
                # Otherwise we start a partial map and
                # extend the partial map
                f = {}
                # f: Verticles from H ->  Vertices in G
                f[h] = g
                l = extend(f,G,H)
                # for all extensions of the partial map
                # These extensions will be full maps
                # we add these extensions to the occurences
                # list
                for q in l:
                    occs.append(q)
    return occs
def checkDegrees(gmap,G,H):
    '''
    We want to generate a induced subgraph copyG
    based on only the nodes that are in the range of the
    mapping gmap.

    We compare the degrees of the nodes in H
    and the nodes in copyG to see if copyG is a isomorphism
    of H and we return true if it is.
    '''
    # Generate range of mapping
    gmap_vals = set([gmap[k] for k in gmap])

    # Generate a induced subgraph of G based on only the
    # nodes in the range of the mapping
    copyG = {k: set([v for v in G[k]]) for k in gmap_vals}

    # Make sure each node in the induced subgraph is
    # only mapped to other nodes in the range of the mapping
    # so its not mapped to nodes that aren't in the range
    # of the mapping
    for k in copyG:
        copyG[k] = copyG[k].intersection(gmap_vals)

    # If the degree of any node in the query graph is
    # different than the degree of any node in the induced
    # subgraph we return false, since this means we 
    # could have done something like map a triangle without
    # one side onto a full triangle.
    for k in gmap:
        v = gmap[k]
        if len(H[k]) != len(copyG[v]):
            return False
    # If all the degrees are equal then
    # we have ourselves an isomorphism and return true.
    return True
def subGraphOccurences(G,H):
    '''
    H is small query-graph and G is big graph/network.

    Finds the number of occurences of isomorphisms of 
    H in G and it returns a list of mappings between
    vertices in H to G.
    
    For the input:

    G: 0 <-> 1 <-> 2 
    H: 0 <-> 1

    If the algorithm returned (2,[{0:1,1:0},{0:2,1:1}])
    
    This would mean that this algorithm found 2 matching 
    isomorphisms of H in G. H is a 2 vertex Graph. The first
    mapping was the 0th vertex in H mapped to the 1st
    vertex in G, and the 1st vertex in H mapped to the 0th
    vertex in G. The second mapping was the 0th vertex in H
    mapped to the 2nd vertex in G, and the 1st vertex in H
    mapped to the 1st vertex in G.
    '''
    if len(H) > len(G):
        '''
        If H has more vertices than G,
        obviously H has no isomorphisms occuring in G
        since H is a bigger graph than G.
        '''
        # Therefore we reutrn 0 isomorphisms, and
        # a empty list of mappings
        return 0,[]
    else:
        # We create a copy of G because G is mutable
        # and passed by reference and we don't want the
        # original input to be mutated by the algorithm.

        # The dictionary comprehension you see below
        # creates a deep copy of the dictionary by copying
        # its keys and values by value and not reference.
        # Think about what it is doing and the structure of
        # dictionary based graphs in python.

        # You can see examples of dictionary based graphs at
        # the top of this file with Gf and Hf.
        copyG = {k:set([x for x in G[k]]) for k in G}

        # We get all possible mappings from the Grochow-Kellis
        # algorithm which takes our deepcopy of G and our query
        # graph H

        '''
        Some of these mappings end up having the same range
        with the co-domain and range of the mapping being
        the noes in G. The next for loop generates uniqs
        which is unique mappings that aren't the same.

        For example if one mapping has nodes 0,1,2 in its
        range and another mapping has 2,0,1 in its range,
        than regardless of the ordering of the mappings
        we will only include one of the mappings.
        '''

        # Occs will be in the format [mapping1,mapping2]
        # mappings will be like:
        # {HNode: GNode, HNode1: GNode1,...}
        # like {0:1,1:0,...}
        occs = GK(copyG,H)
        uniqs = []
        uniqset = set()
        for d in occs:
            # We sort the values in the returned map
            # so 213 and 321 both turn into 123
            # we turn this into a string and hash it
            # we only insert a mapping from occs into uniqs
            # if the range of the mapping isn't already
            # in the hashed set
            vals  = [d[k] for k in d]
            vals = sorted(vals)
            vals = list(map(str,vals))
            hash_key = "".join(vals)
            if not hash_key in uniqset:
                uniqset.add(hash_key)
                uniqs.append(d)
        '''
        The next for loops job is to prevent.
        a graph like
        {
            0: set([1,2]),
            1: set([0]),
            2: set([1])
        }

        from being mapped onto a graph like
        {
            0: set([1,2]),
            1: set([0,2]),
            2: set([0,1]),
        }

        since the latter graph is a triangle
        whereas the first graph is a triangle with a side
        removed. The second graph isn't actually an 
        isomorphism of the first.

        The list good will just be comprised of mappings
        that adhere to this rule.
        '''
        good = []
        for agraph in uniqs:
            # we check if each mapping in G, H
            # is actually a real isomorphism
            if checkDegrees(agraph,G,H):
                good.append(agraph)
        return len(good),good
tests = [
    (
        [[0,1], [1,2], [0,2]],[[0,1], [1,2], [0,2]], 1
    ),
    (
        [[0,1], [1,2], [0,2]], [[1,2], [2,3], [1,3], [0,1]], 1
    ),
    (
        [[1,2], [2,3], [1,3], [0,1]], [[0,1], [1,2], [0,2]], 0
    ),
    (
        [[0,1], [0,2], [1,2], [0,3]], [[1,2], [2,3], [1,3], [0,1]], 1
    ),
    (
        [[0,1], [1,2], [0,2]], [[0,1], [1,2], [2,3], [3,0], [0,2]], 2
    ),
    (
        [[0,1], [1,2], [2, 3], [3,0]], [[0,1], [1,2], [2,3], [3,0], [0,2]], 0
    ),
    (
        [[0,1], [1,2], [2, 3], [3,0]], [[1,0], [0,2], [2, 3], [3,1]], 1
    ),
    (
        [[0,1], [1,2], [2,3], [3,0], [0,2]], [[0,3], [3,1], [3,2], [2,1], [1,0]], 1
    ),
    (
        [[0,1], [1,2], [0,2]], [[1,2], [1,4], [1,6], [1,7], [2,6], [3,4], [3,8], [3,9], [4,5], [4,6], [4,8], [5,6], [5,0], [6,8], [6,9]], 5
    ),
    (
        [[0,1], [0,2], [1,2], [0,3]], [[1,2], [1,4], [1,6], [1,7], [2,6], [3,4], [3,8], [3,9], [4,5], [4,6], [4,8], [5,6], [5,0], [6,8], [6,9]], 16
    ),
    (
        [[1,2], [2,3], [3,4], [3,5], [4,2], [4,5], [5,0]],[[0,5], [5,4], [4,3], [4,2], [3,5], [3,2], [2,1]],1
    ),
    (
        [[1,2], [2,3], [3,4], [3,5], [4,2], [4,5], [5,0]], [[1,0], [2,3], [3,4], [3,5], [4,2], [4,5], [5,2]], 0
    ),
    (
        [[0,5], [5,4], [4,3], [4,2], [3,5], [3,2], [2,1]], [[1,0], [2,3], [3,4], [3,5], [4,2], [4,5], [5,2]], 0
    ),
]
def convertElToDictGraph(el):
    '''
    Takes in a edge list in the format [[0,1],[1,2]]
    and outputs a dictionary/adjacency list
    style dictionary like
    {
        0 : set([1])
        1 : set([0,2])
        2 : set([1])
    }
    '''
    dgraph = {}
    for tup in el:
        b,e = tup
        if not (b in dgraph):
            dgraph[b] = set([e])
            if not (e in dgraph):
                dgraph[e] = set([b])
            else:
                dgraph[e].add(b)
        else:
            dgraph[b].add(e)
            if not(e in dgraph):
                dgraph[e] = set([b])
            else:
                dgraph[e].add(b)
    return dgraph

def tester():
    for idx,test in enumerate(tests):
        H = convertElToDictGraph(test[0])
        G = convertElToDictGraph(test[1])
        copies = test[2]
        lens, gmap = subGraphOccurences(G,H)
        assert(lens == copies)
