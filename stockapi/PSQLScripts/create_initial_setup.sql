-- Create initial setup for db

-- Create user table
CREATE TABLE IF NOT EXISTS users(
	user_id SERIAL PRIMARY KEY NOT NULL,
	password VARCHAR ( 255 ) NOT NULL,
	fn VARCHAR ( 255 ),
	ln VARCHAR ( 255 ),
	phone_no VARCHAR ( 255 ) UNIQUE NOT NULL,
	email VARCHAR ( 255 ) UNIQUE NOT NULL,
	created_on TIMESTAMP NOT NULL
);

-- Create role table  
CREATE TABLE IF NOT EXISTS roles(
   role_id serial PRIMARY KEY,
   role_name VARCHAR (255) UNIQUE NOT NULL
);

-- INSERT TWO ROLES
INSERT INTO roles(role_name) VALUES ('user');
INSERT INTO roles(role_name) VALUES ('admin');

-- Create role-user mapping table  
CREATE TABLE IF NOT EXISTS users_roles(
    user_id INT NOT NULL,
  	role_id INT NOT NULL,
  
  	PRIMARY KEY (user_id, role_id),
  	FOREIGN KEY (role_id)
      	REFERENCES roles (role_id),
  	FOREIGN KEY (user_id)
      REFERENCES users (user_id)
);

-- Create stock table
CREATE TABLE IF NOT EXISTS stocks(
   stock_id serial PRIMARY KEY,
   stock_symbol VARCHAR (255) UNIQUE NOT NULL
);

-- Create mapping table for users and stocks
CREATE TABLE IF NOT EXISTS users_stocks(
    user_id INT NOT NULL,
  	symbol VARCHAR(10) NOT NULL,
  
  	PRIMARY KEY (user_id, symbol),
  	FOREIGN KEY (symbol)
      	REFERENCES stockinfo (symbol),
  	FOREIGN KEY (user_id)
      REFERENCES users (user_id)
);