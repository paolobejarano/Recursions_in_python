def factorial(n):
    """Assumes n an int > 0
        Returns n!"""
    if n == 1:
        return n
    return n * factorial(n-1)

def test():
    for x in [1,2,3,4,5,6]:
        print("Testing " + str(x) + "! = ", factorial(x))
        
test()
