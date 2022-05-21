lint:
				poetry run flake8 gendiff

build:
				poetry build

install:
				poetry install

publish:
				poetry publish --dry-run

publish-test:
				poetry publish -r testPyPi --dry-run

package-install:
				pip install dist/*.whl

test:
				poetry run python tests/test_files.py