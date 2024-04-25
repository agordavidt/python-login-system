# Console Based Authentication System

## Overview
A python console-based authentication system using SQLite for database management. The system involves a server-client architecture where the server interacts with an SQLite database to verify user credentials provided by the client.

## Features
- **SQLite Database Creation**: Initializes an SQLite database to store user credentials securely.
- **Sample Data Population**: Fills the database with sample data such as usernames and hashed passwords for testing purposes.
- **Server Script Development**: Builds a server script responsible for handling client requests and validating user credentials against the database.
- **Client Script Implementation**: Develops a client script to send authentication requests to the server.
- **Secure Authentication**: Ensures security through hashing techniques for storing passwords and comparison of hashed credentials in a secure manner.
- **Access Control**: Grants or denies access to clients based on the validity of the provided username and password.

## Security Measures
- **Hashing**: Utilizes hashing algorithms to securely store passwords in the database, mitigating the risk of storing plaintext passwords.
- **Prepared Statements**: Implements prepared statements to prevent SQL injection attacks, ensuring safe interaction with the database.
- **Secure Communication**: Ensures secure communication between the client and server to protect sensitive information during transit.

## Usage
1. Run the server script to initiate the authentication server.
2. Execute the client script and provide the username and password for authentication.
3. The server will validate the provided credentials against the database.
4. Access will be granted or denied based on the validity of the credentials.

## Dependencies
- SQLite3: A lightweight, file-based database engine used for local data storage.
- Python (for scripts): The programming language used for developing the server and client scripts.

## Note
This project serves as a basic demonstration of a console-based authentication system.

