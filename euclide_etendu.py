def euclide_etendu(a,b):
    if b == 0:
        return a, 1, 0
    else:
        d, x1, y1 = euclide_etendu(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return d, x, y
    
    
def exponentiation_modulaire(a,b,n):
    d = 1
    binaire = bin(b)[2:]  
    for i in range(len(binaire)-1, -1, -1):
        d = (d * d) % n
        if binaire[i] == '1':
            d = (d * a) % n
    return d
