import os

# The absolute path to the SQLite file (stored in the 'database' folder)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'database', 'requests.db')
