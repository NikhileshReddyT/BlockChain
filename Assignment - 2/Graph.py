#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd


# In[ ]:


tx = pd.read_table("tx.csv", header=None, names = ["txID", "blockID", "n_inputs", "n_outputs"])

txin_cols = ["txID", "input_seq", "prev_txID", "prev_output_seq", "addrID", "sum"]
txin = pd.read_table("txin.csv", header=None, names=txin_cols)

txout_cols = ["txID", "output_seq", "addrID", "sum"]
txout = pd.read_table("txout.csv", header=None, names=txout_cols)


# In[ ]:


txin_.groupby(['txID'], sort=False).agg({"addrID: list})


# In[ ]:


txin_group = txin[txin['txID'].isin(txIDs)].groupby("txID")
txout_group = txout[txout['txID'].isin(txIDs)].groupby('txID')


# In[ ]:


lists = []

# create list of lists by applying both joint and serial control
for txID in txIDs:
    inputs = txin[txin['txID'] == txID]['addrID'].values.tolist()
    outputs = txout[txout['txID'] == txID]['addrID'].values.tolist()
    
    # below code does both joint + serial
    x = inputs
    # joint control + serial control
    if len(outputs) == 1:
       x = (inputs + outputs) 
    else:
       for i in outputs:
         lists.append([i])
            
    lists.append(x)    


# In[ ]:


import networkx 
from networkx.algorithms.components.connected import connected_components


def to_graph(l):
    G = networkx.Graph()
    for part in l:
        # each sublist is a bunch of nodes
        G.add_nodes_from(part)
        # it also imlies a number of edges:
        G.add_edges_from(to_edges(part))
    return G

def to_edges(l):
    """ 
        treat `l` as a Graph and returns it's edges 
        to_edges(['a','b','c','d']) -> [(a,b), (b,c),(c,d)]
    """
    it = iter(l)
    last = next(it)

    for current in it:
        yield last, current
        last = current    


# In[ ]:


G = to_graph(lists)


# In[ ]:


#dump graph
#import pickle
#pickle.dump(G,open('g.txt', 'wb'))


# In[ ]:


cc = []
for i, value in connected_components(G):
    cc.append([i]+ list(value))


# In[ ]:


import  csv

with open("addresses_sccs.csv","w") as f:
    wr = csv.writer(f)
    wr.writerows(cc)

