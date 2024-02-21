import datetime
import hashlib
import json
from flask import Flask, jsonify, request
import requests
from uuid import uuid4
from urllib.parse import urlparse
import argparse


class Blockchain:
    def __init__(self):
        self.chain = []
        self.transactions = []
        self.transactions.append({'sender': "origin",
                                    'receiver': "Danny",
                                    'amount': 100000})
        self.create_block(proof=1, previous_hash='0')
        self.nodes = set()

    def create_block(self, proof, previous_hash):
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash,
                 'transactions': self.transactions}
        self.transactions = []
        self.chain.append(block)
        return block

    def get_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(
                str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
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
            hash_operation = hashlib.sha256(
                str(proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False
            previous_block = block
            block_index += 1
        return True

    def add_transaction(self, sender, receiver, amount):
        senderamt = 0
        for block in self.chain:
            curr_trans = block["transactions"]
            for trans in curr_trans:
                curr_send = trans["sender"]
                curr_rec = trans["receiver"]
                if curr_send == sender:
                    senderamt -= trans["amount"]
                elif curr_rec == sender:
                    senderamt += trans["amount"]

        if amount <= senderamt:
            self.transactions.append({'sender': sender,
                                    'receiver': receiver,
                                    'amount': amount})
            previous_block = self.get_previous_block()
            return previous_block['index'] + 1
        else:
            return 0

    def add_node(self, address):
        parsed_url = urlparse(address)
        self.nodes.add(parsed_url.netloc)

    def replace_chain(self):
        network = list(self.nodes)
        print(network)
        longest_chain = self.chain
        max_length = len(self.chain)
        long_is_unique = True
        port = request.host
        network.remove(str(port))
        for node in network:
            response = requests.get(f'http://{node}/get_chain')
            if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain']
                if length > max_length and self.is_chain_valid(chain):
                    print(f"length>max on {node}")
                    max_length = length
                    longest_chain = chain
                    long_is_unique = True
                elif length == max_length:
                    if self.chain == chain:
                        print(f"are equal on {node}")
                        long_is_unique = False
        if longest_chain != self.chain and long_is_unique:
            self.chain = longest_chain
        print("LONGISUNIQUE: " + str(long_is_unique))
        if long_is_unique:
            return True
        return False


# Creating a Web App
app = Flask(__name__)

# Creating an address for the node on Port 5000
node_address = str(uuid4()).replace('-', '')

# Creating a Blockchain
blockchain = Blockchain()


@app.route('/mine_block', methods=['GET'])
# Mining a new block
def mine_block():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    #blockchain.add_transaction(
     #   sender=node_address, receiver='monty', amount=1)
    block = blockchain.create_block(proof, previous_hash)
    response = {'message': 'Congratulations, you just mined a block!',
                'index': block['index'],
                'timestamp': block['timestamp'],
                'proof': block['proof'],
                'previous_hash': block['previous_hash'],
                'transactions': block['transactions']}
    return jsonify(response), 200


@app.route('/get_chain', methods=['GET'])
# Getting the full Blockchain
def get_chain():
    response = {'chain': blockchain.chain,
                'length': len(blockchain.chain)}
    return jsonify(response), 200


@app.route('/confirm_chain', methods=['GET'])
# Checking if the Blockchain is valid
def is_valid():
    is_valid = blockchain.is_chain_valid(blockchain.chain)
    if is_valid:
        response = {'message': 'All good. The Blockchain is valid.'}
    else:
        response = {
            'message': 'Houston, we have a problem. The Blockchain is not valid.'}
    return jsonify(response), 200


@app.route('/add_transaction', methods=['POST'])
# Adding a new transaction to the Blockchain
def add_transaction():
    json = request.get_json()
    transaction_keys = ['sender', 'receiver', 'amount']
    if not all(key in json for key in transaction_keys):
        return 'Some elements of the transaction are missing', 400
    index = blockchain.add_transaction(
        json['sender'], json['receiver'], json['amount'])
    if index != 0:
        response = {'message': f'This transaction will be added to Block {index}'}
    else:
        response = {'message': 'insufficient funds'}
    return jsonify(response), 201


@app.route('/connect_node', methods=['POST'])
# Connecting new nodes
def connect_node():
    json = request.get_json()
    nodes = json.get('nodes')
    port = request.host
    if nodes is None:
        return "No node", 400
    for node in nodes:
        blockchain.add_node(node)
    nodes_new = nodes.copy()
    nodes_new.remove("http://"+str(port))
    for n in nodes_new:
        response = requests.post(f'{n}/connect_node_secret', json={"nodes": nodes})
    response = {'message': 'All the nodes are now connected. The Montycoin Blockchain now contains the following nodes:',
                'total_nodes': list(blockchain.nodes)}
    return jsonify(response), 201


@app.route('/connect_node_secret', methods=['POST'])
def connect_node_secret():
    json = request.get_json()
    nodes = json.get('nodes')
    port = request.host
    if nodes is None:
        return "No node", 400
    for node in nodes:
        blockchain.add_node(node)
    response = {'message': 'All the nodes are now connected. The Montycoin Blockchain now contains the following nodes:',
                'total_nodes': list(blockchain.nodes)}
    return jsonify(response), 201

@app.route('/replace_chain', methods=['GET'])
# Replacing the chain by the longest chain if needed
def replace_chain():
    is_chain_replaced = blockchain.replace_chain()
    if is_chain_replaced:
        nodes = blockchain.nodes
        print("THE NODES ARE: " + str(nodes))
        port = request.host
        nodes.remove(str(port))
        for n in nodes:
            resp = requests.post(f'http://{n}/prop_chain', json={"chain": blockchain.chain})
        response = {'message': 'Propogated correct chain',
                    'new_chain': blockchain.chain}
    else:
        response = {'message': 'Chain still working',
                    'chain': blockchain.chain}
    return jsonify(response), 200

@app.route('/prop_chain', methods=['POST'])
def prop_chain():
    json = request.get_json()
    chain = json.get("chain")
    blockchain.chain = chain
    response = {"message": "Done!"}
    return jsonify(response), 200


parser = argparse.ArgumentParser()
parser.add_argument('--port', type=int, default=5000, help='port to listen on')
args = parser.parse_args()

# Running the app
app.run(host='0.0.0.0', port=args.port)
