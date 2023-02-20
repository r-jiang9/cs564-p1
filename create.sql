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
  Seller_ID INTEGER,
  FOREIGN KEY (Seller_ID) references User (User_ID)
);
CREATE TABLE User (
  User_ID CHAR(20) PRIMARY KEY,
  Rating INTEGER,
  Location CHAR(20),
  Country CHAR(20)
);
CREATE TABLE Bid (
  Item_ID INTEGER,
  Bidder_ID INTEGER, 
  Time CHAR(20),
  Amount REAL,
  FOREIGN KEY (Item_ID) references Item(Item_ID),
  PRIMARY KEY(Item_ID, Bidder_ID, Time)
);
CREATE TABLE ItemCategory (
  Item_ID INTEGER,
  Category_ID INTEGER, 
  FOREIGN KEY (Category_ID) references Category (Category_ID),
  PRIMARY KEY(Item_ID, Category_ID)
);
CREATE TABLE Category (
  Category_ID INTEGER PRIMARY KEY,
  Category CHAR(20)
);
