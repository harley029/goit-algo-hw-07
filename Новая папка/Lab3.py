class PowTwo:
    def __init__(self, max=0):
        self.max = max
 
    def __iter__(self): # ініціалізація ітератора
        self.n = 0
        return self
 
    def __next__(self): # Отримання наступного елемента
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration
        
if __name__=="__main__":
    pt=PowTwo(5)
    for i in pt:
        print(i)
    # it=iter(pt)
    # print(it)
    print(next(pt))