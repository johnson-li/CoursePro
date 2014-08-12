all:
	@echo 'Be professional, use make!'

run:
	@python CoursePro

pep8:
	@grep --color=auto -T PEP8 CoursePro/*.py

clean:
	@rm -rfv html image CoursePro/*.pyc
