from contextlib import contextmanager
from time import sleep

@contextmanager
def readfile(fname:str):
    # __enter__()
    file=open(fname,"r+")
    yield file
    # __exit__()
    file.close()

with readfile("1.txt") as f:
    print(f.read(3))