init:
	pip install -r requirements.txt

test:
	nosetests --with-doctest --verbose
