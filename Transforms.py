from Utils import getRandomOrder
from BitPlaneSlicing import getBitPlanes
import copy

def bitIntensityTransform(img, order):
    enc_image = []
    for i in range(len(img)):
        enc_image.append([0]*len(img[i]))

    planes = getBitPlanes(img)
    
    for i, idx in enumerate(order):
        for j in range(len(img)):
            for k in range(len(img[0])):
                enc_image[j][k] += planes[idx][j][k] * (2**(7-i))

    return enc_image

def reversebitIntensityTransform(encrypted_img, order):
    dec_img = []
    for i in range(len(encrypted_img)):
        dec_img.append([0]*len(encrypted_img[i]))

    planes = getBitPlanes(encrypted_img)

    for i, idx in enumerate(order):
        for j in range(len(encrypted_img)):
            for k in range(len(encrypted_img[0])):
                dec_img[j][k] += planes[i][j][k] * (2**(7-idx))

    return dec_img

def spacialTransform(img, filter):
    enc_image = copy.deepcopy(img)
    
    height = len(img)
    width = len(img[0])
    r = (height%len(filter))//2
    while(r+len(filter) < len(img)):
        c = (width%len(filter[0]))//2
        while(c+len(filter[0]) < len(img[0])):
            for i in range(len(filter)):
                for j in range(len(filter[0])):
                    enc_image[r+i][c+j] = img[r+filter[i][j]//len(filter)][c+(filter[i][j]%len(filter[0]))]
            c+=len(filter[0])
        r+=len(filter)

    return enc_image

def reverseSpacialTransform(enc_image, filter):
    dec_image = copy.deepcopy(enc_image)

    height = len(enc_image)
    width = len(enc_image[0])
    r = (height%len(filter))//2
    while(r+len(filter) < len(enc_image)):
        c = (width%len(filter[0]))//2
        while(c+len(filter[0]) < len(enc_image[0])):
            for i in range(len(filter)):
                for j in range(len(filter[0])):
                    dec_image[r+filter[i][j]//len(filter)][c+filter[i][j]%len(filter[0])] = enc_image[r+i][c+j]
            c+=len(filter[0])
        r+=len(filter)

    return dec_image

if __name__ == '__main__':
    print('To be used as an import')