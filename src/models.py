import json 
import os
from pathlib import Path
from datetime import datetime

path = os.path.join(Path(__file__).parent, "data")


class dataBase:

    def __init__(self, name):
        self.name = name


    def read_db(self):
        with open(path+f"/{self.name}.json",'r') as file:
            data = json.load(file)
        return data

    def write_db(self, data):
        with open(path+f"/{self.name}.json",'w') as file:
            json.dump(data, file, indent=4)

    def create_database(self):
        if os.path.exists(path+f"/{self.name}.json"):
            raise Exception("Database already exists")
        else:
            with open(path+f"/{self.name}.json", 'w') as file:
                json.dump({}, file, indent=True)

    def check_database_exists(self):
        if os.path.exists(path+f"/{self.name}.json"):
            return True
        else:
            return False

    def check_table_exists(self, table):
        data = self.read_db()
        if table not in data.keys():
            return False
        else:
            return True

    def create_table(self, table_name, attributes:list):
        if self.check_database_exists() == False:
            raise Exception("Database does exist")
        elif self.check_table_exists(table_name) == False:
            data = self.read_db()
            data[table_name] = {'attributes': attributes}
            self.write_db(data)
        else:
            raise Exception("Table already exists")

    def add_value_to_table(self, table,values:dict):
        if self.check_database_exists() == False:
            raise Exception("Database does not exist")
        elif self.check_table_exists(table):
            data = self.read_db()
            value_att = []

            for i in values.keys():
                value_att.append(i)

            if value_att == data[table]['attributes']:
                data[table][str(datetime.now())] = values
                self.write_db(data)
            else:
                raise Exception(" Attributes do not match table")
        else:
            raise Exception("Table does not exist")

    def where(self, table, conditions):
        if self.check_database_exists() == False:
            raise Exception("Database does not exist")
        elif self.check_table_exists(table) == False:
            raise Exception("Table does not exist")
        else:
            data = self.read_db()[table]
            for i in data:
                if i!= "attributes":
                    condition = True
                    for j in conditions:
                        if data[i][j] != conditions[j]:
                            condition = False
                    if condition:
                        return data[i]
        return {}

    def delete_condition(self, table, conditions):
        data = self.read_db()
        
        data2 = self.where(table, conditions)

        for i in data:
            if data[table][i] == data2:
                del data[table][i]
                break
        self.write_db(data)

    def delete_table(self, table):
        if self.check_database_exists() == True:
            data = self.read_db()
            del data[table]
            self.write_db(data)

        elif self.check_database_exists() == False:
            raise Exception('Database does not exist')
        else:
            raise Exception('Table does not exist')
        
    def update_table(self, table, conditions, values):
        if self.check_database_exists() == True:
            if self.check_table_exists(table) == True:
                var = self.where(table, conditions)
                data = self.read_db()
                current= ""
                for i in data[table]:
                    if data[table][i] == var:
                        current = i
                
                for i in var:
                    for j in values:
                        if i == j:
                            var[i] = values[j]
                data[table][current] = var
                self.write_db(data)
            else:
                raise ValueError("Could not find table")
        else:
            raise Exception("Databse does not exist")
