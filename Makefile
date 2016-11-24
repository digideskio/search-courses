setup:
	@pip install -r requirements.txt

run:
	@python manage.py runserver

clean:
	@find . -name "*.pyc" -delete

task:
	@python manage.py process_tasks
