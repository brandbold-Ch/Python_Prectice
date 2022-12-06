class simplyfr():
    
    def __init__(self, numerator, denominator) -> None:
        self.numerator = numerator
        self.denominator = denominator
        
        for i in range(1,101):
            
            if ((i//1==i) and (i//2>0) and (i%2!=0) or (i==2)):
                
                if (self.numerator%i==0 and self.denominator%i==0):
                    
                    self.up = self.numerator//i
                    self.down = self.denominator//i
                    
                    print(i)
                    
    def __str__(self) -> str:
        return f"{self.up}\{self.down}"
    
a = simplyfr(4,8)
print(a)