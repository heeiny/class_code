def func_2(_x,_y):
        
        sum=0
        for i in range(_x,_y+1,1):
            sum += i 
        return(sum)


#Class init함수에서 
class ModClass():
    def __init__(self,_a,_b): 
        self.a = _a
        self.b = _b
    def func_2(self): 
        return self.a ** self.b
