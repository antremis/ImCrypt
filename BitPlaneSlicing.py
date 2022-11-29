def getBinary(pixel):
    return format(pixel, 'b').zfill(8)

def getBitPlanes(img):
    data = []
    for pixelRow in img:
        new_pixel_row = []
        for pixel in pixelRow:
            new_pixel_row.append(getBinary(pixel))
        data.append(new_pixel_row)

    planes = []
    for i in range(8):
        pixelData = []
        for pixelRow in data:
            pixels = []
            for pixelBin in pixelRow:
                pixels.append(int(pixelBin[i]))
            pixelData.append(pixels)
        planes.append(pixelData)

    return planes

if __name__ == '__main__':
    print('To be used as an import')