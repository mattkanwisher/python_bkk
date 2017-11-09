Web3 = require('web3')
fs = require('fs');
solc = require('solc')
var sleep = require('sleep');

web3 = new Web3(new Web3.providers.HttpProvider("http://localhost:8545"));

code = fs.readFileSync('Voting.sol').toString()
compiledCode =  solc.compile(code)

abiDefinition = JSON.parse(compiledCode.contracts[':Voting'].interface)

VotingContract = web3.eth.contract(abiDefinition)

byteCode = compiledCode.contracts[':Voting'].bytecode

VotingContract.new(['Rama','Nick','Jose'],{data: byteCode, from: web3.eth.accounts[0], gas: 4700000}, function(err, deployedContract){
    if(!err) {
        if(!deployedContract.address) {
           console.log(deployedContract.transactionHash) // The hash of the transaction, which deploys the contract
       	   return
        } 
		console.log("total votes for Rama-" + deployedContract.totalVotesFor.call('Rama').toLocaleString())
		deployedContract.voteForCandidate('Rama', {from: web3.eth.accounts[0]})
		deployedContract.voteForCandidate('Rama', {from: web3.eth.accounts[0]})
		deployedContract.voteForCandidate('Rama', {from: web3.eth.accounts[0]})
		deployedContract.voteForCandidate('Rama', {from: web3.eth.accounts[0]})
		console.log("voted for Rama 4 times")
		console.log("total votes for Rama-" + deployedContract.totalVotesFor.call('Rama').toLocaleString())
		console.log("total votes for Nick-" + deployedContract.totalVotesFor.call('Nick').toLocaleString())
		console.log("total votes for Jose-" + deployedContract.totalVotesFor.call('Jose').toLocaleString())
		console.log("contractaddress-   " + deployedContract.address)
	} else {
		console.log(err);
	}
});
