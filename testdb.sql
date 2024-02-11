
import mysql.connector

def db_connect():
    db = mysql.connector.connect(
      host="localhost",
      user="root",
      password="admin",
      database="testdb"
    )
    return db

DROP TABLE IF EXISTS customers;
CREATE TABLE customers (
    customer_id int NOT NULL AUTO_INCREMENT,
    fname varchar(125) NOT NULL,
    lname varchar(125) NOT NULL,
    org varchar(125) NOT NULL,
    email varchar(125),
    phone varchar(12) NOT NULL,
    note varchar(255),
    PRIMARY KEY (customer_id)
);

DROP TABLE IF EXISTS reagents;
CREATE TABLE reagents (
    reagent_id int NOT NULL AUTO_INCREMENT,
    name varchar(125) NOT NULL,
    standard varchar(3) NOT NULL,
    supplier varchar(125) NOT NULL,
    grade varchar(125) NOT NULL,
    concentration varchar(125) NOT NULL,
    date_received date NOT NULL,
    expiration date NOT NULL,
    PRIMARY KEY (reagent_id)
);
