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

def create_table(database, name, attributes:list):
    if check_database_exists(database) == False:
        raise Exception("Database does exist")
    else:
        data = read_db(database)
        data[name] = {'attributes': attributes}
        write_db(database, data)
        
def add_value_to_table(database, table,values:dict):
    if check_database_exists(database) == False:
        raise Exception("Database does not exist")
    else:
        data = read_db(database)
        value_att = []

        for i in values.keys():
            value_att.append(i)

        if value_att == data[table]['attributes']:
            data[table][str(datetime.now())] = values
            write_db(database, data)
        else:
            raise Exception(" Attributes do not match table")

add_value_to_table(
    'test',
    'PEOPLE',
    {
        'name':'Snehashish Laskar',
        'age':15,
        'gender':'male',
    }
)
