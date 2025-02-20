### Create a Blockchain ###

# Import Libraries

import datetime
import hashlib
import json
import random
from flask import Flask, jsonify, render_template

### Build Blockchain

class Blockchain: 
    
    def __init__(self): 
        self.chain = []
        self.transactions_open = []
        self.create_block(proof = 1, previous_hash = '0')
        self.add_transaction('BlockMaster', 'Danny', 1000)
        
    def add_transaction(self, sender, recipient, amount):
        new_trans = {'sender': sender,
                     'amount': amount,
                     'recipient': recipient}
        self.transactions_open.append(new_trans)
        
    def create_block(self, proof, previous_hash):
        
        transactions = []
        loops = len(self.transactions_open)
        if loops > 5:
            loops = 5
        for i in range(loops):
            transactions.append(self.transactions_open[0])
            del self.transactions_open[0]
        
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'transactions': transactions,
                 'previous_hash': previous_hash}
        self.chain.append(block)
        return block
    
    def get_previous_block(self): 
        return self.chain[-1]
    
    def proof_of_work(self, previous_proof): 
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else: 
                new_proof += 1
        return new_proof
    
    def hash(self, block): 
        encoded_block = json.dumps(block, sort_keys = True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
    
    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False
            previous_block = block
            block_index += 1
        return True
    
    def print_blockchain(self, chain):
        print(json.dumps(chain, indent=4))
        
    

### Mine Blockchain

# Create Web App
app = Flask(__name__)

# Create Blockchain
blockchain = Blockchain()

#people available
people = ['John', 'Sam', 'Danny', 'Jeff', 'Sarah', 'Katherine', 'Mike', 'Nadia', 'Maria', 'Noah', 'Karen', 'Kevin', 'Joe', 'Justice', 'Brian', 'Shrisay', 'Calder']

#shown webpage
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

# Mine a new block
@app.route('/mine_block', methods = ['GET'])
def mine_block():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash)
    response = {'message': 'Congratulations, you just mined a block!',
                'index': block['index'],
                'timestamp': block['timestamp'],
                'transactions': block['transactions'],
                'proof': block['proof'],
                'previous_hash': block['previous_hash']}
    
    for i in range(random.randint(1,8)):
        send = ''
        receive = ''
        while send == receive:
            send = random.choice(people)
            receive = random.choice(people)
        
        blockchain.add_transaction(send, receive, random.randint(1,100))
    
    return jsonify(response), 200

# Get a full blockchain
@app.route('/get_chain', methods = ['GET'])
def get_chain():
    response = {'chain': blockchain.chain,
                'length': len(blockchain.chain)}
    blockchain.print_blockchain(blockchain.chain)
    
    return jsonify(response), 200

# Confirm chain is valid
@app.route('/confirm_chain', methods = ['GET'])
def confirm_chain():
    response = {'valid': blockchain.is_chain_valid(blockchain.chain)}
    return jsonify(response), 200

# Run app
app.run(host = '0.0.0.0', port = 5001)
