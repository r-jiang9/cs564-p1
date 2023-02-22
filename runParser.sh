JSON_DIR="./ebay_data"
SCRIPT_PATH="./EbayParser.py"
CATEGORY_TB="./Category.dat"
ITEMCATEGORY_TB="./ItemCategory.dat"
ITEMS_TB="./Item.dat"
BIDS_TB="./Bid.dat"
USERS_TB="./User.dat"


ARGS=””
rm -f $CATEGORY_TB
rm -f $ITEMCATEGORY_TB
rm -f $ITEMS_TB
rm -f $BIDS_TB
rm -f $USERS_TB
rm -f itemCategories.txt
rm -f categories.txt
 
  python $SCRIPT_PATH $JSON_DIR/items-*.json


  python -c 'from EbayParser import create_categories_tables; create_categories_tables()'


sort -u $USERS_TB -o $USERS_TB
sort -u $ITEMCATEGORY_TB -o $ITEMCATEGORY_TB
exit
