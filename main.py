def sumBetween(x, y):
    chunkyref = 0
    for i in range (x + 1, y):
        chunkyref = chunkyref + i
     
    return chunkyref 

print (sumBetween(1, 2))