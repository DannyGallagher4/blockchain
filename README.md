What features and functionality did you add to your blockchain? Why? 

The 2 main features that I added to my blockchain are the randomly created transaction pool to be part of the blocks and a UI that can be used to make the server calls. Everytime a block is mined, a random amount of transactions which have a random sender name, receiver name, and amount, and added to a transaction pool. Then, when a block gets mined, up to 5 of the transactions from the pool are added to the block in a transactions array. Then, I made a UI with three buttons, one for each of the three server calls, that initially printed the result to the console. Then, I made it so that when you mine a block, it displays the data of the mined block in a blokc shown on the UI. Also, I made it so that whenever the validate chain button is clicked, it will show underneath whether or not the blockchain is valid. I made the first change because I felt that a blockchain that did not have any data held in its blocks did not make much sense, so I wanted some transactions to be added to the blocks. I made the second change because I wanted some way to make the calls without postman and also have a better way to show the data besides just some json.


Explanation of what a class is in Python/Object-Oriented Programming

A class is something that defines an object/data type that can be used later to hold values and run functions. A class can be instantiated to use all of its functionality that gets saved to some variable name. This variable will be of the type of the class and every version of that class has the same functionality.


What is an endpoint? What is a server? What is Flask? What is Postman doing? 

An endpoint is a certain url that can be called which will return some data to wherever it is being called from. A server is something on the internet which is able to deliver data when its endpoints are called. Flask is a python library that enables the creation of servers through one's own computer. Postman is calling the endpoints on the server and displaying the data it receives back.


What you intended to do vs. what you actually completed. What challenges did you face? 

Originally, on the UI side, I intended to add a visual representation of the entire blockchain so far whenever the get chain button is pressed. Because of time constraints, I did not quite get to this point. Also, getting the visual UI to run on the same server as the calls for the blockchain was a little tricky with having to make another app route and file with the html.