# Gaussian blur
Here is my gaussian blur implementation on python3 from scratch

Currently implemented:
- get scope from image by pixel
- - border solution is extending (https://en.m.wikipedia.org/wiki/Kernel_(image_processing))
- apply weight to scope
- get averaged pixel
- write pixel to array and convert array to image
- show final image and exit

# Usage

**Use with command line arguments:**

`python3 gaussian_blur.py /path/to/image.jpg`

Other formats are probably supported too, since it depends on PIL for image reading.

By default my 5x5 kernel is used. It's crap, honestly, since it doesn't even generate from gaussian equation, just some semi-random numbers i've come up with.

**Use as a module in a script**

```
import gaussian_blur
path = 'image path'
kernel = <your_kernel> # Kernel should be an array of arrays of int values
                       # and should be same lenth by X and by Y

blurred_image = gaussian_blur.blur_image(path, kernel)
blurred_image.show() # Opens a window to show final image
```

__Note, that my implementation is quite slow (mainly because I'm a crap programmer, but also because python3 is slow)__
On big (1900x1200) images, processing may take up to 5 minutes
__I am open to suggestions on how to improve this__
