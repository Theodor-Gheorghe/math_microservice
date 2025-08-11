from flask import Flask
from routes import api          # ✅ importăm blueprint-ul
from models import init_db      # ✅ importăm inițializarea DB

app = Flask(__name__)
init_db()                       # ✅ creăm tabela dacă nu există

# ✅ Înregistrăm toate rutele din blueprint
app.register_blueprint(api)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
