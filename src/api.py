from flask import *
from models import *
from auth.auth import *

app = Flask(__name__)

@app.route('/database', methods=['GET', 'POST', 'DELETE'])
def index():
    if request.method == 'GET':
        try:
            key = request.headers['key']
            db  = request.headers.get('database')

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

    elif request.method == "POST":
        try:
            key = request.headers['key']
            db = request.headers['database']

            if check_key(key):
                database = dataBase(db)
                if database.check_database_exists():
                    abort(403)
                else:
                    database.create_database()
                    return jsonify(database.read_db())
            else:
                abort(403)
        except Exception as ex:
            return str(ex)

    elif request.method == "DELETE":
        try:
            key = request.headers['key']
            db = request.headers['database']

            if check_key(key):
                database = dataBase(db)
                if database.check_database_exists():
                    db.delete_database()
                    return redirect("/database")
                else:
                    return "database not found"
            else:
                abort(403)
        except:
            abort(403)


@app.route('/table', methods=['GET', 'POST', 'PATCH', 'DELETE'])
def table():

    if request.method == "GET":
        try:
            key = request.headers['key']
            table = request.headers.get('table')
            db = request.headers.get('database')

            if check_key(key):
                database = dataBase(db)
                if database.check_database_exists():
                    if database.check_table_exists(table):
                        if "conditions" not in request.json:
                            table = database.read_db()[table]
                            return jsonify(table)
                        else:
                            conditions = request.json['conditions']
                            ans = database.where(table, conditions)
                            print(ans)
                            return jsonify(ans)
                    else:
                        abort(404)
                else:
                    abort(404)
            else:
                abort(403)
        except Exception as e:
            return jsonify(str(e))

    elif request.method == 'POST':
        
        headers = request.headers
        key = headers['key']
        table = request.headers['table']
        database = request.headers['database']
        values = request.json

        if check_key(key):
            db = dataBase(database)
            if db.check_database_exists():
                if db.check_table_exists(table):
                    db.add_value_to_table(table, values)
                    return jsonify(db.read_db())
                else:
                    return ("Table Does Not Exist")
            else:
                return ("Database does Not Exist")
        else:
            return "Key Invalid"

    elif request.method == "PATCH":

        headers = request.headers
        key = headers['key']
        table = request.headers['table']
        database = request.headers['database']
        conditions = request.json['conditions']
        values = request.json['values']

        if check_key(key):
            db = dataBase(database)
            if db.check_database_exists():
                if db.check_table_exists(table):
                    db.update_table(table, conditions, values)
                    return jsonify(db.read_db())
                else:
                    abort(404)
            else:
                abort(404)
        else:
            abort(403)

    elif request.method == 'DELETE':
        if "conditions" not in request.json:
            database =  request.headers.get('database')
            table = request.headers['table']
            db = dataBase(database)
            key = request.headers['key']
            
            if check_key(key):
                if db.check_database_exists():
                    if db.check_table_exists(table):
                        db.delete_table(table)
                        return jsonify(db.read_db())
                    else:
                        abort(404)
                else:
                    abort(404)
            else:
                abort(403)
        else:
            database =  request.headers.get('database')
            table = request.headers['table']
            db = dataBase(database)
            key = request.headers['key']

            if check_key(key):
                if db.check_database_exists():
                    if db.check_table_exists(table):
                        db.delete_table(table)
                        return jsonify(db.read_db())
                    else:
                        abort(404)
                else:
                    abort(404)
            else:
                abort(403)

if __name__ == '__main__':
    app.run(debug=True, port = 8000)
