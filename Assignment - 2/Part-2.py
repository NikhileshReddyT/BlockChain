#!/usr/bin/env python
# coding: utf-8
import pandas as pd
addr_sccs = pd.read_table('addr_sccs_joint_serial.csv', header=None, names=['addrID', 'userID'])

addr = pd.read_table("addresses.csv", header=None, names=["addrID", "address"])

txin_cols = ["txID", "input_seq", "prev_txID", "prev_output_seq", "addrID", "sum"]
txin_ = pd.read_table("txin.csv", header=None, names=txin_cols)

txout_cols = ["txID", "output_seq", "addrID", "sum"]
txout_ = pd.read_table("txout.csv", header=None, names=txout_cols)

txin = pd.merge(txin_, addr_sccs, how="inner", on='addrID')
txout = pd.merge(txout_, addr_sccs, how="inner", on='addrID')

txin_group = txin.groupby("userID",as_index=False).agg({"sum":["sum", "count"]})
txout_group = txout.groupby("userID",as_index=False).agg({"sum":["sum", "count"]})

bal = pd.merge(txin_group[1:], txout_group[1:], on="userID",how="outer")

bal = bal.fillna(0)

bal["balance"] = bal["sum_y"]["sum_y"] - bal["sum_x"]["sum_x"]
bal.sort_values("balance", ascending=False, inplace=True)
max_balance_user_addresses= addr_sccs[addr_sccs['userID'] == 12461805]['addrID'].values
num_users = len(addr_sccs['userID'].unique())
print("Q1 number of users: " + str(num_users))
print("Q2 Max balance: " + str(bal["balance"].max()))
print("Q3 Average balance per user : " + str(bal["balance"].mean()))

print("Q4 : avg input , output txs per user:")

txin_group["sum"]["count"].sum()/num_users, txout_group["sum"]["count"].sum()/num_users

bal["total_txs"] = bal["sum_x"]["count"] + bal["sum_y"]["count"]
print("Q4 : avg txs(input + output) per user: " + str(bal["total_txs"].mean()))
del addr
del txin
del txout
del txout_group
del bal
