from Utils import getRandomOrder, hashOrder, unhashOrder, getRandomFilter, hashFilter, unhashFilter
from Transforms import bitIntensityTransform, reversebitIntensityTransform, spacialTransform, reverseSpacialTransform
import copy

def encrypt(img):
    channels = []
    channels.append(img[:,:,0])
    channels.append(img[:,:,1])
    channels.append(img[:,:,2])
    orders = []
    filter = getRandomFilter(min(len(img), len(img[0])))
    temp = []
    hash=''
    for i in range(3):
        orders.append(getRandomOrder())
        t = bitIntensityTransform(channels[i], orders[i])
        temp.append(spacialTransform(t, filter))
        hash += hashOrder(orders[i])
        
    enc_img = copy.deepcopy(img)
    enc_img[:,:,0] = temp[0]
    enc_img[:,:,1] = temp[1]
    enc_img[:,:,2] = temp[2]
    bits, hashed_filter = hashFilter(filter)
    hash += str(bits)
    hash += hashed_filter
    
    return enc_img, hash

def decrypt(enc_img, hash):
    channels = []
    channels.append(enc_img[:,:,0])
    channels.append(enc_img[:,:,1])
    channels.append(enc_img[:,:,2])
    bits = int(hash[24])
    filter = unhashFilter(hash[25:len(hash)], bits)
    orders = []
    orders.append(unhashOrder(hash[0:8]))
    orders.append(unhashOrder(hash[8:16]))
    orders.append(unhashOrder(hash[16:24]))
    temp = []
    for i in range(3):
        t = reverseSpacialTransform(channels[i], filter)
        temp.append(reversebitIntensityTransform(t, orders[i]))

    dec_img = copy.deepcopy(enc_img)
    dec_img[:,:,0] = temp[0]
    dec_img[:,:,1] = temp[1]
    dec_img[:,:,2] = temp[2]
    return dec_img