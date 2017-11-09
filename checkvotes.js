Web3 = require('web3')
fs = require('fs');
solc = require('solc')

web3 = new Web3(new Web3.providers.HttpProvider("http://localhost:8545"));
web3.eth.defaultAccount = web3.eth.accounts[0];
web3.eth.accounts

code = fs.readFileSync('Voting.sol').toString()
compiledCode = solc.compile(code)

abiDefinition = JSON.parse(compiledCode.contracts[':Voting'].interface)

VotingContract = web3.eth.contract(abiDefinition)

console.log("loading contract at-" + process.argv[2])
contractInstance = VotingContract.at(process.argv[2]);

console.log("total votes for Rama-" + contractInstance.totalVotesFor.call('Rama').toLocaleString())
console.log("total votes for Nick-" + contractInstance.totalVotesFor.call('Nick').toLocaleString())
console.log("total votes for Jose-" + contractInstance.totalVotesFor.call('Jose').toLocaleString())
