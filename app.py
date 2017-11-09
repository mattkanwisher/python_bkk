import sys, os, time
from solc import compile_source, compile_files, link_code

from web3 import Web3, HTTPProvider, IPCProvider
print("Using environment in "+sys.prefix)
print("Python version "+sys.version)

web3 = Web3(HTTPProvider('http://localhost:8545'))

compiled = compile_files(['Voting.sol'])

abi = compiled['Voting.sol:Voting']['abi'],
bytecode = compiledCode #compiled['Voting.sol:Voting']['bin'], 
compiledCode = '0x'+compiled['Voting.sol:Voting']['bin'] # This is a hack which makes the system work
compiledCode = '0x'+compiled['Voting.sol:Voting']['bin'] # This is a hack which makes the system work
bytecode_runtime = compiled['Voting.sol:Voting']['bin-runtime']
contract = web3.eth.contract(abi, bytecode=compiledCode, bytecode_runtime: )
transHash = contract.deploy(transaction={'from':web3.eth.accounts[0],'value':120})


myContract = web3.eth.contract(
    bytecode_runtime = compiled['Voting.sol:Voting']['bin-runtime'],
)


# Put the contract in the pool for mining, with a gas reward for processing
#contractTx = web3.eth.contract(web3.eth.coinbase, bytecode=compiledCode, gas=300000)
print("Contract transaction id is "+contractTx)

print("Waiting for the contract to be mined into the blockchain...")
while c.eth_getTransactionReceipt(contractTx) is None:
        time.sleep(1)


contractAddr = c.get_contract_address(contractTx)
print("Contract address is "+contractAddr)

# There is no cost or delay for reading the state of the blockchain, as this is held on our node
results = c.call(contractAddr, 'get_s()', [], ['string'])
print("The message reads: '"+results[0]+"'")


# Send a transaction to interact with the contract
#   We are targeting the set_s() function, which accepts 1 argument (a string)
#   In the contact definition, this was   function set_s(string new_s){s = new_s;}
params = ['Hello, fair parishioner!']
tx = c.call_with_transaction(c.eth_coinbase(), contractAddr, 'set_s(string)', params)

print("Sending these parameters to the function: "+str(params))
print("Waiting for the state changes to be mined and take effect...")
while c.eth_getTransactionReceipt(tx) is None:
    time.sleep(1)

results = c.call(contractAddr, 'get_s()', [], ['string'])
print("The message now reads '"+results[0]+"'")