from Utils import getRandomOrder, hashOrder, unhashOrder, getRandomFilter, hashFilter, unhashFilter
from Transforms import bitIntensityTransform, reversebitIntensityTransform, spacialTransform, reverseSpacialTransform

def encrypt(img):
    order = getRandomOrder()
    enc_img = bitIntensityTransform(img, order)
    filter = getRandomFilter()
    enc_img = spacialTransform(enc_img, filter)
    hashed_order = hashOrder(order)
    hashed_filter = hashFilter(filter)
    hash = hashed_order+hashed_filter
    
    return enc_img, hash

def decrypt(enc_img, hash):
    filter = unhashFilter(hash[8:len(hash)])
    dec_img = reverseSpacialTransform(enc_img, filter)
    order = unhashOrder(hash[0:8])
    dec_img = reversebitIntensityTransform(dec_img, order)
    return dec_img