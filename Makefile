install:
	poetry install

test:
	poetry run pytest -vv

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

lint:
	poetry run flake8 gendiff

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build

publish:
	poetry publish --dry-run

publish-test:
	poetry publish -r testPyPi --dry-run

package-install:
	pip install dist/*.whl
