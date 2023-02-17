import sys
from json import loads
from re import sub

with open('items-0.json', 'r') as f:
    items = loads(f.read())['Items']

itemOutput = open("items.dat", "a")
for item in items:
    itemInfo = ""
    itemID = item["ItemID"]
    itemInfo += itemID + "|"

    itemName = item["Name"]
    itemInfo += itemName + "|"

    itemCurrently = item["Currently"]
    itemInfo += itemCurrently + "|"

    if "Buy_Price" in item.keys():
        itemBuyPrice = item["Buy_Price"]
        itemInfo += itemBuyPrice + "|"
    else:
        itemInfo += "NULL|"

    itemFirstBid = item["First_Bid"]
    itemInfo += itemFirstBid + "|"

    itemNumBids = item["Number_of_Bids"]
    itemInfo += itemNumBids + "|"

    itemStart = item["Started"]
    itemInfo += itemStart + "|"

    itemEnd = item["Ends"]
    itemInfo += itemEnd + "|"

    if item["Description"] == None:
        itemInfo += "NULL|"
    else:
        itemDescription = item["Description"]
        itemInfo += itemDescription + "|"
    
    seller = item["Seller"]
    sellerID = seller["UserID"]
    itemInfo += sellerID

    sellerLocation = item["Location"]
    sellerCountry = item["Country"]

    itemOutput.write(itemInfo + "\n")