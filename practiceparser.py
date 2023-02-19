import sys
from json import loads
from re import sub
import pickle
from os.path import exists as file_exists

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
    
    #create Category and ItemCategory tables
    catList = [] #category table - list of all possible categories
    itemCategoryList = {}
    #find the categories file
    if file_exists("categories.txt"):  #if yes, read it in
        with open("categories.txt", 'rb') as c:
            catList = pickle.load(c)
            c.close()
        catTxt = open("categories.txt", 'wb') 
    
    else:  #else create new file
        catTxt = open("categories.txt", 'wb')
        
    #find the itemCategories file
    if file_exists("itemCategories.txt"): #if it exists, read it
        with open("itemCategories.txt", 'rb') as ic:
            itemCategoryList = pickle.load(ic)
            ic.close()
        itemCategoriesTxt = open("itemCategories.txt", 'wb')
    else:  #else create new file
        itemCategoriesTxt = open("itemCategories.txt" ,'wb')

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
            itemInfo += "\"" + sub(r'\"','\"\"', itemName) + "\"|"


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
            itemInfo += "\"" + sub(r'\"','\"\"', itemDescription) + "\"|"
        
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
        #create ItemCategory table
        Categories = item["Category"]
        ItemId = item["ItemID"]
        
        #add all new unique categories to the CatList
        for ItemCats in Categories: 
            for cat in ItemCats.split('", "'):
                category = cat.strip()
                if not category in catList:
                    catList.append(category)
        itemCategoryList[ItemId] = Categories

        seller = item["Seller"]
        sellerID = seller["UserID"]    
        sellerRating = seller["Rating"]
        sellerLocation = item["Location"]
        sellerCountry = item["Country"]

        userInfo += sellerID + "|" + sellerRating + "|" + sellerLocation + "|" + sellerCountry
    
        itemInfo += sellerID
        itemOutput.write(itemInfo + "\n")
        userOutput.write(userInfo + "\n")
    
    #save to file so we can use between runs
    pickle.dump(catList, catTxt)
    pickle.dump(itemCategoryList, itemCategoriesTxt)



def create_categories_tables():
    #sort catList and create Categories table 
    C = open("Category.dat", 'a')
    with open("categories.txt", 'rb') as c:       
        catList = pickle.load(c)
        catDict = {}
        catList.sort();
        c.close()


    for i in range(0, len(catList)):
        catDict[catList[i]] = i+1
        C.write(str(i+1) + '|"'+ catList[i] + '"\n')


    #create itemCategories table    
    IC = open("ItemCategory.dat", 'a')
    with open("itemCategories.txt", 'rb') as ic:
      itemCategoriesList = pickle.load(ic)
      ic.close()
  
    for item in itemCategoriesList:
        for cat in itemCategoriesList[item]:
            line = item +"|" + str(catDict[cat])
            IC.write(line+'\n')


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
    #create categories
    create_categories_tables()

if __name__ == '__main__':
    main(sys.argv)