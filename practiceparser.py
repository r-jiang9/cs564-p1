import sys
from json import loads
from re import sub

with open('items-0.json', 'r') as f:
    items = loads(f.read())['Items']

itemOutput = open("items.dat", "a")
bidOutput = open("bids.dat", "a")

for item in items:
    itemInfo = ""
    userInfo = ""

    if item["ItemID"] == None:
        itemInfo += "NULL|"
    else:
        itemID = item["ItemID"]
        itemInfo += itemID + "|"
    
    if item["Name"] == None:
        itemInfo += "NULL|"
    else:
        itemName = item["Name"]
        itemInfo += itemName + "|"

    if item["Currently"] == None:
        itemInfo += "NULL|"
    else:
        itemCurrently = item["Currently"]
        itemInfo += itemCurrently + "|"

    if "Buy_Price" in item.keys():
        if item["Buy_Price"] == None:
            itemInfo += "NULL"
        else:
            itemBuyPrice = item["Buy_Price"]
            itemInfo += itemBuyPrice + "|"
    else:
        itemInfo += "NULL|"

    if item["First_Bid"] == None:
        itemInfo += "NULL"
    else:
        itemFirstBid = item["First_Bid"]
        itemInfo += itemFirstBid + "|"

    if item["Number_of_Bids"] == None:
        itemInfo += "NULL"
    else:
        itemNumBids = item["Number_of_Bids"]
        itemInfo += itemNumBids + "|"

    if item["Started"] == None:
        itemInfo += "NULL"
    else:
        itemStart = item["Started"]
        itemInfo += itemStart + "|"

    if item["Ends"] == None:
        itemInfo += "NULL"
    else:
        itemEnd = item["Ends"]
        itemInfo += itemEnd + "|"

    if item["Description"] == None:
        itemInfo += "NULL|"
    else:
        itemDescription = item["Description"]
        itemInfo += itemDescription + "|"
    
    if "Bids" in item.keys():
        if item["Bids"] != None:
            bids = item["Bids"]
            for i in range(len(bids)):
                bidInfo = ""
                bidInfo += itemID + "|"
                bid = bids[i]["Bid"]
                if bid["Bidder"] == None:
                    bidInfo += "NULL|"
                else:
                    bidder = bid["Bidder"]
                    bidInfo += bidder["UserID"] + "|"
                if bid["Time"] == None:
                    bidInfo += "NULL|"
                else:
                    bidInfo += bid["Time"] + "|"
                bidOutput.write(bidInfo + "\n")       
         
    seller = item["Seller"]
    sellerID = seller["UserID"]
    sellerRating = seller["Rating"]
    sellerLocation = item["Location"]
    sellerCountry = item["Country"]

    itemInfo += sellerID

    itemOutput.write(itemInfo + "\n")