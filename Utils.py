import random

def getHex(value, size=0):
    if size==0:
        return format(value, 'x')
    return format(value, 'x').zfill(size)

def getDecFromHex(value):
    return int(value, 16)

def getRandomOrder():
    order = []
    temp = list(range(8))
    for i in range(8):
        t = random.choice(temp)
        order.append(t)
        temp.remove(t)
    return order

def hashOrder(order):
    hashed_order = ''
    for i, idx in enumerate(order):
        if i%2==0:
            hashed_order+=chr(ord('a')+idx)
        else:
            hashed_order+=chr(ord('A')+idx)
    return hashed_order

def unhashOrder(hashed_order):
    order = []
    for i, idx in enumerate(hashed_order):
        if i%2==0:
            order.append(ord(idx) - ord('a'))
        else:
            order.append(ord(idx) - ord('A'))
    return order

def getRandomFilter(n=1000):
    size = n//10
    temp = list(range(size**2))
    filter = []
    for i in range(size):
        row = []
        for j in range(size):
            t = random.choice(temp)
            row.append(t)
            temp.remove(t)
        filter.append(row)

    return filter

def hashFilter(filter):
    bits = int(len(getHex(len(filter)**2, 0)))
    hashed_filter = ''
    for r in filter:
        for c in r:
            hashed_filter+=getHex(c, bits)
    return bits, hashed_filter

def unhashFilter(hashed_filter, bits):
    filter = []
    size = int((len(hashed_filter)//bits)**(1/2))
    for i in range(size):
        row = []
        for j in range(size):
            row.append(getDecFromHex(hashed_filter[(i*size*bits)+(j*bits) : (i*size*bits)+(j*bits)+bits]))
        filter.append(row)
    return filter

if __name__ == '__main__':
    print('To be used as an import')