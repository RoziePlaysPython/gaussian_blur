from sys import argv
from PIL import Image

kernel = [
        [1, 2, 1],
        [2, 4, 2],
        [1, 2, 1],
        ]
scope_size = len(kernel)
# average_dividor = sum([sum([weight for weight in row]) for row in kernel])

# Open image by path and extract nessesary data
def open_image(path):
    image = Image.open(path)
    sizeX, sizeY = image.size[0], image.size[1]
    pixels = image.load()
    return sizeX, sizeY, pixels

# Return scope of image pixels
def modify_scope(X, Y, sizeX, sizeY, pixels, scope_size):
    scope_delta = scope_size//2 # Since we are working with a square scope _around_ the pixels
    scope = []
    row_cnt=0
    for dY in range(-scope_delta, scope_delta+1):
        scope.append([])
        for dX in range(-scope_delta, scope_delta+1):
            tX, tY = dX, dY
            while X+tX < 0:
                tX+=1
            while X+tX > sizeX:
                tX-=1
            while Y+tY < 0:
                tY+=1
            while Y+tY > sizeY:
                tY-=1
            print(dX, dY, 'before extending')
            print(tX, tY, 'after extending')
            scope[row_cnt].append(pixels[Y+tY][X+tX]) # later on this will be changed to pixels[x, y] format
                                                      # due to how pixels object works
        print(row_cnt, scope[row_cnt])
        row_cnt+=1
    return scope # reminder that each pixel in scope is a 3-item array on its own

# Applies weights to scope
# def apply_weight(scope, kernel):
 

 #testing zone

pixels = [
           [0, 1, 2, 3 ],
           [4, 5, 6, 7 ],
           [8, 9, 10,11],
           [12,13,14,15],
         ]
print(modify_scope(0, 0, 3, 3, pixels, 5))

