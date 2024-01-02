from multiprocessing import Process, set_start_method
from api import app
from time import sleep

set_start_method('fork')
mu = Process(target=app.run)

if __name__=="__main__":
    mu.start()
    sleep(3)
    mu.kill()