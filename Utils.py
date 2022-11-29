import random

def getHex(value):
    return format(value, 'x').zfill(3)

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

def getRandomFilter():
    n=1024
    temp = list(range(n))
    filter = []
    for i in range(int(n**(1/2))):
        row = []
        for j in range(int(n**(1/2))):
            t = random.choice(temp)
            row.append(t)
            temp.remove(t)
        filter.append(row)
    return filter

def hashFilter(filter):
    hashed_filter = ''
    for r in filter:
        for c in r:
            hashed_filter+=getHex(c)
    return hashed_filter

def unhashFilter(hashed_filter):
    filter = []
    size = int((len(hashed_filter)//3)**(1/2))
    for i in range(size):
        row = []
        for j in range(size):
            row.append(getDecFromHex(hashed_filter[(i*size*3)+(j*3) : (i*size*3)+(j*3)+3]))
        filter.append(row)
    return filter

if __name__ == '__main__':
    print('To be used as an import')