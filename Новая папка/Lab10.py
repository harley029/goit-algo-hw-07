from Lab9 import FileWorker
file=FileWorker("2.txt")
with file as f:
    for word in f:
        print(word)