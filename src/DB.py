import json 
import os
from pathlib import Path
from datetime import datetime

path = os.path.join(Path(__file__).parent, "data")

def read_db(database):
    with open(path+f"/{database}.json",'r') as file:
        data = json.load(file)
    return data

def write_db(database, data):
    with open(path+f"/{database}.json",'w') as file:
        json.dump(data, file, indent=4)

def create_database(name):
    if os.path.exists(path+f"/{name}.json"):
        raise Exception("Database already exists")
    else:
        with open(path+f"/{name}.json", 'w') as file:
            json.dump({}, file, indent=True)

def check_database_exists(name):
    if os.path.exists(path+f"/{name}.json"):
        return True
    else:
        return False

def check_table_exists(database, table):
    data = read_db(database)
    if table not in data.keys():
        return False
    else:
        return True
        
def create_table(database, name, attributes:list):
    if check_database_exists(database) == False:
        raise Exception("Database does exist")
    elif check_table_exists(name) == False:
        data = read_db(database)
        data[name] = {'attributes': attributes}
        write_db(database, data)
    else:
        raise Exception("Table already exists")
        

def add_value_to_table(database, table,values:dict):
    if check_database_exists(database) == False:
        raise Exception("Database does not exist")
    elif check_table_exists(database, table):
        data = read_db(database)
        value_att = []

        for i in values.keys():
            value_att.append(i)

        if value_att == data[table]['attributes']:
            data[table][str(datetime.now())] = values
            write_db(database, data)
        else:
            raise Exception(" Attributes do not match table")
    else:
        raise Exception("Table does not exist")


def where(database, table, conditions):
    if check_database_exists(database) == False:
        raise Exception("Database does not exist")
    elif check_table_exists(database, table) == False:
        raise Exception("Table does not exist")
    else:
        data = read_db(database)[table]
        for i in data:
            if i!= "attributes":
                condition = True
                for j in conditions:
                    if data[i][j] != conditions[j]:
                        condition = False
                if condition:
                    return data[i]
    return {}

def delete_condition(database, table, conditions):
    data = read_db(database)
    
    data2 = where(database, table, conditions)

    for i in data:
        if data[table][i] == data2:
            del data[table][i]

    write_db(database, data)
        
delete_condition('test', 'PEOPLE', {'age':43})