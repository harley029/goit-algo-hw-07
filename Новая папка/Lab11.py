import random
from time import sleep

def my_generator():
    
    while True:
        received = yield "Ready"
        yield f"Received: {received}"

gen = my_generator()

def genInt():
    while True:
        yield random.randint(1,100)

for i in genInt():
    print(next(gen))  
    print(gen.send(i))
    sleep(1)