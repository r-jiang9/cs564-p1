import sys
from json import loads
from re import sub

MONTHS = {'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06',\
        'Jul':'07','Aug':'08','Sep':'09','Oct':'10','Nov':'11','Dec':'12'}

"""
Returns true if a file ends in .json
"""
def isJson(f):
    return len(f) > 5 and f[-5:] == '.json'

"""
Converts month to a number, e.g. 'Dec' to '12'
"""
def transformMonth(mon):
    if mon in MONTHS:
        return MONTHS[mon]
    else:
        return mon

"""
Transforms a timestamp from Mon-DD-YY HH:MM:SS to YYYY-MM-DD HH:MM:SS
"""
def transformDttm(dttm):
    dttm = dttm.strip().split(' ')
    dt = dttm[0].split('-')
    date = '20' + dt[2] + '-'
    date += transformMonth(dt[0]) + '-' + dt[1]
    return date + ' ' + dttm[1]

"""
Transform a dollar value amount from a string like $3,453.23 to XXXXX.xx
"""

def transformDollar(money):
    if money == None or len(money) == 0:
        return money
    return sub(r'[^\d.]', '', money)

"""
Parses a single json file. Currently, there's a loop that iterates over each
item in the data set. Your job is to extend this functionality to create all
of the necessary SQL tables for your database.
"""
def parseJson(json_file):
    with open(json_file, 'r') as f:
        items = loads(f.read())['Items']

    itemOutput = open("items.dat", "a")
    bidOutput = open("bids.dat", "a")
    userOutput = open("users.dat", "a")
    categoryOutput = open("categories.dat", "a")

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
            itemCurrently = transformDollar(item["Currently"])
            itemInfo += itemCurrently + "|"

        if "Buy_Price" in item.keys():
            if item["Buy_Price"] == None:
                itemInfo += "NULL"
            else:
                itemBuyPrice = transformDollar(item["Buy_Price"])
                itemInfo += itemBuyPrice + "|"
        else:
            itemInfo += "NULL|"

        if item["First_Bid"] == None:
            itemInfo += "NULL"
        else:
            itemFirstBid = transformDollar(item["First_Bid"])
            itemInfo += itemFirstBid + "|"

        if item["Number_of_Bids"] == None:
            itemInfo += "NULL"
        else:
            itemNumBids = item["Number_of_Bids"]
            itemInfo += itemNumBids + "|"

        if item["Started"] == None:
            itemInfo += "NULL"
        else:
            itemStart = transformDttm(item["Started"])
            itemInfo += itemStart + "|"

        if item["Ends"] == None:
            itemInfo += "NULL"
        else:
            itemEnd = transformDttm(item["Ends"])
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
                    bidderInfo = ""
                    bidInfo += itemID + "|"
                    bid = bids[i]["Bid"]
                    if bid["Bidder"] != None:
                        bidder = bid["Bidder"]
                        bidInfo += bidder["UserID"] + "|"
                        bidderInfo += bidder["UserID"] + "|"
                        if bidder["Rating"] == None:
                            bidderInfo += "NULL|"
                        else: 
                            bidderInfo += bidder["Rating"] + "|"
                        if "Location" in bidder.keys():
                            if bidder["Location"] == None:
                                bidderInfo += "NULL|"
                            else: 
                                bidderInfo += bidder["Location"] + "|"
                        else: 
                            bidderInfo += "NULL|"
                        if "Country" in bidder.keys():
                            if bidder["Country"] == None:
                                bidderInfo += "NULL"
                                userOutput.write(bidderInfo + "\n")
                            else:
                                bidderInfo += bidder["Country"]
                                userOutput.write(bidderInfo + "\n")
                        else:
                            bidderInfo += "NULL"
                            userOutput.write(bidderInfo + "\n")
                    if bid["Time"] == None:
                        bidInfo += "NULL|"
                    else:
                        bidInfo += transformDttm(bid["Time"]) + "|"
                    if bid["Amount"] == None:
                        bidInfo += "NULL"
                    else:
                        bidInfo += transformDollar(bid["Amount"])
                    bidOutput.write(bidInfo + "\n")      

        seller = item["Seller"]
        sellerID = seller["UserID"]    
        sellerRating = seller["Rating"]
        sellerLocation = item["Location"]
        sellerCountry = item["Country"]

        userInfo += sellerID + "|" + sellerRating + "|" + sellerLocation + "|" + sellerCountry
    
        itemInfo += sellerID
        itemOutput.write(itemInfo + "\n")
        userOutput.write(userInfo + "\n")

"""
Loops through each json files provided on the command line and passes each file
to the parser
"""
def main(argv):
    if len(argv) < 2:
        print >> sys.stderr, 'Usage: python skeleton_json_parser.py <path to json files>'
        sys.exit(1)
    # loops over all .json files in the argument
    for f in argv[1:]:
        if isJson(f):
            parseJson(f)
            print "Success parsing " + f

if __name__ == '__main__':
    main(sys.argv)