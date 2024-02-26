class FileWorker:
    def __init__(self,filename) -> None:
        self.filename=filename
    
    def __enter__(self):
        self.file=open(self.filename,"r+")
        return self
    
    def __exit__(self,*args):
        self.file.close()

    def __iter__(self):
        self.position=0
        self.text=self.file.read().split(' ')
        return self

    def __next__(self):
        if self.position < len(self.text):
            word=self.text[self.position]
            self.position+=1
            return word
        else:
            raise StopIteration
        
if __name__=="__main__":
    file=FileWorker("1.txt")
    with file as f:
        for word in f:
            print(word)
