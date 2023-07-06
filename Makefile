install:
		poetry install

build:
		poetry build

publish:
		poetry publish --dry-run

package-install:
		python3 -m pip install --user dist/*.whl

package-install-force:
		python3 -m pip install --user --force-reinstall  dist/*.whl

lint:
		poetry run flake8 gendiff

