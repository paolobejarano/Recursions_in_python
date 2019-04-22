def fibonacci(n):
    
    """Assumes n int >= 0
        Returns Fibonnaci of n"""
        
    if n == 0 or n == 1:
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2)

def test():
    
    for x in [0,1,2,3,4,5,6,7,8,9,10]:
        print("Testing Fibonnaci of " + str(x) + " = " + str(fibonacci(x)))
        
test()
