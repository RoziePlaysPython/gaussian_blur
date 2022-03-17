from PIL import Image

#TODO: generate kernel from a function
kernel = [
        [1, 2, 1],
        [2, 4, 2],
        [1, 2, 1],
        ]
scope_size = len(kernel)
average_dividor = sum([sum([weight for weight in row]) for row in kernel])

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
        print(row_cnt, scope[row_cnt])
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
        print(Y, weighted_scope[Y])
    return weighted_scope


 #testing zone

if __name__=="__main__":
    from sys import argv
    sizeX, sizeY, pixels = open_image(path = argv[1])
    print(apply_weight(modify_scope(0, 0, sizeX, sizeY, pixels, 3), kernel))
