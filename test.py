from menousdb import *

db = MenousDB(
    'http://127.0.0.1:5555/',
    'dh8pI_HmXuaLlPMu7w9Luw',
    'HarshaTrust'
)

db.insertIntoTable(
    'authentication',
    {
        'name':'Snehshish',
        'age':15,
        'employee_id':5611987
    }
)

