all:
	@echo 'Be professional, use make!'

pep8:
	@grep --color=auto -T PEP8 *.py

run: clean
	python main.py

clean:
	@rm -fv html/* image/*
