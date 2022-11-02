# Author : Snehashish Laskar
# Date   : 1st November 2022

# Importing necessary modules
from flask import Flask, request, jsonify, abort, redirect
from models import *
from auth.auth import *

app = Flask(__name__)

@app.route('/read-db', methods=['GET'])
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
        except Exception as ex:
            return str(ex)
    else:
        abort(403)

@app.route('/create-db',methods = ['POST'])
def createDb():
    try:
        key= request.headers['key']
        db = request.headers['database']

        if check_key(key):
            database = dataBase(db)
            if database.check_database_exists():
                return 'Error: database already exists'
            else:
                database.create_database()
                return 'Successfully created database'

        else:
            abort(403)
    except Exception as ex:
        return str(ex)

@app.route('/check-db-exists', methods = ['GET'])
def checkDbExists():
    try:
        key = request.headers['key']
        db  = request.headers['database']

        if check_key(key):
            database = dataBase(db)
            if database.check_database_exists():
                return 'True'
            else:
                return 'False'
        else:
            abort(403)
    except Exception as ex:
        return str(ex)

@app.route('/del-database', methods = ['DELETE'])
def delDatabase():
    try:
        key = request.headers['key']
        db = request.headers['database']

        if check_key(key):
            database = dataBase(db)
            database.delete_database()
        else:
            abort(403)
    except Exception as ex:
        return str(ex)

@app.route('/check-table-exists', methods=['GET'])
def checkTableExists():
    try:
        key = request.headers['key']
        database = request.headers['database']
        table = request.headers['table']

        if check_key(key):
            db = dataBase(database)
            if db.check_table_exists(table):
                return 'True'
            else:
                return 'False'
        else:
            abort(403)

    except Exception as ex:
        return str(ex)

@app.route('/create-table', methods=['POST'])
def createTable():
    try:
        key = request.headers['key']
        database = request.headers['database']
        table = request.headers['table']
        attributes = request.json['attributes']

        if check_key(key):
            db = dataBase(database)
            db.create_table(table, attributes)
        else:
            abort(403)
    except Exception as ex:
        return str(ex)

@app.route('/insert-into-table', methods = ['POST'])
def insertInto():
    try:
        key = request.headers['key']
        database  = request.headers['database']
        table = request.headers['table']
        values = request.json['values']

        if check_key(key):
            db = dataBase(database)
            db.add_value_to_table(table, values)
        else:
            abort(403)
    except Exception as ex:
        return str(ex)


@app.route('/select-where', methods=['GET'])
def selectWhere():
    try:
        key = request.headers['key']
        database = request.headers['database']
        table = request.headers['table']
        conditions = request.json['conditions']

        if check_key(key):
            db = dataBase(database)
            db.select_where(table, conditions)
            abort(200)
        else:
            abort(403)
    except Exception as ex:
        return str(ex)


@app.route('/select-columns', methods=['GET'])
def select_columns():
    try:
        key = request.headers['key']
        database = request.headers['database']
        table = request.headers['table']
        columns = request.json['columns']

        if check_key(key):
            db = dataBase(database)
            db.select_columns(table, columns)
            abort(200)
        else:
            abort(403)
    except Exception as ex:
        return str(ex)


@app.route('/select-columns-where', methods=['GET'])
def select_columns_where():
    try:
        key = request.headers['key']
        database = request.headers['database']
        table = request.headers['table']
        columns = request.json['columns']
        conditions = request.json['conditions']

        if check_key(key):
            db = dataBase(database)
            db.select_columns_where(table, columns, conditions)
            abort(200)
        else:
            abort(403)
    except Exception as ex:
        return str(ex)

if __name__ == '__main__':
    app.run(debug = True, port = 80)