VENV := .venv

all: venv

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	./$(VENV)/bin/pip install -r requirements.txt

# venv is a shortcut target
venv: 
	. $(VENV)/bin/activate

run: venv

	./$(VENV)/bin/python3 src/admin.py

clean:
	rm -rf $(VENV)
	find . -type f -name '*.pyc' -delete

test:
	coverage run -m unittest discover -s ./tests -p '*_test.py'
	coverage report -m

.PHONY: all venv run clean test
