from csv import unix_dialect
from pathlib import Path

BASE_DIR = Path(__file__).parents[1]
FORMAT_DATE = '%Y-%m-%d_%H-%M-%S'
ENCODING = 'utf-8'
DIALECT = unix_dialect
