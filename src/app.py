from api import *
from auth import *
from prettytable import *
import sys

# authenticate()

def dbList():
    tb = PrettyTable(
        ["Number","Data Base"]
    )

    x = get_databases()

    for i in x:
        tb.add_row([x.index(i)+1, i])
    print(tb)

    return x

def tableList(database):
    db = dataBase(database)
    x = list(db.read_db().keys())

    tb = PrettyTable(
        ["Number","Table"]
    )
    for i in x:
        tb.add_row([x.index(i)+1, i])

    print(tb)

    return x

def tableData(database, table):
    db = dataBase(database)
    data = db.get_table(table)

    atts = ["id"]+data["attributes"]

    tb = PrettyTable(atts)

    for i in data:
        if i != "attributes":
            x = [i]
            for j in data[i]:
                x.append(data[i][j])
            tb.add_row(x)

    print(tb)

def explore():
    z = dbList()
    db_input = int(input("\nEnter the number to select database: "))

    if db_input > len(z):
        print("\nNo such database exists\n")
    else:
        y = tableList(z[db_input-1])
        table_input = int(input("\nEnter the number to select table: "))

        if table_input > len(y):
            print("\nNo usch table exists\n")
        else:
            print()
            tableData(z[db_input-1], y[table_input-1])

def start():
    port = int(input("Enter port number: "))
    host = input("Enter host: ").replace(" ", "")
    print("""
    # ███╗░░░███╗███████╗███╗░░██╗░█████╗░██╗░░░██╗░██████╗  ██████╗░██████╗░
    # ████╗░████║██╔════╝████╗░██║██╔══██╗██║░░░██║██╔════╝  ██╔══██╗██╔══██╗
    # ██╔████╔██║█████╗░░██╔██╗██║██║░░██║██║░░░██║╚█████╗░  ██║░░██║██████╦╝
    # ██║╚██╔╝██║██╔══╝░░██║╚████║██║░░██║██║░░░██║░╚═══██╗  ██║░░██║██╔══██╗
    # ██║░╚═╝░██║███████╗██║░╚███║╚█████╔╝╚██████╔╝██████╔╝  ██████╔╝██████╦╝
    # ╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░╚════╝░░╚═════╝░╚═════╝░  ╚═════╝░╚═════╝░                                                                                   
    #     """)
    app.run(host=host, port=port)

bindings = {
    "explore": explore,
    "list-db":dbList,
    "new-user":signup,
    "start":start,
    "get-key":getuserkey,
}

def main():
    while True:
        inp = input("menousdb> ")
        if "help" in inp:
            print("Commnds available:\n")
            for i in bindings.keys():
                print(i)
        if "exit" in inp:
            break
        for i in bindings:
            if i in inp:
                bindings[i]()


if len(sys.argv) > 1:
    argument = sys.argv[1]
    
    if "help" in argument:
            print("Commnds available:\n")
            for i in bindings.keys():
                print(i)
    for i in bindings:
        if i == argument:
            bindings[i]()
else:
    main()
