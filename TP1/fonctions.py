#question 2.2 
def puissance(a, b):
    return a ** b

#question 2.4

def puissance(a, b):
    if not type(a) is int:
        raise TypeError("Only integers are allowed")
    if not type(b) is int:
        raise TypeError("Only integers are allowed")
    return a ** b
