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
