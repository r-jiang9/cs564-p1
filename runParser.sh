JSON_DIR="./ebay_data"
SCRIPT_PATH="./practiceparser.py"
CATEGORY_TB="./ItemCategory.dat"
ITEMS_TB="./Item.dat"
BIDS_TB="./Bid.dat"
USERS_TB="./User.dat"
ARGS=””
rm -f $CATEGORY_TB
rm -f $ITEMS_TB
rm -f $BIDS_TB
rm -f $USERS_TB

  python $SCRIPT_PATH $JSON_DIR/items-*.json

  python -c 'from practiceparser import create_categories_tables; create_categories_tables()'

sort -u $USERS_TB -o $USERS_TB
sort -u $CATEGORY_TB -o $CATEGORY_TB
exit