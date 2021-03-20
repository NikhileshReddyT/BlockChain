# Exploring Bitcoin Transactions

## March 23, 2020

## 1. Introduction

In this assignment, we conduct some data analysis on Bitcoin transactions.
We specifically draw on our knowledge of the blockchain structure and deanonymization techniques and use Bitcoin dataset from https://senseable2015-6.mit.edu/bitcoin/

Before getting into this assignment, Review the Bitcoin technical guide:

https://bitcoin.org/en/blockchain-guideandhttps://bitcoin.org/en/transactions-guide to familiarize with Bitcoin transactions. In
particular, understand the following:

- Structure of the transaction: inputs, outputs, value. Pay attention on how
    a transaction relates to previous transactions.
- Bitcoin addresses
- Unspent transaction output (UTXO).
- Coinbase transaction.

Simply speaking, each Bitcoin transaction may have multiple inputs and outputs
where each output is assigned with credits and locked to a Bitcoin address. This
newly created transaction output is referred to as a UTXO. The UTXOs may
then be used as inputs of another transaction, and after this transaction is
committed to a block, those UTXOs will be marked asspentand cannot be
used again (to prevent double-spending). Coinbase transactions are rewards for
mining Bitcoin blocks, and they don’t have any inputs. Each Bitcoin address
is a string of 26-35 alphanumeric characters, beginning with the number 1, 3 or
bc1.


## Part 1: Transactions analysis

We provide answers to these following questions:

1. What is the number of transactions and addresses in the dataset?
2. What is the Bitcoin address that is holding the greatest amount of bitcoins? How much is that exactly? Note that the address here must be
    a valid Bitcoin address string. To answer this, you need to calculate the
    balance of each address. The balance here is the total amount of bitcoins
    in the UTXOs of an address.
3. What is the average balance per address?
4. What is the average number of input and output transactions per address?
    What is the average number of transactions per address (including both
    inputs and outputs)? An output transaction of an address is the transaction that is originated from that address. Likewise, an input transaction
    of an address is the transaction that sends bitcoins to that address.
5. What is the transaction that has the greatest number of inputs? How
    many inputs exactly? Show the hash of that transaction. If there are
    multiple transactions that have the same greatest number of inputs, show
    all of them.
6. What is the average transaction value? Transaction value is the sum of
    all outputs’ value.
7. How many coinbase transactions are there in the dataset?
8. What is the average number of transactions per block?

```
Note: The bitcoin value is in Satoshi and not BTC.
```

## Part 2: Address De-anonymization

In Bitcoin, a user may possess multiple addresses. In this part, we will apply a
simple heuristic to infer the Bitcoin users owning those addresses. The heuristic
consists of two phases:

1. Joint control: assume that all input addresses of a transaction are controlled by the same user.


2. Serial control: assume that the output address of a transaction with only
    a single output is controlled by the same user owning the input addresses.

We implement this heuristic on the dataset by applying both Joint control and
Serial control, then we answer the following questions. 
```
Note: In the dataset that we use, the fileaddr_sccs.dat.gz only applies the Joint control, that
means it CANNOT be used for this part).
```
1. How many users are there in the dataset?
2. We answer questions 2, 3, and 4 in part 1 by replacing "address" with "user".
    Note that each user is identified by the addresses that are owned by
    him/her. Thus, in answering question 2 (i.e., the user who is holding
    the greatest amount of bitcoins), we list all the user’s addresses.
3. Give the hash of the transaction sending the greatest number of bitcoins
    to the user who is holding the greatest balance.

## 2 Deliverable

Report includes the following:

- Answers to each of the above mentioned questions.
- Instructions on how to run your code to obtain those answers.
