class F:
    def __call__(self,h):
        return self.S*h
    def __init__(self,r) -> None:
        self.r=r
    @property
    def S(self):
        return 3.14*self.r**2
    
    
model=F(10)
print(model.S)
print(model(5))
print(model(7))
print(model(10))