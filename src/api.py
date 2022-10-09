from flask import *
from models import *
from auth.auth import *

app = Flask(__name__)

@app.route('/database', methods=['GET', 'POST', 'DELETE'])
def index():
    try:
        key = request.args.get('key')
        db  = request.args.get('database')

        if check_key(key):
            database = dataBase(db)
            if database.check_database_exists():
                data = database.read_db()
                return jsonify(data)
            else:
                abort(403)
        else:
            abort(404)
    except:
        abort(403)


@app.route('/table', methods=['GET', 'POST', 'UPDATE', 'DELETE'])
def table():
    try:
        key = request.args.get('key')
        table = request.args.get('table')
        db = request.args.get('database')

        if check_key(key):
            database = dataBase(db)
            if database.check_database_exists():
                if database.check_table_exists(table):
                    table = database.read_db()[table]
                    return jsonify(table)
                else:
                    abort(404)
            else:
                abort(404)
        else:
            abort(403)
    except:
        abort(403)


if __name__ == '__main__':
    app.run(debug=True, port = 8000)