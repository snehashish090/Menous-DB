from requests import *

headers = {
    "key":"yW4j2LY0AgGCQJg-UrrK1A",
    "table":"students",
    "database":"class",
    "Content-Type":"application/json"
}
var = get('http://127.0.0.1:8000/table', headers=headers)
print(var.json())
