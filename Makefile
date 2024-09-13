install: 
	pip install --upgrade pip && pip install -r requirements.txt

format:
	black *.py

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py

test:
	python -m pytest -cov=main test_main.py -v

report:
	python generate-report.py

report-n-push:
	make report
	git config --local user.email "cpyang@umich.edu"
	git config --local user.name "Peter Yang"
	git add .
	git commit -m "Updated Report"
	git push


all: install format lint test report-n-push