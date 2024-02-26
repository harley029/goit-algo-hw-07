class ReadFileByWords:
    def __init__(self,filename:str) -> None:
        with open(filename,"r") as input:
            self.words=input.read().split(' ')
    def __iter__(self):
        self.count=0
        return self
    def __next__(self):
        if self.count < len(self.words):
            word=self.words[self.count]
            self.count+=1
            return word
        else: raise StopIteration

if __name__=="__main__":
    f=ReadFileByWords("1.txt")
    for w in f:
        print(w, end=', ')