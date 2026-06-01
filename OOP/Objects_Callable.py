class Add:
    def __init__(s):
        pass
    
    def __call__(s,a, b):
        return a + b
    
a = Add()
print(callable(a))       # True → Because __call__ method exists 
print(a(2,4))            # 6  internally  working  a.__call__(2,5)
print(a.__call__(2,5))   # 7
