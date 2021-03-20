# HW1: Building Dapp

## February 12, 2020

## 1 Introduction

The assignment is to develop a smart contract on Ethereum.
We will be using the Truffle framework as a development environment. Truffle is
a framework for building, testing, and deploying applications on the Ethereum
network. The Truffle Framework consists of three primary development frame-
works for Ethereum smart contract and decentralized application (dApp) devel-
opment called Truffle, Ganache, and Drizzle. However, for this assignment, we
only need Truffle and Ganache. To get started with developing a smart contract,we use Solidity - An object-oriented programming language.
for writing Ethereum’s smart contracts. I’d recommend reading this tutorial
https://www.trufflesuite.com/tutorials/pet-shop (don’t need to get
to the part of creating a user interface).

The goal of this assignment is to develop a smart contract for open auction. The
general idea of the auction contract is that everyone can send their bids during
a bidding period. The bids already include sending money / ether in order to
bind the bidders to their bid. If the highest bid is raised, the previously highest
bidder gets their money back. After the end of the bidding period, the contract
will be called manually for the beneficiary to receive their money.

## 2 Setting up the workspace

Requirements
```
1. NodeJS v8.9.4 or later
2. Windows, Linux or Mac OS X

```
**Install Truffle:** Truffle is made for building dApps using the Ethereum Virtual
Machine (EVM) by providing a development environment, testing framework
and asset pipeline. To install, run the following command:
```
npm install −g truffle

```
On a Unix-based system, add "sudo" before the command.
Verify the installation by running "truffle version" on a terminal, output should be similar to the following:
```
T ru f fl e v5. 1. 1 2 ( core : 5. 1. 1 2 )
S o l i d i t y v0. 5. 1 6 ( solc−j s )
Node v8. 1 0. 0
Web3. j s v1. 2. 1

```
**Install Ganache:** Ganache is a personal blockchain that allows developers to
create smart contracts, dApps, and test software that is available as a desktop
application and command-line tool for Windows, Mac, and Linux. To install, fol-
low the instructions on https://www.trufflesuite.com/docs/ganache/quickstart
```
Version: 2.1.2
```
## 3 Writing the smart contract

The source code is provided. The directory containing the
file "truffle-config.js" will be referred as the root directory. After compiling the source code successfully, open a terminal in the root directory and run
the following command:

```
truffle compile
```

## 4 Deploy the contract on Ganache

Start the Ganache software and run the following command in the root directory:

```
truffle migrate
```
By default, Ganache provides 10 Ethereum accounts, each has 100 ETH, to
interact with the smart contract. The first account is the one deploying the
contract and becomes the beneficiary (see the constructor in the source code).

We can interact with our contract using Truffle console. From the root directory, run:

```
truffle console
```
We can make calls or create transactions to the smart contract with some
simple Javascript commands and can find the instructions here: https://www.trufflesuite.com/docs/truffle/getting-started/interacting-with-your-contracts

Report the amount of gas or transaction fee for the following
tasks:

1. Deploying the contract.
2. Triggering each of the implemented functions.


## 5 Report

The report containes the following:

- Brief explanation for each function written and how it works along with deplaying some experiments on sending/withdrawing bids to show
    that the contract works correctly.
- The amount of gas or transaction fee needed to deploy the contract and
    trigger each of the implemented functions. Attached somescreenshots
    showing how those numbers are obtained.
- A screenshot from *Truffle console* showing that the beneficiary account
    has received the money after "auctionEnd" is triggered along with showing the
    change in the beneficiary account balance before and after the function is
    triggered. The change reflects the actual amount of the highest bid
    minus the transaction fee (Calculations Shown).
