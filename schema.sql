CREATE DATABASE IF NOT EXISTS user_data.db;
USE user_data.db;

CREATE TABLE IF NOT EXISTS users(
user_id INT AUTO_INCREMENT,
username VARCHAR(50) NOT NULL,
email VARCHAR(255)  NOT NULL,
passkey VARCHAR(255) NOT NULL,
pfp VARCHAR(255) NOT NULL, 
primary key (user_id)
);
