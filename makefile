make:
	vim makefile

venv:
	virtualenv -p python3 venv

deps:
	./venv/bin/pip3 install -r requirements.txt

checkin:
	git add -A && git commit && git push

read:
	./venv/bin/python app.py ./books/pride_and_prejudice.txt 300
