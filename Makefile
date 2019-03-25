init:
	pip3 install -r requirements.txt
test:
	python3 -m unittest tests/question_A/tests.py
	python3 -m unittest tests/question_B/tests.py