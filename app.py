from flask import Flask
from routes import api          # import of blueprint
from models import init_db      # import DB initialization

app = Flask(__name__)
init_db()                       # create table if not exist

#  registry all routes from blueprint
app.register_blueprint(api)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
