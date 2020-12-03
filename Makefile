install:
		poetry install

lint:
		poetry run flake8 gendiff

build:
		poetry build

publish:
		poetry publish --dry-run

package-install:
		pip install dist/*.whl