from PIL import Image
import numpy as np

# Band 3
red19 = Image.open("2019-R.jpg")
array_red19 = np.array(red19, dtype=np.uint8)

# Band 2
green19 = Image.open("2019-G.jpg")
array_green19 = np.array(green19, dtype=np.uint8)

# Thermal Band
tir19 = Image.open("2019-TIR.jpg")
array_tir19 = np.array(tir19, dtype=np.uint8)

# Result Image
image_array = array_red19

# threshold value on thermal band
thres = 200

def thermal_filter(img, g, r, tir, thres):
    for height in range(len(img)):
        for width in range(len(img[0])):
            img[height][width][2] = g[height][width][1]
            img[height][width][1] = r[height][width][0]
            if(tir[height][width][0] >= thres):
                img[height][width][0] = tir[height][width][0]


thermal_filter(image_array, array_green19, array_red19, array_tir19)
image = Image.fromarray(image_array)
image.save("result19.png")
