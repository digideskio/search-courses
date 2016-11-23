setup:
	@pip install -r requirements.txt

run:
	@python manage.py runserver

clean:
	@find . -name "*.pyc" -delete
