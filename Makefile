all:
	@echo 'Be professional, use make!'

run: clean
	@python CoursePro

clean:
	@rm -rfv html image
