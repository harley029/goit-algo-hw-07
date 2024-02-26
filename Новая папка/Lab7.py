class C:
    def __init__(self,filename) -> None:
        self.filename=filename
        
    def __enter__(self):
        self.file=open(self.filename,"a+")

    def read_n_print(self,text):
        print(self.file.write(f"{str(text)}\n"))

    def __exit__(self,*args):
        self.file.close()
        print(args)

if __name__=="__main__":
    c= C("1.txt")
    with c:
        c.read_n_print("test 1 2 3")