# Author : Snehashish Laskar
# Date   : 1st November 2022

# Importing necessary modules
import json
import os
from pathlib import Path
from datetime import datetime
import random
import sys

if sys.platform == "darwin":
    if not os.path.exists("/Library/Caches/.menousdb"):
        os.mkdir("/Library/Caches/.menousdb")
    if not os.path.exists("/Library/Caches/.menousdb/data"):
        os.mkdir("/Library/Caches/.menousdb/data")
    if not os.path.exists("/Library/Caches/.menousdb/authdata"):
        os.mkdir("/Library/Caches/.menousdb/data")
    path = "/Library/Caches/.menousdb/data"

elif sys.platform == "win32":
    if not os.path.exists(os.getenv("APPDATA")+"/MenoudDb"):
        os.mkdir(os.getenv("APPDATA")+"/MenoudDb")
    if not os.path.exists(os.getenv("APPDATA")+"/MenoudDb"+"/data"):
        os.mkdir(os.getenv("APPDATA")+"/MenoudDb/data")
    path = os.getenv("APPDATA")+"/MenoudDb"+"/data"

class dataBase:

    def __init__(self, name):
        self.name = name

    def read_db(self):
        # Function used throughout the code base 
        # to read from the database's latest data
        with open(path + f"/{self.name}.json", 'r') as file:
            data = json.load(file)
        return data

    def write_db(self, data):
        # Function used throughout the code base to 
        # write to the database
        with open(path + f"/{self.name}.json", 'w') as file:
            json.dump(data, file, indent=4)

    def create_database(self):
        # CREATE DATABASE name
        if os.path.exists(path + f"/{self.name}.json"):
            raise Exception("Database already exists")
        else:
            with open(path + f"/{self.name}.json", 'w') as file:
                json.dump({}, file, indent=True)

    def check_database_exists(self):
        if os.path.exists(path + f"/{self.name}.json"):
            return True
        else:
            return False

    def delete_database(self):
        if self.check_database_exists():
            os.remove(path + f'/{self.name}.json')
        else:
            raise Exception("Database files not found")

    def check_table_exists(self, table: str):
        data = self.read_db()
        if table not in data.keys():
            return False
        else:
            return True

    def create_table(self, table_name: str, attributes: list):
        # CREATE TABLE IF NOT EXISTS table_name(attributes)
        if self.check_database_exists() == False:
            raise Exception("Database does exist")
        elif self.check_table_exists(table_name) == False:
            data = self.read_db()
            data[table_name] = {'attributes': attributes}
            self.write_db(data)
        else:
            raise Exception("Table already exists")

    def add_value_to_table(self, table, values: dict):
        if self.check_database_exists() == False:
            raise Exception("Database does not exist")
        elif self.check_table_exists(table):
            data = self.read_db()
            value_att = []

            for i in values.keys():
                value_att.append(i)

            if value_att == data[table]['attributes']:
                data[table][random.randint(10000, 100000)] = values
                self.write_db(data)
            else:
                raise Exception(" Attributes do not match table")
        else:
            raise Exception("Table does not exist")

    # represents SELECT * FROM table WHERE condition
    def select_where(self, table: str, conditions: dict):
        if self.check_database_exists() == False:
            raise Exception("Database does not exist")
        elif self.check_table_exists(table) == False:
            raise Exception("Table does not exist")
        else:
            data = self.read_db()[table]
            for i in data:
                if i != "attributes":
                    condition = True
                    for j in conditions:
                        if data[i][j] != conditions[j]:
                            condition = False
                    if condition:
                        return data[i]
        return {}

    # represets SELECT cloumns FROM table
    def select_columns(self, table: str, columns: list):
        if self.check_database_exists() == False:
            raise Exception("Database does not exist")
        elif self.check_table_exists(table) == False:
            raise Exception("Table does not exist")
        else:
            data = self.read_db()
            Table = data[table]
            ans = {}
            for column in columns:
                ans[column] = []

            for i in Table:
                if i != "attributes":
                    for j in Table[i]:
                        if j in ans:
                            ans[j].append(Table[i][j])
            return ans

    def select_columns_where(self, table: str, columns: list, conditions: dict):
        if self.check_database_exists() == False:
            raise Exception("Database does not exist")
        elif self.check_table_exists(table) == False:
            raise Exception("Table does not exist")
        else:
            columns = self.select_columns(table, columns)
            result = {}
            for i in columns:
                result[i] = []
            print(columns)
            index = 0
            for i in conditions:
                if conditions[i] in columns[i]:
                    result[i].append(conditions[i])
                    index = columns[i].index(conditions[i])

                for i in columns:
                    result[i].append(columns[i][index])

            return result

    def delete_where(self, table, conditions: dict) -> str:
        data = self.read_db()
        data2 = self.select_where(table, conditions)

        for i in data[table]:
            if data[table][i] == data2:
                del data[table][i]
                self.write_db(data)
                return 'Done'
        raise Exception('Does not exist')

    def delete_table(self, table):
        if self.check_database_exists() == True:
            data = self.read_db()
            del data[table]
            self.write_db(data)

        elif self.check_database_exists() == False:
            raise Exception('Database does not exist')
        else:
            raise Exception('Table does not exist')

    def update_table(self, table: str, conditions: dict, values: dict):
        if self.check_database_exists() == True:
            if self.check_table_exists(table) == True:
                var = self.select_where(table, conditions)
                data = self.read_db()
                current = ""
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

    
def get_databases():
    
    databases = []
    for i in os.listdir(path):
        if ".json" in i:
            databases.append(i.replace(".json", ""))
    return databases

