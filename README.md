<<<<<<< HEAD
What features and functionality did you add to your blockchain? Why? 

The 2 main features that I added to my blockchain are the randomly created transaction pool to be part of the blocks and a UI that can be used to make the server calls. Everytime a block is mined, a random amount of transactions which have a random sender name, receiver name, and amount, and added to a transaction pool. Then, when a block gets mined, up to 5 of the transactions from the pool are added to the block in a transactions array. Then, I made a UI with three buttons, one for each of the three server calls, that initially printed the result to the console. Then, I made it so that when you mine a block, it displays the data of the mined block in a blokc shown on the UI. Also, I made it so that whenever the validate chain button is clicked, it will show underneath whether or not the blockchain is valid. I made the first change because I felt that a blockchain that did not have any data held in its blocks did not make much sense, so I wanted some transactions to be added to the blocks. I made the second change because I wanted some way to make the calls without postman and also have a better way to show the data besides just some json.


Explanation of what a class is in Python/Object-Oriented Programming

A class is something that defines an object/data type that can be used later to hold values and run functions. A class can be instantiated to use all of its functionality that gets saved to some variable name. This variable will be of the type of the class and every version of that class has the same functionality.


What is an endpoint? What is a server? What is Flask? What is Postman doing? 

An endpoint is a certain url that can be called which will return some data to wherever it is being called from. A server is something on the internet which is able to deliver data when its endpoints are called. Flask is a python library that enables the creation of servers through one's own computer. Postman is calling the endpoints on the server and displaying the data it receives back.


What you intended to do vs. what you actually completed. What challenges did you face? 

Originally, on the UI side, I intended to add a visual representation of the entire blockchain so far whenever the get chain button is pressed. Because of time constraints, I did not quite get to this point. Also, getting the visual UI to run on the same server as the calls for the blockchain was a little tricky with having to make another app route and file with the html.
=======
# Blockchain Spring 2024

## Blockchain 
### Endpoint Collections 
  - [Basic Blockchain](https://nobles-blockchain.postman.co/workspace/New-Team-Workspace~6ee04c91-09b2-4066-a420-2d5e83667e0d/collection/24854847-a4059b9c-1111-4056-82e7-6c845caf1603?action=share&creator=24854847)
  - [Basic Blockchain Expanded](https://nobles-blockchain.postman.co/workspace/New-Team-Workspace~6ee04c91-09b2-4066-a420-2d5e83667e0d/collection/24854847-852421c2-4abb-4502-a0cf-e8117949fb49?action=share&creator=24854847)

### Running the Project
1. To run the application, use the following command: ```python basic_blockchain_expanded.py```. The application will start a Flask server on http://127.0.0.1:5000.
## Cryptocurrency

MontyCoin is a simple implementation of a blockchain and cryptocurrency.

### Endpoint Collections
  - [Cryptocurrency](https://nobles-blockchain.postman.co/workspace/New-Team-Workspace~6ee04c91-09b2-4066-a420-2d5e83667e0d/collection/24854847-5aaeccc5-c743-4bf6-a1a2-5f3ec30ad654?action=share&creator=24854847)
  - [Transaction Picker](https://nobles-blockchain.postman.co/workspace/Blockchain~6ee04c91-09b2-4066-a420-2d5e83667e0d/collection/31591599-4b3fe1aa-9f86-41a1-9705-ac6bd2beabe5?action=share&creator=24854847)

### Running the Project
1. Navigate to scripts directory
2. Run ```chmod +x run.sh``` and ```chmod +x stop.sh``` to make scripts executable
3. Run the servers (nodes) with ```./run.sh```. This will start 4 nodes on http://127.0.0.1:5000 - http://127.0.0.1:5003
4. Stop the nodes with  ```./stop.sh```

### Project Improvements
1. **Transaction Validation**:  Implement a system to validate transactions before they are added to the blockchain. This could include checking if the sender has enough balance to perform the transaction.
2. **Wallets**: Create a Wallet class that generates private and public keys for users. The private key can be used to sign transactions and the public key can be used as the user's address.
3. **Transaction Signing and Verification**: Implement a system where transactions are signed using the sender's private key and can be verified by others using the sender's public key. This ensures that only the owner of a wallet can make transactions from it.
4. **Improved Mining Process**: Modify the mining process. For example, you could implement a difficulty adjustment algorithm that adjusts the difficulty of the mining process based on the total computational power of the network.
5. **Custom Hashing Algorithm**: Implement a custom hashing algorithm for the blockchain. This could be a great way to learn about cryptographic hash functions.
6. **Peer-to-Peer Network**: Instead of manually adding nodes, implement a peer-to-peer network where nodes can discover each other.
7. **GUI**: Create a graphical user interface (GUI) for easier interaction with the blockchain.
8. **Error Handling**: Improve error handling and return appropriate HTTP status codes and messages when errors occur.
9. **Data Persistence**: Implement a system to store the blockchain data persistently.
10.** Reward System**: Implement a reward system for miners.

### Smart Contracts
>>>>>>> 2496eef8fa6156ba57cc45c9ae1811629f0b6aca
