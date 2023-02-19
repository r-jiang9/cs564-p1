build:
	python practiceparser.py items-*.json

clean:
	rm items.dat
	rm bids.dat
	rm users.dat
	rm Category.dat
	rm ItemCategory.dat
	rm itemCategories.txt
	rm categories.txt