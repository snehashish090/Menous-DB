from requests import *

var = get('http://127.0.0.1:8000/table?database=test&table=people&key=6ew_8VeRzVjYGbuvsXDKlg')
print(var)