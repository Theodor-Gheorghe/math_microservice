import os

# Calea absolută către fișierul SQLite (salvat în folderul 'database')
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'database', 'requests.db')