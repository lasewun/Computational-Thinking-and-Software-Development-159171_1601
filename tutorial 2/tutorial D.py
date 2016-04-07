#Exercise D - Roger Gilbertson 14.03.16

def double(x):
    print('from double:', x)
    return x*3

def subtract(y, z):
    print('from subtract:', y, ' and ', z)
    return y - z

result = subtract(20, double(10))
print(result)