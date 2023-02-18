build:
	python practiceparser.py items-*.json

clean:
	rm items.dat
	rm bids.dat
	rm users.dat
	rm categories.dat