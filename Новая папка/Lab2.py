class F:
    def __init__(self,filename:str) -> None:
        with open(filename,"r") as input:
            self.text=input.read()

    def __call__(self,fname:str):
        with open(fname,"w+") as output:
            output.write(str(self.text))

    def split(self):
        self.text=self.text.split(' ')

    def join(self,symbol:str):
        self.text=symbol.join(self.text)

if __name__=="__main__":
    file=F("1.txt") #init   Object
    file.split()    #Method
    file("2.txt") # Method __call__
    file.join('_')  #Method
    file("3.txt") # Method __call__
    