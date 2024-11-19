.PHONY: install run

install:
	pip install -r requirements.txt

run:
	/home/${USER}/.local/bin/uvicorn main:app --reload