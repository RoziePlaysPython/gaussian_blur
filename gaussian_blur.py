from PIL import Image
from numpy import array, uint8

#TODO: generate kernel from a function
kernel = [
        [1, 2, 1],
        [2, 4, 2],
        [1, 2, 1],
        ]
kernel2 = [
        [1,2,3,2,1],
        [2,3,4,3,2],
        [3,4,5,4,3],
        [2,3,4,3,2],
        [1,2,3,2,1],
        ]
scope_size = len(kernel)
average_divider = sum([sum([weight for weight in row]) for row in kernel])

# Open image by path and extract nessesary data
def open_image(path):
    image = Image.open(path)
    sizeX, sizeY = image.size[0], image.size[1]
    pixels = image.load()
    return sizeX, sizeY, pixels

# Return scope of image pixels
def create_scope(X, Y, sizeX, sizeY, pixels, scope_size):
    scope_delta = scope_size//2 # Since we are working with a square scope _around_ the pixels
    scope = []
    row_cnt=0
    for dY in range(-scope_delta, scope_delta+1):
        scope.append([])
        for dX in range(-scope_delta, scope_delta+1):
            # If searching pixel out of borders, move it to the closest border pixel
            # Usage of "while" allows extendability (if scope>3, still works as intended)
            tX, tY = dX, dY
            while X+tX < 0:
                tX+=1
            while X+tX > sizeX:
                tX-=1
            while Y+tY < 0:
                tY+=1
            while Y+tY > sizeY:
                tY-=1
            # print(dX, dY, 'before extending')
            # print(tX, tY, 'after extending')
            scope[row_cnt].append(pixels[X+tX, Y+tY]) # later on this will be changed to pixels[x, y] format
                                                      # due to how pixels object works
        row_cnt+=1
    return scope # reminder that each pixel in scope is a 3-item array on its own

# Applies weights to scope
def apply_weight(scope, kernel):
    weighted_scope = []
    for Y in range(len(scope)):
        weighted_scope.append([])
        for X in range(len(scope[Y])):
            pixel = scope[Y][X]
            weighted_pixel = tuple([pixel[channel]*kernel[Y][X] for channel in range(len(pixel))])
            weighted_scope[Y].append(weighted_pixel)
    return weighted_scope

def find_average(scope, divider = average_divider):
    summed_pixel = (0, 0, 0)
    for Y in range(len(scope)):
        for X in range(len(scope[Y])):
            summed_pixel = tuple([summed_pixel[i]+scope[Y][X][i] for i in range(len(scope[Y][X]))])
    average_pixel = tuple([summed_pixel[i]//divider for i in range(len(summed_pixel))])
    return average_pixel

def blur_image(path, kernel):
    kernel_size = len(kernel)
    average_divider = sum([sum([weight for weight in row]) for row in kernel])
    sizeX, sizeY, pixels = open_image(path = path)
    sizeX, sizeY = sizeX-1, sizeY-1
    pixel_array = []
    for Y in range(sizeY):
        pixel_array.append([])
        for X in range(sizeX):
            scope = create_scope(X, Y, sizeX, sizeY, pixels, kernel_size)
            weighted_scope = apply_weight(scope, kernel)
            average_pixel = find_average(weighted_scope, average_divider)
            pixel_array[Y].append(average_pixel)
    blurred_image = Image.fromarray(array(pixel_array, dtype = uint8))
    return blurred_image

 #testing zone
if __name__=="__main__":
    from sys import argv
    blur_image(path = argv[1], kernel = kernel2).show()

# I FINISHED IT, FINALLY!!!!!
