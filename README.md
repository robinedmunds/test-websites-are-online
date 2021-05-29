# test-websites-are-online

Simple Python3 script that batch tests websites and check that they are responding with 200 HTTP status codes. Utilises [**urllib3**](https://urllib3.readthedocs.io/en/latest/user-guide.html).

## Usage

1. cd to directory
2. `python3 -m venv ./venv`
3. `python3 -m pip install -r requirements.txt`
4. Copy file **domains_template.json** to **domains.json**
5. Add your own domains. Do **not** add any prefixes. (e.g. https://, www.). The script adds these with the flags.
6. Run `python3 test-websites-are-online.py`

