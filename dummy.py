source_code = 'contract MyToken {     address issuer;     mapping (address => uint) balances;      event Issue(address account, uint amount);     event Transfer(address from, address to, uint amount);      function MyToken() {         issuer = msg.sender;     }      function issue(address account, uint amount) {         if (msg.sender != issuer) throw;         balances[account] += amount;     }      function transfer(address to, uint amount) {         if (balances[msg.sender] < amount) throw;          balances[msg.sender] -= amount;         balances[to] += amount;          Transfer(msg.sender, to, amount);     }      function getBalance(address account) constant returns (uint) {         return balances[account];     } }'

from web3 import Web3  # The `web3.Web3` object is all you should need to import in most normal cases.
web3 = Web3(Web3.HTTPProvider('http://localhost:8545'))
#web3.personal.unlockAccount(web3.eth.accounts[0],"123456",1000)

from solc import compile_source
compile_sol = compile_source(source_code)

# If an `address` is not passed into this method it returns a contract factory class.
MyContract = web3.eth.contract(
    abi = compile_sol['<stdin>:MyToken']['abi'],
    bytecode = compile_sol['<stdin>:MyToken']['bin'],   # The keyword `code` has been deprecated.  You should use `bytecode` instead.
    bytecode_runtime = compile_sol['<stdin>:MyToken']['bin-runtime'],  # the keyword `code_runtime` has been deprecated.  You should use `bytecode_runtime` instead.
)

trans_hash = MyContract.deploy(transaction={'from':web3.eth.accounts[0],'gas':10000})
# wait for mining
#trans_receipt = web3.eth.getTransactionReceipt(trans_hash)
while c.eth_getTransactionReceipt(trans_hash) is None:
        time.sleep(1)

# get the contract address
contract_address = trans_receipt['contractAddress']
#contract_address = 'some_address_which_has_already_been_deployed_to'
console.log(contract_address)

# now we can instantiate the contract factory to get an instance of the contract.
#my_contract = MyContract(contract_address)

# now you should be able to call the contract methods.
#my_contract.call().getBalance(obj.eth.accounts[0])