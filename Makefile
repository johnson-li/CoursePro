all:
	@echo 'Be professional, use make!'

run: clean
	python main.py

clean:
	@rm -fv html/* image/*
