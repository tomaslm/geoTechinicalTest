create_venv:
	python3 -m venv venv
install:
	pip3 install -r requirements.txt
freeze:
	pip3 freeze > requirements.txt
test_question_A:
	python3 -m unittest tests/question_A/tests.py
test_question_B:
	python3 -m unittest tests/question_B/tests.py
start_server_question_C:
	FLASK_ENV=development \
	FLASK_APP=question_C/flask_server.py \
	flask run