cd
cd
pip install pipenv
pipenv shell
pipenv install selenium --dev
pipenv install pytest --dev
pipenv install openpyxl
pipenv install pytest-azurepipelines
pipenv install pytest-cov
pipenv run python -m pytest -v