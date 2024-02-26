import time
class Squares:
    def __iter__(self):
        self.value=0
        return self
    def __next__(self):
        self.value+=1
        return self.value**2
    
if __name__=="__main__":
    for i in Squares():
        print(i)
        time.sleep(1)