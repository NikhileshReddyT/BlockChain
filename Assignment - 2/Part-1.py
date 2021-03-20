#!/usr/bin/env python
# coding: utf-8

import pandas as pd

bh_cols = ['blockID', 'hash', 'block_timestamp', 'n_txs']
bh = pd.read_table("bh.csv", header=None, names=bh_cols)

txh = pd.read_table("txh.csv", header=None, names = ["txID", "hash"])
addr = pd.read_table("addresses.csv", header=None, names = ["addrID", "address"])

txin_col = ["txID", "input_seq", "prev_txID", "prev_output_seq", "addrID", "sum"]
txin = pd.read_table("txin.csv", header=None, names=txin_col)

txout_col = ["txID", "output_seq", "addrID", "sum"]
txout = pd.read_table("txout.csv", header=None, names=txout_col)

txin_group = txin.groupby("addrID",as_index=False).agg({"sum":["sum", "count"]})
txout_group = txout.groupby("addrID",as_index=False).agg({"sum":["sum", "count"]})

bal = pd.merge(txin_group[1:], txout_group[1:], on="addrID",how="outer")
bal = bal.fillna(0)
bal["balance"] = bal["sum_y"]["sum_y"] - bal["sum_x"]["sum_x"]

bal.sort_values("balance", ascending=False, inplace=True)
txh = pd.read_table("txh.csv", header=None, names = ["txID", "hash"])

tx = pd.read_table("tx.csv", header=None, names = ["txID", "blockID", "n_inputs", "n_outputs"])
max = tx[tx["n_inputs"] == tx["n_inputs"].max()][["txID", "n_inputs"]]
display(max)
max_inp = max["n_inputs"].values[0]
max_txID = max["txID"].values[0]
max_hash = txh[txh["txID"] == max_txID]["hash"].values[0]

avg_input = txin_group["sum"]["count"].sum()/8385065
avg_output = txout_group["sum"]["count"].sum()/8385065
bal["total_txs"] = bal["sum_x"]["count"] + bal["sum_y"]["count"]
avg_input_output = bal["total_txs"].mean()

print("1. The Number of transactions in the dataset are: " + str(bh["n_txs"].sum()) + ", and the total number of addresses in the dataset are: " + str(len(addr)))
print()
print("2. The Bitcoin address holding the greatest amount of bitcoins is " + str(addr.loc[1083442]["address"]) + " and the amount  it is holding: " + str(bal["balance"].max()))
print()
print("3. Average balance per address : " + str(bal["balance"].mean()))
print()
print("4. The Avg number of input and output txs per address: " + str(avg_input) + " , " + str(avg_output) + " respectively.")
print("And the avg number of txs(input + output) per address: " + str(avg_input_output))
print()
print("5. The transaction that has the greatest number of inputs is " + max_hash + " and it has " + str(max_inp) + " inputs")
print()
print("6. Average transaction value is: " + str(txout["sum"].sum()/len(txout['txID'].unique())))
print()
print("7. Number of coinbase transactions in the dataset are: " + str(len(bh)))
print()
print("8. Average transactions per block is: " + str(str(bh["n_txs"].mean())))
