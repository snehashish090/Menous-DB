import tkinter as tk
from api import app
from threading import Thread
from multiprocessing import Process, set_start_method

set_start_method('fork')
mu = Process(target=app.run)


window = tk.Tk()

title = tk.Label(text="Menous DB")
title.pack()

status = [False]

status_label = tk.Label(text="Offline",foreground="red")
status_label.pack()

def server_handler():
    if not exit_flag:
        app.run()

def handler():
    if status[0] == False:
        mu.start()
    else:
        mu.kill()
def handler():
    global exit_flag
    if status[0] == False:
        status_label.config(text="Online", foreground="green")
        status_label.pack()
        status[0] = True
        start.config(text="Stop Server")
        handler()
    else:
        status_label.config(text="Offline",foreground="red")
        status_label.pack()
        status[0] = False
        exit_flag = False
        start.config(text="Start Server")
        handler()


exit_flag = False

thread1 = Thread(target=server_handler)

start = tk.Button(text="Start Server", command=lambda: handler())
start.pack()

window.mainloop()

