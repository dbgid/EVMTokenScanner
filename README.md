# EVMTokenScanner

# Installation
```shell
git clone https://github.com/dbgid/EVMTokenScanner
cd EVMTokenScanner
python multichain.py -h
```

# Install Requirements
```shell
pip install requests colorama bs4
```

# Basic Usage
```shell
python multichain.py -c <chainID> -w <file of list wallet address>
```

# Info
This is first version, that currently just have a three EVM chain like: <strong>ETHEREUM, BINANCE SMART CHAIN and Polygon</strong>

this repository using grabing method, may if there in official website in thier element website update,
this repository can't work and need to be update.

# Feature
- get all token in your address wallet may some NFT are detected as token

# Disclaimer
This repo is not using threading, may the procces can take a while minutes different with how much in your file list wallet address.
Threading are useless bcoz detected as spam requests.
so in this version, I can't use it.
