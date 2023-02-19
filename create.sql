DROP TABLE IF EXISTS Item;
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS ItemCategory;
DROP TABLE IF EXISTS Category;
DROP TABLE IF EXISTS Bid;
CREATE TABLE Item (
  Item_ID INTEGER PRIMARY KEY,
  Name CHAR(20),
  Currently REAL,
  Buy_Price REAL,
  First_Bid INTEGER,
  Number_of_Bids INTEGER,
  Started CHAR(20),
  Ends CHAR(20),
  Description CHAR(20),
  Seller_ID INTEGER
);
CREATE TABLE User (
  User_ID INTEGER PRIMARY KEY,
  Rating INTEGER,
  Location CHAR(20),
  Country CHAR(20)
);
CREATE TABLE Bid (
  Item_ID INTEGER,
  Bidder_ID INTEGER, 
  Amount REAL,
  Time CHAR(20),
  PRIMARY KEY(Item_ID, Bidder_ID)
);
CREATE TABLE ItemCategory (
  Item_ID INTEGER,
  Category_ID INTEGER 
  Foreign Key (Category_ID) references Category
  PRIMARY KEY(Item_ID, Category_ID)
);
CREATE TABLE Category (
  Category_ID INTEGER PRIMARY KEY,
  Category CHAR(20)
);
