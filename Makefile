test:
	mypy hello_world.py
	pytest --cov=hello_world --cov-fail-under=90

