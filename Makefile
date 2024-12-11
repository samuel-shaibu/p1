install:
		pip install --upgrade pip && pip install -r requirements.txt

test:
		python -m pytest -vv test_main.py

format:
		black *.py

run:	
		python app.py

run-uvicorn:
		uvicorn main:app --reload

killweb:
		sudo killall uvicorn

lint:	
		pylint --disable=R, app.py

all:	install lint